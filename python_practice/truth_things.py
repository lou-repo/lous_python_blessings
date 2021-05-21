#!/usr/bin/python3

#this script will return true things fitting specific requirements for true

thing = input ("what do you think is true? ")

def bool2str(v):
    return v.lower() in ('yes', 'y', 'true', 't', '1') #bool2string responds to these variations as true

if bool2str(thing) == True:
    print('this is true')

else:
    print('this is false')