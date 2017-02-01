from datetime import datetime, time
from pytz import timezone

now = datetime.now(timezone('US/Pacific'))
now_time = now.time()

nyc1 = datetime.now(timezone('US/Eastern'))
nyc1_time = nyc1.time()

london1 = datetime.now(timezone('Europe/London'))
london1_time= london1.time()

cities = ['Portland', 'New York City', 'London']
times = (now_time, nyc1_time, london1_time)

def open_time(cities):
        for index in range(0, len(cities)):
                value = cities[index]
                while value <= 2:
                        for y in times:
                                if y >= time(9,00) and y <= time(19,00):
                                       print ("The %s branch is open.")%cities
                                else:
                                        print ("The %s branch is closed.")%cities
                                                          
                

open_time(cities)



