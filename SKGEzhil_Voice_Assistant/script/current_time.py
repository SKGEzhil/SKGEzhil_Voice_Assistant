from datetime import datetime

def hours():
    now = datetime.now()
    time_string = now.strftime("%H:%M")
    current_hour = time_string.split(':')
    exact_hour = int(current_hour[0]) - 12
    exact_min = int(current_hour[1])
    return exact_hour

def minutes():
    now = datetime.now()
    time_string = now.strftime("%H:%M")
    current_hour = time_string.split(':')
    exact_hour = int(current_hour[0]) - 12
    exact_min = int(current_hour[1])
    return exact_min
