###    pip install snowflake-connector-python


import snowflake.connector

# Create a connection object
conn = snowflake.connector.connect(
    user='your_username',
    password='your_password',
    account='your_account_identifier',
    warehouse='your_warehouse',
    database='your_database',
    schema='your_schema'
)

# Create a cursor object
cursor = conn.cursor()

try:
    # Execute a query
    cursor.execute("SELECT CURRENT_VERSION()")
    
    # Fetch the result
    result = cursor.fetchone()
    print(f"Snowflake version: {result[0]}")

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
