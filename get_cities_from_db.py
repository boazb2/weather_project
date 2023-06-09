import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host='cnt7-naya-cdh63',
    user='nifi',
    password='NayaPass1!',
    database='weather_db'
)
def get_cities_array (query):
# Fetch data into a pandas DataFrame
    df =  pd.read_sql_query(query, conn)
    return df['city_name'].values

def get_users_cities (query):
    df = pd.read_sql_query(query,conn)
    return df

df2 = get_cities_array("SELECT distinct city_name FROM users_cities")

#print(df2)