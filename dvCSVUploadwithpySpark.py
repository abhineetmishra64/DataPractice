from pyspark.sql import SparkSession
import mysql.connector as sql
from jproperties import Properties

spark = SparkSession.builder\
    .appName('Abhineet').getOrCreate()

df_pyspark = spark.read.csv('department.csv', header=True, inferSchema=True)

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

