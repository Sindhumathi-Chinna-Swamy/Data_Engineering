
# %% IMPORTED LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sqlalchemy import create_engine, text
from getpass import getpass

# %% CONNECTED TO POSTGRESQL

# Collected PostgreSQL connection details
db_user = input("PostgreSQL Username: ")
db_name = input("Database Name: ")
db_password = getpass("PostgreSQL Password: ")

# Created PostgreSQL database connection
engine = create_engine(
    "postgresql+psycopg://",
    connect_args={
        "user": db_user,
        "password": db_password,
        "dbname": db_name,
        "host": "localhost",
        "port": 5432
    }
)

# Tested the database connection
with engine.connect() as conn:
    result = conn.execute(text("select current_database()"))
    print("Connected to:", result.scalar())


# %% DATA INGESTION (EXTRACT)

# Identified the raw data folder
raw_dir = Path("/Users/sandy/Desktop/RawDatafolder")

# Loaded CSV, JSON, and Excel datasets
orders_df = pd.read_csv(raw_dir / "orders.csv")
customers_df = pd.read_json(raw_dir / "customers.json")
products_df = pd.read_excel(raw_dir / "products.xlsx")

# Verified the dataset sizes
print("Orders:", orders_df.shape)
print("Customers:", customers_df.shape)
print("Products:", products_df.shape)


# %% DATA EXPLORATION (PROFILING)

# Explored the datasets
for name, df in {
    "Orders": orders_df,
    "Customers": customers_df,
    "Products": products_df
}.items():
    print(f"\n{name}")
    print(df.head())
    df.info()
    print(df.describe())
    print("Missing Values:\n", df.isnull().sum())
    print("Duplicates:", df.duplicated().sum())


# %% CLEANED CUSTOMERS

# Created a copy of customer data
customers_clean = customers_df.copy()

# Filled missing cities and standardized text
customers_clean["city"] = customers_clean["city"].fillna("Unknown").str.strip().str.title()
customers_clean["customer_name"] = customers_clean["customer_name"].str.strip().str.title()

# Removed duplicate customers
customers_clean = customers_clean.drop_duplicates()

print("Clean Customers:", len(customers_clean))


# %% CLEANED ORDERS

# Created a copy of orders data
orders_clean = orders_df.copy()

# Converted dates and quantities
orders_clean["order_date"] = pd.to_datetime(
    orders_clean["order_date"], format="mixed", errors="coerce"
)
orders_clean["quantity"] = pd.to_numeric(
    orders_clean["quantity"], errors="coerce"
)

# Standardized status and IDs
orders_clean["status"] = orders_clean["status"].str.strip().str.upper().replace(
    {"COMPLETE": "COMPLETED"}
)
orders_clean["customer_id"] = orders_clean["customer_id"].str.strip()
orders_clean["product_id"] = orders_clean["product_id"].str.strip()

# Removed duplicate orders
orders_clean = orders_clean.drop_duplicates()

# Separated valid and rejected orders
valid_orders = orders_clean[
    orders_clean["order_date"].notna() &
    (orders_clean["quantity"] > 0) &
    (orders_clean["quantity"] % 1 == 0)
].copy()

rejected_orders = orders_clean.drop(valid_orders.index)

print("Valid Orders:", len(valid_orders))
print("Rejected Orders:", len(rejected_orders))


# %% CLEANED PRODUCTS

# Created a copy and converted prices
products_clean = products_df.copy()
products_clean["unit_price"] = pd.to_numeric(
    products_clean["unit_price"], errors="coerce"
)

# Separated valid and rejected products
valid_products = products_clean[
    products_clean["unit_price"] > 0
].drop_duplicates().copy()

rejected_products = products_clean[
    products_clean["unit_price"].isna() |
    (products_clean["unit_price"] <= 0)
].copy()

print("Valid Products:", len(valid_products))
print("Rejected Products:", len(rejected_products))


# %% MERGED ALL THREE TABLES

# Joined orders, customers, and products
sales_df = valid_orders.merge(
    customers_clean, on="customer_id",
    how="left", validate="many_to_one"
)

sales_df = sales_df.merge(
    valid_products, on="product_id",
    how="left", validate="many_to_one"
)

# Checked merged records and missing matches
print("Merged Orders:", len(sales_df))
print("Unmatched Customers:", sales_df["customer_name"].isna().sum())
print("Unmatched Products:", sales_df["unit_price"].isna().sum())


