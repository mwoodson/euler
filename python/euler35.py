#!/usr/bin/env python
#import pdb 
"""
197 circular because 197, 971, 719

13 primes below 100 are circular... 2,3,5,7,11,13,17,31,37,71,73,79,97.

how many circ primes are below one million?
"""
#import math


def primeSieve(n):
    candidates = range(n+1)
    fin = int(n**.5)
    for i in xrange(2,fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)

    #can filter out all 200k's, 400's, 600's, 800's
    return [i for i in candidates[2:] if i], candidates
    #return [i for i in candidates[2:] if i]

#def isPrime(x):
#    for i in xrange(2,int(math.sqrt(x))+1):
#        if x % i == 0:
#            return False
#    else:
#        return True
#
#notin = set(["2","4","5","6","8"])
#def isCirc(x):
#    #global notin
#    xstr = list(str(x))
#    #sxstr = set(xstr)
#    #if len(sxstr.intersection(notin)) > 1:
#        #return False
#    for i in xstr:
#        xstr.append(xstr.pop(0))
#        num = int("".join(xstr))
#        if not isPrime(num):
#            return False
#    #map(aset.add, t)
#    return True
#
aset = set()
aset.add(2) #Add in 2 
aset.add(5) # and 5 because we skip those
primes = primeSieve(1000000)
#notin = set(["2","4","5","6","8"])
notin = set(["2","4","5","6","8"])
for x in primes[0]:
    xstr = list(str(x))
    sxstr = set(xstr)
    if not len(sxstr.intersection(notin)) > 0:
        for i in xstr:
            xstr.append(xstr.pop(0))
            num = int("".join(xstr))
            if not primes[1][num]:
                break
        else: 
            aset.add(x)

#ab = list(aset)
#ab.insert(1, 2)
#ab.sort()
#print ab
#print len(ab)
print len(aset)

#ab = filter(isCirc, xrange(3,1000001,2)) Takes longer
    



