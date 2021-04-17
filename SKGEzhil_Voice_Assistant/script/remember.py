all_objects = []

from SKGEzhil_Voice_Assistant.script.database import cloud_mysql_connection, local_mysql_connection, sqlite_connection


def remember(remember_object):
    local_mysql_cursor = local_mysql_connection.cursor()
    sqlite_cursor = sqlite_connection.cursor()
    db_cursor = cloud_mysql_connection.cursor()
    db_cursor.execute("USE assistant_database")
    try:
        sql = """INSERT INTO remember VALUES (%s)"""
        sqlite = """INSERT INTO remember VALUES (%s)"""
        val = (remember_object,)
        db_cursor.execute(sql, val)
        cloud_mysql_connection.commit()
        sqlite_cursor.execute(sqlite, val)
        sqlite_connection.commit()
        local_mysql_cursor.execute(sql, val)
        local_mysql_connection.commit()
    except Exception as e:
        print(e)


def retrieve(key_word):
    db_cursor = cloud_mysql_connection.cursor()
    sqlite_cursor = sqlite_connection.cursor()
    sqlite_cursor.execute("""SELECT * FROM remember""")
    for data in sqlite_cursor:
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
