import time
from playsound import playsound
import threading
from datetime import datetime
import playsound

from SKGEzhil_Voice_Assistant.script.database import db_connection

def ring_alarm():
    alarm_list = []
    db_cursor = db_connection.cursor()
    db_cursor.execute("""SELECT * FROM alarms ORDER BY time ASC""")
    for data in db_cursor:
        if data[1] == 'on':
            alarm_list.append(data[0])
    for times in alarm_list:
        print(times)
        times = times.split(':')
        real_hour = int(times[0])
        real_minute = int(times[1])
        alarmH = real_hour
        alarmM = real_minute
        amPm = 'am'
        print("Waiting for the alarm", alarmH, alarmM, amPm)
        if alarmH != 12:
            if (amPm == "pm"):
                alarmH = alarmH + 12
        now = datetime.now()
        d = datetime.now().date()
        later = datetime(d.year, d.month, d.day, alarmH, alarmM, 0)
        difference = (later - now)
        total_sec = difference.total_seconds()
        def alarm_func():
            from SKGEzhil_Voice_Assistant.script import current_time
            print('ringing')
            systime = f'{current_time.hours()}:{current_time.minutes()}'
            print(f'{current_time.hours()}:{current_time.minutes()}')
            #playsound.playsound('../alarm.mp3', True)
            try:
                db_cursor.execute(f"UPDATE alarms SET activestatus = 'off' WHERE time = '{current_time.hours()}:{current_time.minutes()}'")
                db_connection.commit()
            except Exception as e:
                print(e)
        timer = threading.Timer(total_sec, alarm_func)
        timer.start()

def set_alarm(hours, minutes):
    alarm_time = f'{hours}:{minutes}'
    db_cursor = db_connection.cursor()
    db_cursor.execute("USE assistant_database")
    sql = """INSERT INTO alarms VALUES (%s, %s)"""
    val = (alarm_time, 'on')
    db_cursor.execute(sql, val)
    db_connection.commit()





