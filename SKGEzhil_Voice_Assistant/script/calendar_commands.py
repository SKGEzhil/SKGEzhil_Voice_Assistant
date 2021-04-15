from SKGEzhil_Voice_Assistant.script import speech_engine


def month_year_change(date_given):
    from datetime import datetime
    d = datetime.now().date()
    month = d.month
    year = d.year
    if d.month == 1:
        if date_given > 31:
            date_given = date_given - 31
            month = d.month + 1
    if d.month == 2:
        if date_given > 28:
            date_given = date_given - 31
            month = d.month + 1
    if d.month == 3:
        if date_given > 31:
            date_given = date_given - 31
            month = d.month + 1
    if d.month == 4:
        if date_given > 30:
            date_given = date_given - 31
            month = d.month + 1
    if d.month == 5:
        if date_given > 31:
            date_given = date_given - 31
            month = d.month + 1
    if d.month == 6:
        if date_given > 30:
            date_given = date_given - 31
            month = d.month + 1
    if d.month == 7:
        if date_given > 31:
            date_given = date_given - 31
            month = d.month + 1
    if d.month == 8:
        if date_given > 31:
            date_given = date_given - 31
            month = d.month + 1
    if d.month == 9:
        if date_given > 30:
            date_given = date_given - 31
            month = d.month + 1
    if d.month == 10:
        if date_given > 31:
            date_given = date_given - 31
            month = d.month + 1
    if d.month == 11:
        if date_given > 30:
            date_given = date_given - 31
            month = d.month + 1
    if d.month == 12:
        if date_given > 31:
            date_given = date_given - 31
            month = 1
            year = d.year + 1
    return date_given, month, year


