from pyspark.sql import SparkSession
import mysql.connector as sql
from jproperties import Properties

spark = SparkSession.builder\
    .appName('Abhineet').getOrCreate()

df_pyspark = spark.read.csv('Book1.csv', header=True, inferSchema=True)

config = Properties()
with open('app-config.properties', 'rb') as config_file:
    config.load(config_file)
prop_view = config.items()

connection = sql.connect(
    host=config.get("DB_HOST").data,
    user=config.get("DB_User").data,
    password=config.get("DB_PWD").data,
    database=config.get("DB_NAME").data
)
cursor = connection.cursor()

query = "SELECT * FROM department"
cursor.execute(query)

record = cursor.fetchall()
print(record)

# for i,row in df_pyspark:
#     queryForInsert = "INSERT INTO student(name, age, email) VALUES(%s,%s,%s)"
#     cursor.execute(queryForInsert,tuple(row))
#     connection.commit()

print(df_pyspark.show())