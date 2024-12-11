# A simple calender disply app.
from calendar import TextCalendar
year = int(input('Enter a year: '))
cal = TextCalendar()
print(cal.formatyear(year, 2, 1, 8, 3))