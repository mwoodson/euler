#!/usr/bin/env python
'''
n! means n x (n - 1) x ... x 3 x 2 x 1

Find the sum of the digits in the number 100!
'''


def fact(x): 
    return (1 if x==0 else x * fact(x-1))

astring = str(fact(100))
print sum([int(x) for x in astring])
