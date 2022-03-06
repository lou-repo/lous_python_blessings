#!/usr/bin/python3

import math
#assign values to variables
X = 4
N = 3

#method 1 
POWER = X ** N
print("%d to the power of %d is %d" % (X,N,POWER))

#method 2
POWER = pow(X,N)
print ("%d to the power of %d is %d" % (X,N,POWER))

#method 3
POWER = math.pow(2,6.5)
print("%d to the power %d is %5.2f" % (X,N,POWER))