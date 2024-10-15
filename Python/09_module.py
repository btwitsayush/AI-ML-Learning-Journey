import math
import calendar

# print(dir(math)) #to get to know all the funtions that are avilable in this module

# i.e to callculate power of a number


power=math.pow(2,3)
# print(power)

# to find factorial of a number

factorial=math.factorial(5)
# print(factorial)


# wroking with calendar module

# print(dir(calendar))

# to get the calendar of specific month 

# Create an HTMLCalendar object
html_cal = calendar.HTMLCalendar()

# Generate HTML for November 2019
nov_calendar = html_cal.formatmonth(2024, 11)

# print(nov_calendar)

monthCalendar=calendar.monthcalendar(2024,11)
print(monthCalendar)