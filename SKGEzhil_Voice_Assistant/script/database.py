import mysql.connector

from SKGEzhil_Voice_Assistant.script import config

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=config.mysql_password,
    database="assistant_database"
)
print(db_connection)
