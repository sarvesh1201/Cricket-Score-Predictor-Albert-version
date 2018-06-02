print("Welcome to daily astrology!")
from datetime import datetime
time=datetime.now()
datex=int(time.day)
date=(3**datex)%7
name=input("what is your name?")
name_person=name.lower()
year=input("enter your year of birth")
yob=int(year)
month=input("enter your month of birth")
length=len(name_person)
datef=int(date)
afactor=length+yob+datef
afactorx=afactor%5
if afactorx==0:
    print ("today you might forget something very important.Stay alert!")
elif afactorx==1:
    print("today is your lucky day!whatever you touch will turn gold!")
elif afactorx==2:
    print("today is a good day for you financially!make use of this advantage!")
elif afactorx==3:
    print("today everyone will show love and affection towards you!make sure you reciprocate")
else:
    print("you will feel lazy today..so buckle up!")
