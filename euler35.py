#!/usr/bin/env python
import pdb 
"""
197 circular because 197, 971, 719

13 primes below 100 are circular... 2,3,5,7,11,13,17,31,37,71,73,79,97.

how many circ primes are below one million?
"""
import math

def isPrime(x):
    for i in xrange(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    else:
        return True

notin = set(["2","4","5","6","8"])
def isCirc(x):
    #global notin
    #xstr = list(str(x))
    #sxstr = set(xstr)
    #if len(sxstr.intersection(notin)) > 1:
        #return False
    for i in xstr:
        xstr.append(xstr.pop(0))
        if not isPrime(int("".join(xstr))):
            return False
    return True

aset = set()
notin = set(["2","4","5","6","8"])
for x in xrange(7,1000001,2):
    #pdb.set_trace()
    xstr = list(str(x))
    sxstr = set(xstr)
    if len(sxstr.intersection(notin)) > 0:
        continue
    elif isCirc(x):
        aset.add(x)
        

#ab = filter(isCirc, xrange(3,1000001,2))
aset.add(2)
aset.add(5)
ab = list(aset)
#ab.insert(1, 2)
ab.sort()
print ab
print len(ab)
    



