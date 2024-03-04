import datetime
import math


birthday = input()
birthday = datetime.date(int(birthday[6:]), int(birthday[3:5]), int(birthday[:2]))
today = input()
today = datetime.date(int(today[6:]), int(today[3:5]), int(today[:2]))
T = (today - birthday).days
print(round((math.sin((2 * math.pi * T) / 23) * 100), 2))
print(round((math.sin((2 * math.pi * T) / 28) * 100), 2))
print(round((math.sin((2 * math.pi * T) / 33) * 100), 2))


