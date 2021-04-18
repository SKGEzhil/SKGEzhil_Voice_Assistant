import threading
from datetime import datetime
from threading import Lock

from SKGEzhil_Voice_Assistant.script import current_time
from SKGEzhil_Voice_Assistant.script import speech_engine
from SKGEzhil_Voice_Assistant.script.database import sqlite_connection

lock = Lock()

sqlite_cursor = sqlite_connection.cursor()


def create_reminder(command):
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
        # speech_engine.talk('what is the remainder for?')
        remainder = input('what in the remainder for? ')
        # remainder = take_command()
    remind(remainder, timing)
    print(f'Remainder set for {timing}')
    speech_engine.talk(f'Remainder set for {timing}')
    reminder_alarm()


def remind(remainder, time):
    if 'minutes' in time:
        if 'hour' not in time:
            time = time.replace(' minutes', '')
            remind_hours = current_time.hours()
            remind_minutes = current_time.minutes() + int(time)
            if remind_minutes > 60:
                remind_minutes = remind_minutes - 60
                remind_hours = remind_hours + 1
            remind_time = f'{remind_hours}:{remind_minutes}'
            sql = """INSERT INTO remainders VALUES(%s, %s, %s)"""
            sqlite = """INSERT INTO remainders VALUES(?, ?, ?)"""
            val = (remind_time, 'on', remainder)
            sqlite_cursor.execute(sqlite, val)
            sqlite_connection.commit()
        else:
            time = time.replace(' hours', '')
            time = time.replace(' minutes', '')
            time = time.split(' ')
            hours = time[0]
            minutes = time[1]
            remind_hours = current_time.hours() + int(hours)
            remind_minutes = current_time.minutes() + int(minutes)
            if remind_minutes > 60:
                remind_minutes = remind_minutes - 60
                remind_hours = remind_hours + 1
            remind_time = f'{remind_hours}:{remind_minutes}'
            sql = """INSERT INTO remainders VALUES(%s, %s, %s)"""
            sqlite = """INSERT INTO remainders VALUES(?, ?, ?)"""
            val = (remind_time, 'on', remainder)
            sqlite_cursor.execute(sqlite, val)
            sqlite_connection.commit()
    elif 'hours' in time:
        if 'minutes' not in time:
            time = time.replace(' hours', '')
            remind_hours = current_time.hours() + int(time)
            remind_minutes = current_time.minutes()
            remind_time = f'{remind_hours}:{remind_minutes}'
            sql = """INSERT INTO remainders VALUES(%s, %s, %s)"""
            sqlite = """INSERT INTO remainders VALUES(?, ?, ?)"""
            val = (remind_time, 'on', remainder)
            sqlite_cursor.execute(sqlite, val)
            sqlite_connection.commit()


exact_reminder = ''


def reminder_alarm():
    remainder_list = []
    sqlite_cursor.execute("""SELECT * FROM remainders ORDER BY time ASC""")
    for data in sqlite_cursor:
        if data[1] == 'on':
            remainder_list.append(f'{data[0]}_{data[2]}')
    for reminders in remainder_list:
        print(reminders)
        reminders = reminders.split('_')
        times = reminders[0]
        times = times.split(':')
        real_hour = int(times[0])
        real_minute = int(times[1])
        exact_reminder = reminders[1]
        print(exact_reminder)
        alarm_h = real_hour
        alarm_m = real_minute
        am_pm = 'pm'
        print("Waiting for the alarm", alarm_h, alarm_m, am_pm)
        now = datetime.now()
        d = datetime.now().date()
        later = datetime(d.year, d.month, d.day, alarm_h, alarm_m, 0)
        difference = (later - now)
        total_sec = difference.total_seconds()

        def alarm_func():

            from SKGEzhil_Voice_Assistant.script import current_time
            print('ringing')
            systime = f'{current_time.hours()}:{current_time.minutes()}'
            print(f'{current_time.hours()}:{current_time.minutes()}')
            print(f'Here is your remainder {exact_reminder}')
            from SKGEzhil_Voice_Assistant.script.speech_engine import talk
            print(exact_reminder)
            talk(f'Here is your remainder.  {exact_reminder}')
            print(id(sqlite_cursor))
            try:
                lock.acquire(True)
                sqlite_cursor.execute(
                    f"UPDATE remainders SET activestatus = 'off' WHERE time = "
                    f"'{current_time.hours()}:{current_time.minutes()}'")
                sqlite_connection.commit()
            finally:
                lock.release()

        timer = threading.Timer(total_sec, alarm_func)
        timer.start()
