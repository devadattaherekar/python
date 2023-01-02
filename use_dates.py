import datetime

#print(dir(datetime))

current_dt=datetime.datetime.now() # to get current date and time
print(current_dt)

current_dt=datetime.datetime.today()# to get current date and time
print(current_dt)

next_date=datetime.date(2024,1,17) # format should be YEAR,month,day
print(next_date)
print(f"{next_date.day}-{next_date.month}-{next_date.year}")

dt1=datetime.date(2022,12,30)
dt2=datetime.timedelta(45) # Note: Add 45 days using timedelta
print("Renewal reminder on ",dt1+dt2) # add 45 days
print("Renewal reminder on ",dt1-dt2) # deduct 45 days

dt3=datetime.timedelta(100)
print(dt2+dt3)

custom_time=datetime.time(10,15,30) # use time to work on time
print(f"{custom_time.hour}:{custom_time.minute}:{custom_time.second}")

dt1=datetime.date(2022,12,30) # to create custom dates
formatted_date=dt1.strftime('%A %B %d/%m/%Y') # To customize date use strftime
print(formatted_date)

try:
    date_format=input("Enter date in dd-mm-yy ")
    date_is=datetime.datetime.strptime(date_format,'%d/%m/%Y')
except ValueError as errmsg:
    print(errmsg)
else:
    print("You have entered ",date_is.strftime("%d/%m/%Y"))
