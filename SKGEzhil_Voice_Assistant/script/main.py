import pyjokes
import requests
import wikipedia
import wolframalpha

try:

    from SKGEzhil_Voice_Assistant.script import config, google_calendar
    from SKGEzhil_Voice_Assistant.script.speech_engine import talk, take_command
except Exception as e:
    print(e)

def last_word(string):
    newstring = ""
    length = len(string)
    for i in range(length - 1, 0, -1):
        if string[i] == " ":
            return newstring[::-1]
        else:
            newstring = newstring + string[i]


def check_connection():
    url = "http://www.kite.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print("Connected to the Internet")
        return 'connected'
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("Not connected")
        return 'not connected'


def google_search(received_command):
    custom_search_api = config.custom_search_api
    custom_search_id = config.custom_search_id
    query = received_command.replace('google ', '')
    page = 1
    start = 1
    url = f"https://www.googleapis.com/customsearch/v1?key={custom_search_api}&cx={custom_search_id}&q={query}&start={start}"
    data = requests.get(url).json()
    print(data)
    search_items = data.get("items")
    for i, search_item in enumerate(search_items, start=1):
        title = search_item.get("title")
        snippet = search_item.get("snippet")
        html_snippet = search_item.get("htmlSnippet")
        link = search_item.get("link")
        print("=" * 10, f"Result #{i + start - 1}", "=" * 10)
        print("Title:", title)
        print("Description:", snippet)
        print("URL:", link, "\n")
        talk(snippet)
        break


def logs(question):
    from SKGEzhil_Voice_Assistant.script.database import cloud_mysql_connection, local_mysql_connection
    from SKGEzhil_Voice_Assistant.script.database import sqlite_connection
    from datetime import datetime
    now = datetime.now()
    d = datetime.now().date()
    time_string = now.strftime("%H:%M")
    date = f'{d.day}/{d.month}/{d.year}'
    db_cursor = cloud_mysql_connection.cursor()
    local_mysql_cursor = local_mysql_connection.cursor()
    sqlite_cursor = sqlite_connection.cursor()
    sql = """INSERT INTO logs (questions, date, time) VALUES (%s, %s, %s)"""
    sqlite = """INSERT INTO logs (questions, date, time) VALUES (?, ?, ?)"""
    val = (question, date, time_string)
    db_cursor.execute(sql, val)
    cloud_mysql_connection.commit()
    sqlite_cursor.execute(sqlite, val)
    sqlite_connection.commit()
    local_mysql_cursor.execute(sql, val)
    local_mysql_connection.commit()

def run_assistant():
    # received_command = take_command()
    received_command = input("enter u'r commands here: ")
    print(received_command)
    if 'command not received' in received_command:
        no_command_received = True
    else:
        no_command_received = False
    while no_command_received:
        print('no command received')
        received_command = take_command()

    if 'play' in received_command:
        import pywhatkit
        song = received_command.replace('play', '')
        talk('playing ' + song + 'song')
        pywhatkit.playonyt(song)

    elif 'who created you' in received_command:
        talk('I was created by yeskejji yelil')

    elif 'your name' in received_command:
        talk('My name is yeskejji yelil')

    elif 'time' in received_command:
        import datetime
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time is now' + time)
        print(time)
    elif 'who is' in received_command:
        try:
            person = received_command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        except Exception as e:
            print(e)
            print("Not found in wikipedia")
            try:
                app_id = "HK8VGY-K22567Q59V"
                question = received_command.replace('ask', '')
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                print(answer)
                talk(answer)
            except Exception as e:
                print(e)
                print('I cant understand what u are speaking')
                google_search(received_command)

    elif 'joke' in received_command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)

    elif 'weather' in received_command:
        print('ok')
        city_name = last_word(received_command)
        from SKGEzhil_Voice_Assistant.script import weather
        weather.weather_report(city_name)
        print('weatherrr')

    elif 'event' in received_command:
        if 'what' in received_command:
            google_calendar.list_events()
        else:
            from SKGEzhil_Voice_Assistant.script import calendar_commands
            calendar_commands.calendar_commands()

    elif 'news' in received_command:
        from SKGEzhil_Voice_Assistant.script import news
        news.news_report()

    elif 'mail' in received_command:
        from SKGEzhil_Voice_Assistant.script import mail
        mail.read_mail()

    elif 'inbox' in received_command:
        from SKGEzhil_Voice_Assistant.script import mail
        mail.read_mail()

    elif 'google' in received_command:
        google_search(received_command)


    elif 'mean' in received_command:
        from PyDictionary import PyDictionary
        dictionary = PyDictionary()
        meaning = dictionary.meaning(last_word(received_command))
        print(meaning)
        y = meaning["Noun"]
        for i in y:
            print(i)
            talk(i)
            break

    elif 'score' in received_command:
        from SKGEzhil_Voice_Assistant.script import cricket
        cricket.cricket_score()

    elif 'remember that' in received_command:
        from SKGEzhil_Voice_Assistant.script import remember
        received_command = received_command.replace('remember that', '')
        remember.remember(received_command)

    elif 'kept' in received_command:
        if 'remember' not in received_command:
            from SKGEzhil_Voice_Assistant.script import remember
            key_word = last_word(received_command)
            remember.retrieve(key_word)
        else:
            from SKGEzhil_Voice_Assistant.script import remember
            received_command = received_command.replace('remember that', '')
            remember.remember(received_command)

    elif 'alarm' in received_command:
        from SKGEzhil_Voice_Assistant.script import alarm
        alarm.create_alarm(received_command)

    elif 'wake' in received_command:
        from SKGEzhil_Voice_Assistant.script import alarm
        alarm.create_alarm(received_command)

    elif 'remind' in received_command:
        from SKGEzhil_Voice_Assistant.script import reminder
        reminder.create_reminder(received_command)


    else:
        try:
            question = received_command.replace('ask', '')
            client = wolframalpha.Client(config.wolframalpha_api)
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            talk(answer)
        except Exception as e:
            print(e)
            print('I cant understand what u are speaking')
            google_search(received_command)

    logs(received_command)


startup_processes = 0
while True:
    # internet = check_connection()
    # if 'not' in internet:
    #     talk('Please connect to internet')
    # else:
    if startup_processes == 0:
        from SKGEzhil_Voice_Assistant.script.alarm import ring_alarm

        ring_alarm()
        from SKGEzhil_Voice_Assistant.script.reminder import reminder_alarm

        reminder_alarm()
        startup_processes = 1
    # from SKGEzhil_Voice_Assistant.script import wake_word, calendar_commands, config, news, google_calendar, weather
    # wake_engine = wake_word.wake_word()
    run_assistant()
