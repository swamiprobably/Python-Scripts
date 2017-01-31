from datetime import datetime, time
from pytz import timezone

fmt = "%H:%M:%S %Z"

# Current time in Portland
portland = datetime.now(timezone('US/Pacific'))
print ("It is " + portland.strftime(fmt) + " in Portland.")

# US/Eastern time zone
nyc = datetime.now(timezone('US/Eastern'))
print ("It is " + nyc.strftime(fmt) + " in NYC time.")

# London time zone
now_london = datetime.now(timezone('Europe/London'))
print ("It is " + now_london.strftime(fmt) + " in London time.")

now = datetime.now(timezone('US/Pacific'))
now_time = now.time()

nyc1 = datetime.now(timezone('US/Eastern'))
nyc1_time = nyc1.time()

london1 = datetime.now(timezone('Europe/London'))
london1_time= london1.time()

if nyc1_time >= time(9,00) and nyc1_time <= time(21,00):
    print ("The New York branch is open.")
else:
    print ("The New York branch is closed.")

if london1_time >= time(9,00) and london1_time <= time(21,00):
    print ("The London branch is open.")
else:
    print ("The London branch is closed.")


