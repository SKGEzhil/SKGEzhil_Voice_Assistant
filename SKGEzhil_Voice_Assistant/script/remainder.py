import threading
from datetime import datetime

from SKGEzhil_Voice_Assistant.script import current_time
from SKGEzhil_Voice_Assistant.script import speech_engine
from SKGEzhil_Voice_Assistant.script.database import cloud_mysql_connection, local_mysql_connection, sqlite_connection


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
        # remainder = input('what in the remainder for? ')
        from SKGEzhil_Voice_Assistant.script.speech_engine import take_command
        remainder = take_command()
    remaind(remainder, timing)
    print(f'Remainder set for {timing}')
    speech_engine.talk(f'Remainder set for {timing}')
    global reminder
    reminder = subject
    remainder_alarm()


def remaind(remainder, time):
    local_mysql_cursor = local_mysql_connection.cursor()
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
            sqlite = """INSERT INTO remainders VALUES(?, ?, ?)"""
            val = (remaind_time, 'on', remainder)
            db_cursor = cloud_mysql_connection.cursor()
            sqlite_cursor = sqlite_connection.cursor()
            sqlite_cursor.execute(sqlite, val)
            db_cursor.execute(sql, val)
            cloud_mysql_connection.commit()
            local_mysql_cursor.execute(sql, val)
            local_mysql_connection.commit()
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
            sqlite = """INSERT INTO remainders VALUES(?, ?, ?)"""
            val = (remaind_time, 'on', remainder)
            db_cursor = cloud_mysql_connection.cursor()
            sqlite_cursor = sqlite_connection.cursor()
            sqlite_cursor.execute(sqlite, val)
            db_cursor.execute(sql, val)
            cloud_mysql_connection.commit()
            local_mysql_cursor.execute(sql, val)
            local_mysql_connection.commit()
    elif 'hours' in time:
        if 'minutes' not in time:
            time = time.replace(' hours', '')
            remaind_hours = current_time.hours() + int(time)
            remaind_minutes = current_time.minutes()
            remaind_time = f'{remaind_hours}:{remaind_minutes}'
            sql = """INSERT INTO remainders VALUES(%s, %s, %s)"""
            sqlite = """INSERT INTO remainders VALUES(?, ?, ?)"""
            val = (remaind_time, 'on', remainder)
            db_cursor = cloud_mysql_connection.cursor()
            sqlite_cursor = sqlite_connection.cursor()
            sqlite_cursor.execute(sqlite, val)
            db_cursor.execute(sql, val)
            cloud_mysql_connection.commit()
            local_mysql_cursor.execute(sql, val)
            local_mysql_connection.commit()


def remainder_alarm():
    remainder_list = []
    sqlite_cursor = sqlite_connection.cursor()
    cloud_mysql_cursor = cloud_mysql_connection.cursor()
    local_mysql_cursor = local_mysql_connection.cursor()
    sqlite_cursor.execute("""SELECT * FROM alarms ORDER BY time ASC""")
    for data in sqlite_cursor:
        if data[1] == 'on':
            remainder_list.append(data[0])
    for times in remainder_list:
        print(times)
        times = times.split(':')
        real_hour = int(times[0])
        real_minute = int(times[1])
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
            from SKGEzhil_Voice_Assistant.script.mail import send_mail
            from SKGEzhil_Voice_Assistant.script import config
            send_mail('Reminder', f'Here is your remainder {reminder}', f'{config.gmail_id}', f'{config.gmail_id}')
            from SKGEzhil_Voice_Assistant.script import current_time
            print('ringing')
            systime = f'{current_time.hours()}:{current_time.minutes()}'
            print(f'{current_time.hours()}:{current_time.minutes()}')
            print(f'Here is your remainder {reminder}')
            speech_engine.talk(f'Here is your remainder {reminder}')
            sqlite_cursor = sqlite_connection.cursor()
            cloud_mysql_cursor = cloud_mysql_connection.cursor()
            local_mysql_cursor = local_mysql_connection.cursor()
            cloud_mysql_cursor.execute(
                f"UPDATE alarms SET activestatus = 'off' WHERE time = '{current_time.hours()}:{current_time.minutes()}'")
            cloud_mysql_connection.commit()
            sqlite_cursor.execute(
                f"UPDATE alarms SET activestatus = 'off' WHERE time = '{current_time.hours()}:{current_time.minutes()}'")
            sqlite_connection.commit()
            local_mysql_cursor.execute(
                f"UPDATE alarms SET activestatus = 'off' WHERE time = '{current_time.hours()}:{current_time.minutes()}'")
            local_mysql_cursor.commit()

        timer = threading.Timer(total_sec, alarm_func)
        timer.start()
