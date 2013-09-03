#!/usr/bin/env python
import collections

'''
The following iterative sequence is defined for the set of positive integers:

n = n/2 (n is even)
n = 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 - 40 - 20 - 10 - 5 - 16 - 8 - 4 - 2 - 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


mydict = collections.defaultdict(int)
highest = 0,0
for i in xrange(2, 1000001):
    num_list = []
    x = i
    count = 0
    while (x != 1):
        count += 1
        if mydict[x] > 0:
            break
        if x % 2 ==0:
            x = x/2
        else:
            x = 3*x+1
    mydict[i] = count + mydict[x]
    if mydict[i] > highest[1]:
        highest = i,mydict[i]+1
print highest
