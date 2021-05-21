#!/usr/bin/python3
from datetime import datetime 
import pytz

#read current date

nytimezone= pytz.timezone("America/New_york")
ny_time = datetime.now(nytimezone)
print( "The time in Virginia Beach is:", ny_time.strftime("%H:%M"))

londontimezone = pytz.timezone("Europe/London")
london_time = datetime.now(londontimezone)
print( "The time in Scotland is:", london_time.strftime("%H:%M"))
