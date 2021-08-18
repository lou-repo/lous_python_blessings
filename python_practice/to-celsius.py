#!/usr/bin/python3

#Python implimentation goes here

fahrenheit = float(input("What temperature (in Fahrenheit) would you like to convert to Celsius? "))
celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "F is", round(celsius, 2), "C")