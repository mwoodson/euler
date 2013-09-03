#!/usr/bin/env python
import math

'''
The sum of the squares of the first ten natural numbers is,
    1pow(2) + 2pow(2) + ... + 10pow(2) = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)pow(2) = 55pow(2) = 3025

    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

sum_of_sq = 0
sum_of_num = 0
sum_of_pow = 0
for i in xrange(0, 101):
    sum_of_num += i
    sum_of_pow += math.pow(i,2)

print sum_of_num
print sum_of_pow
print math.pow(sum_of_num, 2) 
print math.pow(sum_of_num, 2) - sum_of_pow
