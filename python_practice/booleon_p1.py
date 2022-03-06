#!/usr/bin/python3

#boolean value
from lib2to3.pgen2.token import NUMBER


VAL1 = True
print(VAL1)

#num to boolean
NUMBER = 10
print(bool(NUMBER))

NUMBER = -5
print(bool(NUMBER))

NUMBER = 0
print(bool(NUMBER))

#boolean from comparison operator
VAL1 = 6
VAL2 = 3
print(VAL1 < VAL2)