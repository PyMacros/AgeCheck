import datetime


now = datetime.datetime.now()

agelimit = 13
year = int(now.year)
user_year = int(raw_input("Enter your birth year: "))
allowed = False

if year - user_year >= agelimit:
  allowed = True
  print "You are old enough!"
else:
  allowed = False
  print "You are too young!"
