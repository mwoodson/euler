#!/usr/bin/env python
#import pdb

"""
145 = 1!+4!+5!

sum of all nums that are equal to the sum of their ! digits
"""

#def fact(x,cache):
#    if x < 2:
#        return 1
#    elif x < 3:
#        return 2
#    if cache[x] != 1000:
#        return cache[x]
#    cache[x] = x * fact(x-1,cache)
#    return cache[x]
isum = 0
cache = [1, 1, 2]
for i in xrange(3,50000):
    cache.append(cache[i-1] * i)
    if i == sum([cache[int(z)] for z in str(i)]):
        isum += i
print "answer=%s"%isum
