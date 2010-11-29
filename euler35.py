#!/usr/bin/env python
import pdb

"""
197 circular because 197, 971, 719

13 primes below 100 are circular... 2,3,5,7,11,13,17,31,37,71,73,79,97.

how many circ primes are below one million?
"""
import math
import copy

def isPrime(x):
    #if x == 1 or x == 2:
        #return True
    for i in xrange(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    else:
        return True

def isCirc(x):
    xstr = list(str(x))
    for i in range(len(xstr)):
        xstr.append(xstr.pop(0))
        if not isPrime(int("".join(xstr))):
            return False
    return True
print len(filter(isCirc, filter(isPrime, xrange(3,1000000,2)))) + 2
    



