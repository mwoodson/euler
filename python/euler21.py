#!/usr/bin/env python
import collections
import math
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def find_div(x):
    run_sum = 0
    for i in xrange(1, x/2+1):
        if x % i == 0:
            #print i
            run_sum += i
    return run_sum



final_sum = 0
for i in xrange(1, 10000):
    i_num_sum = find_div(i)
    isum_amic = find_div(i_num_sum)
    if isum_amic == i and i != i_num_sum:
        print i
        final_sum += i 
print final_sum
#print sum([x for x in amicables])


