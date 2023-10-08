# import package called daytime
import datetime

#my first python program
#check if today is tuesday or not.

print("check if its a Tuesday!")

today  = datetime.datetime.today()
dayOfweek = today.weekday()                          # extract weekday from today, 0-6 integer(mon-sun)

if dayOfweek == 1:
    print("It's Tuesday")
elif dayOfweek == 2:
    print("It's Wednesday")
else: 
    print("It's not Tuesday")
