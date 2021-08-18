#!/usr/bin/python3

message = input("enter a message: ")

print("First Character:", message[0])
print("Last Character:", message[-1])
print("Middle Chatacter:", message[int(len(message) / 2)])
print("Even index characters:", message[0])
print("odd index characters:", message[1::2])
print("Reversed message", message[::-1])