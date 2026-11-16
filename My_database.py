# 1. Import SQLite library
import sqlite3

# 2. Create or connect to a database
conn = sqlite3.connect("my_database.db")

# 3. Create a cursor to execute SQL
cursor = conn.cursor()

# 4. Create a table
cursor.execute("""
    create table if not exists users (
        id integer primary key,
        name text
    )
""")

# 5. Insert data
cursor.execute(
    "insert into users (name) values (?)",
    ("Alice",)
)

# 6. Save changes
conn.commit()

# 7. Read data
cursor.execute("select * from users")
print(cursor.fetchall())

# 8. Close connection
conn.close()