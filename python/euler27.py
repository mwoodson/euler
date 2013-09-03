#!/usr/bin/env python
import collections
import math
import heapq
'''
Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 40^(2) + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

    n^2 + an + b where |a| < 1000 and |b| < 1000
        where |n| is the modulus/absolute value of n
            e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients a and b for the quadratic expression that produces the maximum number of primes for consecutive values of n starting with n = 0

'''

def is_prime(num):
    divisors_count = 2 
    #print num
    if num < 2:
        return False
    for x in range(2, int(math.sqrt(num))+1):
        if num % x == 0:
            #print x,
            divisors_count += 1
            if x != num/x: 
                #print num/x,
                divisors_count += 1
                #divisors_sum += num/x
        if divisors_count > 2:
            break;
    else:
        return True
    return False;

max = 0
result = 0
for i in range(-999, 1000):
    for x in range(-999, 1000):
        n = 0
        num=0
        while (1):
            if not (is_prime(n*n + n*i + x)):
                break
            n+=1
        if n > max:
            max = n
            result = i*x

print result
