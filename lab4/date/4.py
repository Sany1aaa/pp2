import datetime

x1 = datetime.datetime.now()
x2 = datetime.datetime.now()-datetime.timedelta(days = 19)
x = x1 - x2
print(x)