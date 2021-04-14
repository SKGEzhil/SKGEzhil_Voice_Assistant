import mysql.connector
import mysql

all_objects = []

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="EzHiL2005&&",
    database = "assistant_database"
)
print(db_connection)

def remember(object):
    db_cursor = db_connection.cursor()
    db_cursor.execute("USE assistant_database")
    try:
        sql = """INSERT INTO remember VALUES (%s)"""
        val = (object,)
        db_cursor.execute(sql, val)
        db_connection.commit()
    except Exception as e:
        print(e)

def retrieve(key_word):
    db_cursor = db_connection.cursor()
    db_cursor.execute("""SELECT * FROM remember""")
    for data in db_cursor:
        all_objects.append(data)
    for i in all_objects:
        for word in i:
            if key_word in word:
                if 'I' in word:
                    word = word.replace('I', 'you')
                if 'my' in word:
                    word = word.replace('my', 'your')
                print(word)



retrieve('phone')

