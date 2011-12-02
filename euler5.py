#!/usr/bin/env python

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
'''
nums = [19,13,18,17,16,15,14,13,12,11]

found = False
for i in xrange(2520, 1000000000, 2520):
    if any(z for z in nums if i % z != 0):
        continue
    else:
        print i
        break
