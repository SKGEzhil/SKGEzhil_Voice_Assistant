from datetime import datetime

def hours():
    ampm = 'am'
    now = datetime.now()
    time_string = now.strftime("%H:%M")
    current_hour = time_string.split(':')
    if ampm == 'pm':
        exact_hour = int(current_hour[0]) - 12
    else:
        exact_hour = int(current_hour[0])
    exact_min = int(current_hour[1])
    return exact_hour

def minutes():
    now = datetime.now()
    time_string = now.strftime("%H:%M")
    current_hour = time_string.split(':')
    exact_hour = int(current_hour[0]) - 12
    exact_min = int(current_hour[1])
    return exact_min

print(f'{hours()}:{minutes()}')
