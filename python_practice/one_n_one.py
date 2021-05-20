#!/usr/bin/python3

#import another python script
import vacations as v

#initialize the month list
months = ["january", "february", "march", "april", "may",
"june", "july", "august", "september", "october", "november", "december"]

# Initialize flag variable to print summer vacation one time
flag = 0

#iterate the list using for loop
for month in months:
    if month == "june" or month == "july":
        if flag == 0:
            print("Now",v.vacation1)
            flag = 1
    elif month == "december":
        print("Now",v.vacation2)
    else:
        print("The current month is", month)