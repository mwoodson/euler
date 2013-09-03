#!/usr/bin/env python
import math

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6^(th) prime is 13.

What is the 10001^(st) prime number?

'''

def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

count = 0
for i in xrange(1, 10000000, 2):
    if isprime(i):
        count += 1
    if count == 10001:
        print i
        break
