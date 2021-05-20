#!/usr/bin/python3

# import syst module
import sys

#total number of arguments 
print('Total arguments:', len(sys.argv))

print("Argument values are:")
# Interate command-line arguments using for loop
for i in sys.argv:
    print(i)