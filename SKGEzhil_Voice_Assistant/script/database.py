import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="EzHiL2005&&"
)
print(db_connection)
# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()
db_cursor.execute("USE assistant_database")
db_cursor.execute("CREATE TABLE alarms (time varchar(10))")
db_cursor.execute("CREATE TABLE reminders (time varchar(10))")
db_cursor.execute("CREATE TABLE remember (object varchar(1000))")
db_cursor.execute("SHOW TABLES")
for db in db_cursor:
    print(db)