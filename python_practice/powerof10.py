#!/usr/bin/python3

import math
#assign values to variables
x = 4
n = 3

#method 1 
power = x ** n
print("%d to the power of %d is %d" % (x,n,power))

#method 2
power = pow(x,n)
print ("%d to the power of %d is %d" % (x,n,power))

#method 3
power = math.pow(2,6.5)
print("%d to the power %d is %5.2f" % (x,n,power))

