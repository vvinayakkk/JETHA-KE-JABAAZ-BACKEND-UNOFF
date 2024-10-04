import psycopg2

try:
    connection = psycopg2.connect(
        database="your_database_name",
        user="your_username",
        password="your_password",
        host="aws-0-ap-south-1.pooler.supabase.com",
        port="6543"
    )
    print("Connection successful")
except Exception as e:
    print("Error connecting to the database:", e)
finally:
    if connection:
        connection.close()
