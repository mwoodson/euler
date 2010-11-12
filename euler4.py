#!/usr/bin/env python

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

highest = 0
for i in xrange(1000, 100, -1):
    for y in xrange(1000, 100, -1):
        ptest = str(i * y)
        if ptest[:] == ptest[::-1]:
            if ptest > highest:
                highest = ptest
                print ptest
            break
