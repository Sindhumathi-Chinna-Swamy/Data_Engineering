
# %% CELL 1 - IMPORTED LIBRARIES

import pandas as pd
import sqlite3


# %% CELL 2 - LOADED RAW DATA INTO SQLITE

# Read the existing CSV file
sales_df = pd.read_csv("sales.csv")

# Connected to SQLite database
conn = sqlite3.connect("my_database.db")

# Loaded CSV into the raw table
sales_df.to_sql("raw_sales", conn, if_exists="replace", index=False)

print("Raw Records:", len(sales_df))


# %% CELL 3 - READ SQLITE DATA INTO PANDAS

# Read the raw sales table
df = pd.read_sql("select * from raw_sales", conn)

# Displayed the data
print(df.head())
print("Total Records:", len(df))


# %% CELL 4 - DATA PROFILING

# Checked data structure
df.info()

# Checked missing values
print("Missing Values:")
print(df.isnull().sum())

# Checked duplicate records
print("Duplicates:", df.duplicated().sum())

# Displayed column names
print("Columns:", df.columns.tolist())


# %% DATA PREPROCESSING AND VALIDATION

# Created a copy of the raw data
clean_df = df.copy()

# Removed duplicate records
clean_df = clean_df.drop_duplicates()

# Removed extra spaces from product names
clean_df["product"] = clean_df["product"].str.strip()

# Separated valid and rejected sales
curated_df = clean_df[clean_df["amount"] > 0].copy()
rejected_df = clean_df[clean_df["amount"] <= 0].copy()

# Displayed validation results
print("Valid Records:", len(curated_df))
print("Rejected Records:", len(rejected_df))


# %% DATA LOADING - SQLITE3

# Loaded cleaned data into SQLite
curated_df.to_sql("curated_sales", conn, if_exists="replace", index=False)

# Loaded rejected records into SQLite
rejected_df.to_sql("rejected_sales", conn, if_exists="replace", index=False)

# Verified loaded records
print(pd.read_sql("select * from curated_sales", conn))

# Closed the database connection
conn.close()

print("SQLite ETL Pipeline Completed!")
