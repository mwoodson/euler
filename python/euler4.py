#!/usr/bin/env python

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

highest = 0
for i in xrange(999, 900, -2):
    for y in xrange(999, 900, -2):
        ptest = str(i * y)
        if ptest[:] == ptest[::-1]:
            if int(ptest) > highest:
                highest = int(ptest)
            break
print highest
