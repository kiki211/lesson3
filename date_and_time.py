from datetime import datetime, timedelta
import locale


locale.setlocale(locale.LC_TIME,'ru_RU')

# dt = datetime.now()
# print(dt)
# print(help(datetime.weekday))
# print(datetime.today())
# print("Today is " +str(datetime.weekday(datetime.now())))
# print(datetime.date(datetime.now()))
# print(datetime.day)
# print(datetime.astimezone(datetime.now()))
#
# delta = timedelta(1,600,9,12)
# print(delta)

# Task one
current_time = datetime.now()
def yesterday(today):
    delta = today - timedelta(1)
    return 'Yesterday was ' +str(delta.strftime('%A %B %d %Y'))

def tomorrow(today):
    delta = today + timedelta(1)
    return 'Tomorrow will be ' +str(delta.strftime('%A %D'))

print(yesterday(current_time))
print('Todays is ' + str(current_time.strftime('%A %d %B %Y')))
print(tomorrow(current_time))

# Task two
strochka = "01/01/17 12:10:03.234567"

def datetime_convert(str):
    date_time= datetime.strptime(str,'%d/%m/%y %H:%M:%S.%f')
    return date_time

print(datetime_convert(strochka))

