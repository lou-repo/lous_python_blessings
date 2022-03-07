#!/usr/bin/python3
import os
import getpass
import smtplib
import ssl 

#shows uptime in human readable format
def uptime():
        try:
            f = open( "/proc/uptime" )
            contents = f.read().split()
            f.close()
        except:
            return "Cannot open uptime file: /proc/uptime"
            total_seconds = float(contents[0])
# Helper vars:
        MINUTE  = 60
        HOUR    = MINUTE * 60
        DAY     = HOUR * 24
# Get the days, hours, etc:
        days    = int( total_seconds / DAY )
        hours   = int( ( total_seconds % DAY ) / HOUR )
        minutes = int( ( total_seconds % HOUR ) / MINUTE )
        seconds = int( total_seconds % MINUTE )

# Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
string = ""
        if days > 0:
            string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
        if len(string) > 0 or hours > 0:
            string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
        if len(string) > 0 or minutes > 0:
            string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
            string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
            return string;

        print("The system uptime is: " + uptime())

#shows users logged in

checkuser = getpass.getuser()

print("The user currently logged in is: " + checkuser)

#This emails administrator with details above
sender = 'system'
receivers = ['administrator'] 

text = f"""\
Subject: System Notification
To: {receivers}
From: {sender}

Hello Admin,

The system uptime is: {uptime()}
The user(s) currently logged in: {checkuser}
"""

try:
    smtp = smtplib.SMTP('localhost')
    smtp.sendmail(sender, receivers, text)         
    print ("Successfully sent email")
except SMTPException:
    print ("Error: unable to send email")
