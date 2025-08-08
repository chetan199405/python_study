import psycopg2
from psycopg2 import sql

# Configuration - replace with your PostgreSQL credentials
DB_CONFIG = {
    'dbname': 'contacts_db',
    'user': 'postgres',
    'password': 'yourpassword',
    'host': 'localhost',
    'port': '5432'
}

def create_connection():
    """Step 1: Establish a connection to PostgreSQL database"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Connected to PostgreSQL database successfully!")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def create_table(conn):
    """Step 2: Create contacts table if it doesn't exist"""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        mobile_number VARCHAR(20) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
        print("Table created successfully or already exists")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")

def add_contact(conn, name, mobile_number):
    """Step 3: Add a new contact to the database"""
    insert_query = sql.SQL("""
    INSERT INTO contacts (name, mobile_number)
    VALUES (%s, %s)
    RETURNING id;
    """)
    
    try:
        cursor = conn.cursor()
        cursor.execute(insert_query, (name, mobile_number))
        contact_id = cursor.fetchone()[0]
        conn.commit()
        print(f"Contact added successfully with ID: {contact_id}")
        return contact_id
    except psycopg2.Error as e:
        print(f"Error adding contact: {e}")
        return None

def main():
    """Main function to handle the program flow"""
    # Step 1: Create database connection
    conn = create_connection()
    if not conn:
        return
    
    # Step 2: Create table
    create_table(conn)
    
    # Step 3: Get user input
    print("\n==== Add New Contact ====")
    name = input("Enter name: ").strip()
    mobile_number = input("Enter mobile number: ").strip()
    
    # Step 4: Add contact to database
    add_contact(conn, name, mobile_number)
    
    # Step 5: Close connection
    conn.close()
    print("\nConnection closed. Goodbye!")

if __name__ == "__main__":
    main()


Key Steps Explained:
Database Connection

Uses psycopg2.connect() with connection parameters
Handles potential connection errors
Always close the connection when done
Table Creation

Creates a table with proper data types:
SERIAL for auto-incrementing ID
VARCHAR for text fields with length limits
TIMESTAMP for creation record
Data Insertion

Uses parameterized queries with %s placeholders to prevent SQL injection
Returns the newly created ID using RETURNING id
Commits changes explicitly for data persistence
User Input

Simple command-line interface to collect contact details
Input validation could be added
Security Best Practices

Uses psycopg2.sql for safe SQL composition
Parameterized queries prevent SQL injection
Credentials are managed in a configuration dictionary
Prerequisites:
Install PostgreSQL and create database contacts_db
Install psycopg2: pip install psycopg2-binary
Update DB_CONFIG with your credentials
This implementation includes:

Error handling for database operations
Proper connection management
Basic input validation (strip whitespace)
Auto-timestamping
Safe SQL query construction
The script can be easily extended with features like:

Multiple contact entry
Input validation for phone numbers
Updating existing contacts
Listing all contacts

Bookmark message
Copy message
