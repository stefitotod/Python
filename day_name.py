# Потребителят въвежда дата, а в конзолата се принтира кой ден от седмицата е.

import datetime
year = int(input("Enter year:"))
month = int(input("Enter month:"))
day = int(input("Enter day:"))
dt = datetime.date(year, month, day)
print("Datetime is:", dt)
print("Day Name:", dt.strftime("%A"))