def calendar_commands():
    from SKGEzhil_Voice_Assistant.script import google_calendar
    from datetime import datetime
    speech_engine.talk('What is the event')
    event = input('What is the event : ')
    speech_engine.talk('when is the event')
    time = input('when is the event : ')

    if 'tomorrow' in time:
        time_in_bool = True
        is_pm = False
        d = datetime.now().date()
        timetext = time.replace('tomorrow', '')
        if 'at' in timetext:
            timetext = timetext.replace('at', '')
        if 'am' in timetext:
            timetext = timetext.replace('am', '')
        elif 'pm' in timetext:
            timetext = timetext.replace('pm', '')
            is_pm = True
        else:
            time_in_bool = False
            speech_engine.talk('At what time : ')
            time_in = input('At what time : ')
            is_pm = False
            if 'at' in time_in:
                time_in = time_in.replace('at', '')
            if 'am' in time_in:
                time_in = time_in.replace('am', '')
            if 'pm' in time_in:
                time_in = time_in.replace('pm', '')
                is_pm = True
            print(time_in)
            if ' ' in time_in:
                time_in = time_in.replace(' ', '')
            print(time_in)
            exact_time = time_in.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)
            google_calendar.create_event(event, ' ', datetime(d.year, d.month, d.day + 1, hours, minutes))
        if time_in_bool:
            print(timetext)
            if ' ' in timetext:
                timetext = timetext.replace(' ', '')
            print(timetext)
            exact_time = timetext.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)

            google_calendar.create_event(event, ' ', datetime(d.year, d.month, d.day + 1, hours, minutes))
    elif 'monday' in time:
        monday_face = 1
        d = datetime.now().date()
        day = datetime.now().weekday()
        day = day + 1
        if monday_face < day:
            date_given = (7 - day) + monday_face
        elif monday_face > day:
            date_given = monday_face - day
        date_given = d.day + date_given
        print(date_given)

        year = month_year_change(date_given)[2]
        month = month_year_change(date_given)[1]
        date_given = month_year_change(date_given)[0]

        time_in_bool = True
        is_pm = False
        d = datetime.now().date()
        timetext = time.replace('monday', '')
        if 'at' in timetext:
            timetext = timetext.replace('at', '')
        if 'am' in timetext:
            timetext = timetext.replace('am', '')
        elif 'pm' in timetext:
            timetext = timetext.replace('pm', '')
            is_pm = True
        else:
            time_in_bool = False
            speech_engine.talk('At what time : ')
            time_in = input('At what time : ')
            is_pm = False
            if 'at' in time_in:
                time_in = time_in.replace('at', '')
            if 'am' in time_in:
                time_in = time_in.replace('am', '')
            if 'pm' in time_in:
                time_in = time_in.replace('pm', '')
                is_pm = True
            print(time_in)
            if ' ' in time_in:
                time_in = time_in.replace(' ', '')
            print(time_in)
            exact_time = time_in.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)
            google_calendar.create_event(event, ' ', datetime(2021, 3, date_given, hours, minutes))
        if time_in_bool:
            print(timetext)
            if ' ' in timetext:
                timetext = timetext.replace(' ', '')
            print(timetext)
            exact_time = timetext.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)

            google_calendar.create_event(event, ' ', datetime(year, month, date_given, hours, minutes))
    elif 'tuesday' in time:
        tuesday_face = 2
        d = datetime.now().date()
        day = datetime.now().weekday()
        day = day + 1
        if tuesday_face < day:
            date_given = (7 - day) + tuesday_face
        elif tuesday_face > day:
            date_given = tuesday_face - day
        date_given = d.day + date_given
        print(date_given)

        year = month_year_change(date_given)[2]
        month = month_year_change(date_given)[1]
        date_given = month_year_change(date_given)[0]

        time_in_bool = True
        is_pm = False
        d = datetime.now().date()
        timetext = time.replace('tuesday', '')
        if 'at' in timetext:
            timetext = timetext.replace('at', '')
        if 'am' in timetext:
            timetext = timetext.replace('am', '')
        elif 'pm' in timetext:
            timetext = timetext.replace('pm', '')
            is_pm = True
        else:
            time_in_bool = False
            speech_engine.talk('At what time : ')
            time_in = input('At what time : ')
            is_pm = False
            if 'at' in time_in:
                time_in = time_in.replace('at', '')
            if 'am' in time_in:
                time_in = time_in.replace('am', '')
            if 'pm' in time_in:
                time_in = time_in.replace('pm', '')
                is_pm = True
            print(time_in)
            if ' ' in time_in:
                time_in = time_in.replace(' ', '')
            print(time_in)
            exact_time = time_in.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)
            google_calendar.create_event(event, ' ', datetime(2021, 3, date_given, hours, minutes))
        if time_in_bool:
            print(timetext)
            if ' ' in timetext:
                timetext = timetext.replace(' ', '')
            print(timetext)
            exact_time = timetext.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)

            google_calendar.create_event(event, ' ', datetime(2021, 3, date_given, hours, minutes))

    elif 'wednesday' in time:
        wednesday_face = 3
        d = datetime.now().date()
        day = datetime.now().weekday()
        day = day + 1
        if wednesday_face < day:
            date_given = (7 - day) + wednesday_face
        elif wednesday_face > day:
            date_given = wednesday_face - day
        date_given = d.day + date_given
        print(date_given)

        year = month_year_change(date_given)[2]
        month = month_year_change(date_given)[1]
        date_given = month_year_change(date_given)[0]

        time_in_bool = True
        is_pm = False
        d = datetime.now().date()
        timetext = time.replace('wednesday', '')
        if 'at' in timetext:
            timetext = timetext.replace('at', '')
        if 'am' in timetext:
            timetext = timetext.replace('am', '')
        elif 'pm' in timetext:
            timetext = timetext.replace('pm', '')
            is_pm = True
        else:
            time_in_bool = False
            speech_engine.talk('At what time : ')
            time_in = input('At what time : ')
            is_pm = False
            if 'at' in time_in:
                time_in = time_in.replace('at', '')
            if 'am' in time_in:
                time_in = time_in.replace('am', '')
            if 'pm' in time_in:
                time_in = time_in.replace('pm', '')
                is_pm = True
            print(time_in)
            if ' ' in time_in:
                time_in = time_in.replace(' ', '')
            print(time_in)
            exact_time = time_in.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)
            google_calendar.create_event(event, ' ', datetime(2021, 3, date_given, hours, minutes))
        if time_in_bool:
            print(timetext)
            if ' ' in timetext:
                timetext = timetext.replace(' ', '')
            print(timetext)
            exact_time = timetext.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)

            google_calendar.create_event(event, ' ', datetime(2021, 3, date_given, hours, minutes))

    elif 'thursday' in time:
        thursday_face = 4
        d = datetime.now().date()
        month = d.month
        year = d.year
        day = datetime.now().weekday()
        day = day + 1
        date_given = 0
        if thursday_face < day:
            date_given = (7 - day) + thursday_face
        elif thursday_face > day:
            date_given = thursday_face - day
        date_given = d.day + date_given
        print(date_given)

        year = month_year_change(date_given)[2]
        month = month_year_change(date_given)[1]
        date_given = month_year_change(date_given)[0]

        time_in_bool = True
        is_pm = False
        d = datetime.now().date()
        timetext = time.replace('thursday', '')
        if 'at' in timetext:
            timetext = timetext.replace('at', '')
        if 'am' in timetext:
            timetext = timetext.replace('am', '')
        elif 'pm' in timetext:
            timetext = timetext.replace('pm', '')
            is_pm = True
        else:
            time_in_bool = False
            speech_engine.talk('At what time : ')
            time_in = input('At what time : ')
            is_pm = False
            if 'at' in time_in:
                time_in = time_in.replace('at', '')
            if 'am' in time_in:
                time_in = time_in.replace('am', '')
            if 'pm' in time_in:
                time_in = time_in.replace('pm', '')
                is_pm = True
            print(time_in)
            if ' ' in time_in:
                time_in = time_in.replace(' ', '')
            print(time_in)
            exact_time = time_in.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)
            google_calendar.create_event(event, ' ', datetime(year, month, date_given, hours, minutes))
        if time_in_bool:
            print(timetext)
            if ' ' in timetext:
                timetext = timetext.replace(' ', '')
            print(timetext)
            exact_time = timetext.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)

            google_calendar.create_event(event, ' ', datetime(year, month, date_given, hours, minutes))

    elif 'friday' in time:
        friday_face = 5
        d = datetime.now().date()
        month = d.month
        year = d.year
        day = datetime.now().weekday()
        day = day + 1
        if friday_face < day:
            date_given = (7 - day) + friday_face
        elif friday_face > day:
            date_given = friday_face - day
        date_given = d.day + date_given
        print(date_given)

        year = month_year_change(date_given)[2]
        month = month_year_change(date_given)[1]
        date_given = month_year_change(date_given)[0]

        time_in_bool = True
        is_pm = False
        d = datetime.now().date()
        timetext = time.replace('friday', '')
        if 'at' in timetext:
            timetext = timetext.replace('at', '')
        if 'am' in timetext:
            timetext = timetext.replace('am', '')
        elif 'pm' in timetext:
            timetext = timetext.replace('pm', '')
            is_pm = True
        else:
            time_in_bool = False
            speech_engine.talk('At what time : ')
            time_in = input('At what time : ')
            is_pm = False
            if 'at' in time_in:
                time_in = time_in.replace('at', '')
            if 'am' in time_in:
                time_in = time_in.replace('am', '')
            if 'pm' in time_in:
                time_in = time_in.replace('pm', '')
                is_pm = True
            print(time_in)
            if ' ' in time_in:
                time_in = time_in.replace(' ', '')
            print(time_in)
            exact_time = time_in.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)
            google_calendar.create_event(event, ' ', datetime(year, month, date_given, hours, minutes))
        if time_in_bool:
            print(timetext)
            if ' ' in timetext:
                timetext = timetext.replace(' ', '')
            print(timetext)
            exact_time = timetext.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)

            google_calendar.create_event(event, ' ', datetime(year, month, date_given, hours, minutes))

    elif 'saturday' in time:
        saturday_face = 6
        d = datetime.now().date()
        month = d.month
        year = d.year
        day = datetime.now().weekday()
        day = day + 1
        if saturday_face < day:
            date_given = (7 - day) + saturday_face
        elif saturday_face > day:
            date_given = saturday_face - day
        date_given = d.day + date_given
        print(date_given)

        year = month_year_change(date_given)[2]
        month = month_year_change(date_given)[1]
        date_given = month_year_change(date_given)[0]

        time_in_bool = True
        is_pm = False
        d = datetime.now().date()
        timetext = time.replace('saturday', '')
        if 'at' in timetext:
            timetext = timetext.replace('at', '')
        if 'am' in timetext:
            timetext = timetext.replace('am', '')
        elif 'pm' in timetext:
            timetext = timetext.replace('pm', '')
            is_pm = True
        else:
            time_in_bool = False
            speech_engine.talk('At what time : ')
            time_in = input('At what time : ')
            is_pm = False
            if 'at' in time_in:
                time_in = time_in.replace('at', '')
            if 'am' in time_in:
                time_in = time_in.replace('am', '')
            if 'pm' in time_in:
                time_in = time_in.replace('pm', '')
                is_pm = True
            print(time_in)
            if ' ' in time_in:
                time_in = time_in.replace(' ', '')
            print(time_in)
            exact_time = time_in.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)
            google_calendar.create_event(event, ' ', datetime(year, month, date_given, hours, minutes))
        if time_in_bool:
            print(timetext)
            if ' ' in timetext:
                timetext = timetext.replace(' ', '')
            print(timetext)
            exact_time = timetext.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)

            google_calendar.create_event(event, ' ', datetime(year, month, date_given, hours, minutes))

    elif 'sunday' in time:
        sunday_face = 7
        d = datetime.now().date()
        month = d.month
        year = d.year
        day = datetime.now().weekday()
        day = day + 1
        if sunday_face < day:
            date_given = (7 - day) + sunday_face
        elif sunday_face > day:
            date_given = sunday_face - day
        date_given = d.day + date_given
        print(date_given)

        year = month_year_change(date_given)[2]
        month = month_year_change(date_given)[1]
        date_given = month_year_change(date_given)[0]

        time_in_bool = True
        is_pm = False
        d = datetime.now().date()
        timetext = time.replace('sunday', '')
        if 'at' in timetext:
            timetext = timetext.replace('at', '')
        if 'am' in timetext:
            timetext = timetext.replace('am', '')
        elif 'pm' in timetext:
            timetext = timetext.replace('pm', '')
            is_pm = True
        else:
            time_in_bool = False
            speech_engine.talk('At what time : ')
            time_in = input('At what time : ')
            is_pm = False
            if 'at' in time_in:
                time_in = time_in.replace('at', '')
            if 'am' in time_in:
                time_in = time_in.replace('am', '')
            if 'pm' in time_in:
                time_in = time_in.replace('pm', '')
                is_pm = True
            print(time_in)
            if ' ' in time_in:
                time_in = time_in.replace(' ', '')
            print(time_in)
            exact_time = time_in.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)
            google_calendar.create_event(event, ' ', datetime(year, month, date_given, hours, minutes))
        if time_in_bool:
            print(timetext)
            if ' ' in timetext:
                timetext = timetext.replace(' ', '')
            print(timetext)
            exact_time = timetext.split(':')
            print(exact_time)
            print(exact_time[0])
            print(exact_time[1])
            minutes = int(exact_time[1])
            hours = int(exact_time[0])
            if is_pm:
                print('pm')
                hours = 12 + hours
                print(hours)

            google_calendar.create_event(event, ' ', datetime(year, month, date_given, hours, minutes))
