import pandas as pd
import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='cnt7-naya-cdh63',
    user='nifi',
    password='NayaPass1!',
    database='weather_db'
)

# Query to fetch data from the table
query = "SELECT * FROM users"

# Fetch data into a pandas DataFrame
df = pd.read_sql_query(query, conn)

print(df)
