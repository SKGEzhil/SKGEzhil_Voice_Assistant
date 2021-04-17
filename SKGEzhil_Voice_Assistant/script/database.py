import sqlite3

import mysql.connector

from SKGEzhil_Voice_Assistant.script import config

cloud_mysql_connection = mysql.connector.connect(
    host="SG-SKGEzhil-4178-mysql-master.servers.mongodirector.com",
    user="sgroot",
    passwd=config.cloud_mysql_password,
    database="assistant_database"
)
print(cloud_mysql_connection)

local_mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=config.mysql_password,
    database="assistant_database"
)
print(local_mysql_connection)

sqlite_connection = sqlite3.connect('../assistant_db.sqlite')
print(sqlite_connection)
