import mysql.connector as sql
from jproperties import Properties
import pandas as pd

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

pd_csv = pd.read_csv('department.csv', index_col=False, delimiter=',')
print(pd_csv)

cursor.execute("CREATE TABLE IF NOT EXISTS `department`(`id` int NOT NULL AUTO_INCREMENT,`name` varchar(45) NOT NULL,`departments` varchar(45) NOT NULL,`salary` int NOT NULL,PRIMARY KEY (`id`))")

for i,row in pd_csv.iterrows():
    query = "INSERT INTO department(name, departments, salary) VALUES(%s,%s,%s)"
    cursor.execute(query, tuple(row))
    connection.commit()

# query = "INSERT INTO department(name, departments, salary) VALUES(%s,%s,%s)"
# values = (df_pyspark.select("Name"), df_pyspark.select("Departments"), df_pyspark.select("Salary"))
# cursor.execute(query,values)
# connection.commit()
