import threading
from datetime import datetime

from SKGEzhil_Voice_Assistant.script.database import cloud_mysql_connection, local_mysql_connection, sqlite_connection
from SKGEzhil_Voice_Assistant.script.speech_engine import talk


def create_alarm(command):
    if ' every day ' in command:
        command = command.replace(' every day ', '')
        every_day = True
    elif ' every day' in command:
        command = command.replace(' every day', '')
        every_day = True
    else:
        every_day = False

    if ' at ' in command:
        command = command.split(' at ')
        alarm_time = command[1]
        if 'pm' in alarm_time:
            ampm = 'pm'
            alarm_time = alarm_time.replace('pm', '')
        else:
            ampm = 'am'
            alarm_time = alarm_time.replace('am', '')

    elif 'at ' in command:
        command = command.split('at ')
        alarm_time = command[1]
        if 'pm' in alarm_time:
            ampm = 'pm'
            alarm_time = alarm_time.replace('pm', '')
        else:
            ampm = 'am'
            alarm_time = alarm_time.replace('am', '')
    else:
        talk('At what time?')
        alarm_time = input('At what time? ')
        if 'pm' in alarm_time:
            ampm = 'pm'
            alarm_time = alarm_time.replace('pm', '')
        else:
            ampm = 'am'
            alarm_time = alarm_time.replace('am', '')
    alarm_time = alarm_time.split(':')
    alarm_hours = int(alarm_time[0])
    alarm_minutes = int(alarm_time[1])

    set_alarm(alarm_hours, alarm_minutes, every_day, ampm)


def ring_alarm():
    alarm_list = []
    sqlite_cursor = sqlite_connection.cursor()
    cloud_mysql_cursor = cloud_mysql_connection.cursor()
    local_mysql_cursor = local_mysql_connection.cursor()
    sqlite_cursor.execute("""SELECT * FROM alarms ORDER BY time ASC""")
    for data in sqlite_cursor:
        if data[1] == 'on':
            alarm_list.append(f'{data[0]} {data[3]} {data[2]}')
            # ampm_list.append(data[3])
    for times in alarm_list:
        print(times)
        times = times.split(' ')
        real_time = times[0]
        real_time = real_time.split(':')
        real_hour = int(real_time[0])
        real_minute = int(real_time[1])
        alarm_h = real_hour
        alarm_m = real_minute
        am_pm = times[1]
        every_day = times[2]
        print("Waiting for the alarm", alarm_h, alarm_m, am_pm)
        if alarm_h != 12:
            if am_pm == "pm":
                alarm_h = alarm_h + 12
        now = datetime.now()
        d = datetime.now().date()
        later = datetime(d.year, d.month, d.day, alarm_h, alarm_m, 0)
        difference = (later - now)
        total_sec = difference.total_seconds()
        if total_sec < 0:
            total_sec = 86400 + total_sec

        def alarm_func():
            from SKGEzhil_Voice_Assistant.script import current_time
            print('ringing')
            print(f'{current_time.hours()}:{current_time.minutes()}')
            from pydub import AudioSegment
            from pydub.playback import play
            song = AudioSegment.from_mp3("../alarm.mp3")
            play(song)
            if every_day == 'no':
                try:
                    cloud_mysql_cursor.execute(
                        f"UPDATE alarms SET activestatus = 'off' WHERE time = '{current_time.hours()}:{current_time.minutes()}'")
                    cloud_mysql_connection.commit()
                    sqlite_cursor.execute(
                        f"UPDATE alarms SET activestatus = 'off' WHERE time = '{current_time.hours()}:{current_time.minutes()}'")
                    sqlite_connection.commit()
                    local_mysql_cursor.execute(
                        f"UPDATE alarms SET activestatus = 'off' WHERE time = '{current_time.hours()}:{current_time.minutes()}'")
                    local_mysql_cursor.commit()
                except Exception as e:
                    print(e)

        timer = threading.Timer(total_sec, alarm_func)
        timer.start()


def set_alarm(hours, minutes, every_day, ampm):
    alarm_time = f'{hours}:{minutes}'
    sqlite_cursor = sqlite_connection.cursor()
    cloud_mysql_cursor = cloud_mysql_connection.cursor()
    local_mysql_cursor = local_mysql_connection.cursor()
    cloud_mysql_cursor.execute("USE assistant_database")
    local_mysql_cursor.execute("USE assistant_database")
    sql = """INSERT INTO alarms VALUES (%s, %s, %s, %s)"""
    sqlite = """INSERT INTO alarms VALUES (?, ?, ?, ?)"""
    if every_day:
        val = (alarm_time, 'on', 'yes', ampm)
    else:
        val = (alarm_time, 'on', 'no', ampm)
    cloud_mysql_cursor.execute(sql, val)
    cloud_mysql_connection.commit()
    local_mysql_cursor.execute(sql, val)
    local_mysql_connection.commit()
    sqlite_cursor.execute(sqlite, val)
    sqlite_connection.commit()
    ring_alarm()
