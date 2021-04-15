import mysql.connector

from SKGEzhil_Voice_Assistant.script import config

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="EzHiL2005",
    database="assistant_database"
)
print(db_connection)
