#Database Integration (Postgres)

#Postgres module
#Connecting, inserting, querying

#We’ll use the most popular library for PostgreSQL in Python:
#psycopg2
#It’s a PostgreSQL adapter for Python.

# Installing psycopg2
#pip install psycopg2-binary

#psycopg2-binary is recommended for beginners (includes compiled binaries).
#For production: use psycopg2 and compile from source.

#Connecting to PostgreSQL

import psycopg2

# Connection details
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="mydb",
    user="postgres",
    password=1234,
)

print("Connected successfully!")

# Always create a cursor to execute queries
cur = conn.cursor()

#Inserting Data
query = "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)"
data = ("Alice", "IT", 75000)

cur.execute(query, data)
conn.commit()  # Save changes

print("Data inserted successfully.")

# Querying Data
cur.execute("SELECT * FROM employees")
rows = cur.fetchall()

for row in rows:
    print(row)

#Fetch one row:
cur.execute("SELECT * FROM employees WHERE name = %s", ("Alice",))
row = cur.fetchone()
print(row)


#Full Example: Connect, Insert, Query
import psycopg2

try:
    # Step 1: Connect
    conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="postgres",
        password="1234"
    )
    cur = conn.cursor()

    # Step 2: Insert data
    cur.execute(
        "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)",
        ("Bob", "HR", 60000)
    )
    conn.commit()

    # Step 3: Query
    cur.execute("SELECT * FROM employees")
    for row in cur.fetchall():
        print(row)

except Exception as e:
    print("Error:", e)

finally:
    cur.close()
    conn.close()


#Tips & Best Practices
#Tip	                                              Why
#Use with conn.cursor() as cur:	                      Automatically closes the cursor
#Use try-except blocks	                              Handle DB errors safely
#Use .fetchone() or .fetchall()	                      Retrieve query results
#Always commit() after INSERT/UPDATE/DELETE	          Save changes
#Use connection pools in production	Efficient         handling of many users