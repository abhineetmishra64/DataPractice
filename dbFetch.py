import configs
import mysql.connector as sql
from jproperties import Properties

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
# cursor.execute("CREATE DATABASE school")

# cursor.execute("SHOW DATABASES")

# for x in cursor:
#     print(x)

# cursor.execute("CREATE TABLE `student` (`id` int NOT NULL AUTO_INCREMENT,`name` varchar(45) NOT NULL,`age` int NOT NULL,`email` varchar(45) NOT NULL,PRIMARY KEY (`id`))")

query = "INSERT INTO student (name,age,email) VALUES (%s,%s,%s)"
value = ("Abhineet", "25", "abhineetmishra64@gmail.com")
cursor.execute(query,value)
print("ROW Inserted")