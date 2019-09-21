# Get the datetime library
from datetime import datetime, timedelta

# Get today's date
today = datetime.now()
print('Today is ' + str(today))
print('Day:    ' + str(today.day))
print('Month:  ' + str(today.month))
print('Year:   ' + str(today.year))
print('Hour:   ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))

# Get yesterday's date
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was ' + str(yesterday))

# Get the date from a string
birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Your birthday is ' + str(birthday_date))