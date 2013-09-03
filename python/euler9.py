#!/usr/bin/env python
import math

'''
    A pythagorean triplet is a set of three natural numbers, a < b < c, for which,
     a^(2) + b^(2) = c^(2)
        
        For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
        
            There exists exactly one Pythagorean triplet for which a + b + c = 1000.
                Find the product abc.
'''


#a^2 + b^2 = c^2
found = False

for a in xrange(1, 1000):
    for b in xrange(1, 1000):
        num = math.pow(a,2) + math.pow(b,2)
        c = math.sqrt(num)
        if c > a and c > b and (a + b + c == 1000):
            print a
            print b
            print c
            num = a * b * c
            print num
            found = True 
            break
    if found:
        break
