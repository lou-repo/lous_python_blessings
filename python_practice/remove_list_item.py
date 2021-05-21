#!/usr/bin/python3

#Declare a fruit list
fruits = ["Mango", "Orange", "Banana", "Pineapple", "Watermellon"]

#insert an item into 2nd position
fruits.insert(1, "Grape")

#display list after inserting 

print(f"The fruit list after insert: {fruits}")

#remove an item 
fruits.remove("Pineapple")

#print the list after delete

print(f"The list of fruits after removing 1 is: {fruits}")