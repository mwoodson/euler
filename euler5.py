#!/usr/bin/env python

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
'''

found = False
for i in xrange(2520, 1000000000, 20):
    for x in xrange(2, 21):
        if i % x != 0:
            break
    else:
        print i
        break
