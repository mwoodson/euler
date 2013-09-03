#!/usr/bin/env python
import collections
import math
import heapq
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
ans:
4179871
'''
a_dict = collections.defaultdict(int)
my_dict = {}
num_sum = 0
abundant = []
a_sums = []

def divisors(num):
    divisors_sum = 1 
    for x in range(2, int(math.sqrt(num))+1):
        if num % x == 0:
            divisors_sum += x
            if x != num/x: 
                divisors_sum += num/x
    return divisors_sum

for i in range(1, 28124):
    if divisors(i) > i:
        abundant.append(i)
        for z in range(0, len(abundant)):
            a_dict[abundant[z] + i] += 1
    if a_dict[i] == 0:
        num_sum += i

print num_sum
