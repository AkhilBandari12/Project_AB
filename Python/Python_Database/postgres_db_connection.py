import psycopg2
from psycopg2 import sql

# Define the connection parameters
conn_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port'
}

try:
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(**conn_params)
    cursor = connection.cursor()

    # Execute a sample query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Connected to - {db_version}")

    # Close the cursor and connection
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error connecting to PostgreSQL database: {error}")
