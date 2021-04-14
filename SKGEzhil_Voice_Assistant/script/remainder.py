from SKGEzhil_Voice_Assistant.script import current_time
from datetime import datetime
import mysql.connector
import mysql
import pyttsx3
import threading
from SKGEzhil_Voice_Assistant.script import speech_engine
from SKGEzhil_Voice_Assistant.script import config

from SKGEzhil_Voice_Assistant.script.database import db_connection


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def remainder_command(command):
    if ' in ' in command:
        command = command.split(' in ')
    elif ' after ' in command:
        command = command.split(' after ')
    elif ' for ' in command:
        command = command.split(' for ')
    subject = command[0]
    timing = command[1]
    if 'to' in subject:
        subject = subject.split('to')
        remainder = subject[1]
    else:
        speech_engine.talk('what is the remainder for?')
        remainder = input('what in the remainder for? ')
    remaind(remainder,timing)
    print(f'Remainder set for {timing}')
    speech_engine.talk(f'Remainder set for {timing}')
    remainder_alarm()


def remaind(remainder,time):
    if 'minutes' in time:
        if 'hour' not in time:
            time = time.replace(' minutes', '')
            remaind_hours = current_time.hours()
            remaind_minutes = current_time.minutes() + int(time)
            if remaind_minutes > 60:
                remaind_minutes = remaind_minutes - 60
                remaind_hours = remaind_hours + 1
            remaind_time = f'{remaind_hours}:{remaind_minutes}'
            sql = """INSERT INTO remainders VALUES(%s, %s, %s)"""
            val = (remaind_time, 'on', remainder)
            db_cursor = db_connection.cursor()
            db_cursor.execute(sql,val)
            db_connection.commit()
        else:
            time = time.replace(' hours', '')
            time = time.replace(' minutes', '')
            time = time.split(' ')
            hours = time[0]
            minutes = time[1]
            remaind_hours = current_time.hours() + int(hours)
            remaind_minutes = current_time.minutes() + int(minutes)
            if remaind_minutes > 60:
                remaind_minutes = remaind_minutes - 60
                remaind_hours = remaind_hours + 1
            remaind_time = f'{remaind_hours}:{remaind_minutes}'
            sql = """INSERT INTO remainders VALUES(%s, %s, %s)"""
            val = (remaind_time, 'on', remainder)
            db_cursor = db_connection.cursor()
            db_cursor.execute(sql, val)
            db_connection.commit()
    elif 'hours' in time:
        if 'minutes' not in time:
            time = time.replace(' hours', '')
            remaind_hours = current_time.hours() + int(time)
            remaind_minutes = current_time.minutes()
            remaind_time = f'{remaind_hours}:{remaind_minutes}'
            sql = """INSERT INTO remainders VALUES(%s, %s, %s)"""
            val = (remaind_time, 'on', remainder)
            db_cursor = db_connection.cursor()
            db_cursor.execute(sql, val)
            db_connection.commit()

def remainder_alarm():
    remainder_list = []
    db_cursor = db_connection.cursor()
    db_cursor.execute("""SELECT * FROM remainders ORDER BY time ASC""")
    for data in db_cursor:
        if data[1] == 'on':
            remainder_list.append(data[0])
    for times in remainder_list:
        print(times)
        times = times.split(':')
        real_hour = int(times[0])
        real_minute = int(times[1])
        alarmH = real_hour
        alarmM = real_minute
        amPm = 'pm'
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
            db_cursor = db_connection.cursor()
            db_cursor.execute(f"UPDATE remainders SET activestatus = 'off' WHERE time = '{current_time.hours()}:{current_time.minutes()}'")
            db_connection.commit()
            print('Here is your remainder')
            speech_engine.talk('Here is your remainder')
            # playsound.playsound('../alarm.mp3', True)


        timer = threading.Timer(total_sec, alarm_func)
        timer.start()