# %% CALCULATED REVENUE - Transformation

# Selected completed orders with valid customers and products
sales_valid = sales_df[
    (sales_df["status"] == "COMPLETED") &
    sales_df["customer_name"].notna() &
    sales_df["unit_price"].notna()
].copy()

# Calculated sales amount
sales_valid["sales_amount"] = sales_valid["quantity"] * sales_valid["unit_price"]

# Displayed revenue
print("Total Revenue:", sales_valid["sales_amount"].sum())
print("Completed Orders:", len(sales_valid))


# %% AGGREGATED SALES DATA - Transformation

# Calculated revenue by category, date, and city
category_sales = sales_valid.groupby("category")["sales_amount"].sum()
daily_sales = sales_valid.groupby("order_date")["sales_amount"].sum()
city_sales = sales_valid.groupby("city")["sales_amount"].sum()

# Displayed sales summaries
print(category_sales)
print(daily_sales)
print(city_sales)

# %% NUMPY - MEAN, MEDIAN AND STANDARD DEVIATION

# Calculated statistics for sales revenue
data = sales_valid["sales_amount"]

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))

# %% SAVED PROCESSED DATA

# Created the processed data folder
output_dir = raw_dir / "processed"
output_dir.mkdir(exist_ok=True)

# Saved cleaned and aggregated data
sales_valid.to_csv(output_dir / "sales_enriched.csv", index=False)
category_sales.to_csv(output_dir / "category_sales.csv")
daily_sales.to_csv(output_dir / "daily_sales.csv")
city_sales.to_csv(output_dir / "city_sales.csv")

# Saved rejected records
rejected_orders.to_csv(output_dir / "rejected_orders.csv", index=False)
rejected_products.to_csv(output_dir / "rejected_products.csv", index=False)

print("Data Loading Completed!")


# %% CREATED FOUR GRAPHS

# Created the graphs folder
graphs_dir = output_dir / "graphs"
graphs_dir.mkdir(exist_ok=True)

# Defined the four graphs
charts = [
    (category_sales, "bar", "Revenue by Category", "category_sales.png"),
    (daily_sales, "line", "Daily Revenue", "daily_sales.png"),
    (category_sales, "pie", "Revenue Distribution", "revenue_distribution.png"),
    (sales_valid["sales_amount"], "hist", "Order Values", "order_distribution.png")
]

# Created, saved, and displayed each graph
for data, chart_type, title, filename in charts:
    plt.figure()

    data.plot(kind=chart_type, title=title)

    plt.tight_layout()
    plt.savefig(graphs_dir / filename)
    plt.show()

print("All Four Graphs Saved!")


# %% CREATED AUDIT TABLE

# Created the audit table if it did not exist
with engine.begin() as conn:
    conn.execute(text("""
        create table if not exists pipeline_audit (
            audit_id bigint generated always as identity primary key,
            pipeline_name varchar(100),
            table_name varchar(100),
            execution_time timestamp default current_timestamp,
            records_loaded integer,
            total_revenue numeric(12, 2),
            status varchar(20)
        )
    """))

    # Added table_name if an older audit table already existed
    conn.execute(text("""
        alter table pipeline_audit
        add column if not exists table_name varchar(100)
    """))

print("Pipeline Audit Table Created!")


# %% LOADED CURATED DATA WITH AUDIT LOGGING

# Created a reusable function to load and audit data
def load_to_postgres(df, table_name):
    with engine.begin() as conn:

        # Loaded curated data into PostgreSQL
        df.to_sql(table_name, conn, if_exists="replace", index=False)

        # Recorded the successful load in the audit table
        conn.execute(text("""
            insert into pipeline_audit
            (pipeline_name, table_name, records_loaded, total_revenue, status)
            values (:pipeline, :table, :rows, :revenue, :status)
        """), {
            "pipeline": "retail_sales_etl",
            "table": table_name,
            "rows": len(df),
            "revenue": float(df["sales_amount"].sum()) if "sales_amount" in df.columns else None,
            "status": "SUCCESS"
        })

    print(f"{table_name}: {len(df)} records loaded")


# Loaded all four curated datasets
load_to_postgres(sales_valid, "curated_sales")
load_to_postgres(category_sales.reset_index(), "category_sales")
load_to_postgres(daily_sales.reset_index(), "daily_sales")
load_to_postgres(city_sales.reset_index(), "city_sales")

