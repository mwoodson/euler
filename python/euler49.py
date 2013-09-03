#!/usr/bin/env python

import math

'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

def primeSieve4digit(n):
    candidates = range(n+1)
    fin = int(n**.5)
    for i in xrange(2,fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)

    #can filter out all 200k's, 400's, 600's, 800's
    #for i in range(2,9,2):
        #candidates[i*100000:(i+1)*100000] = [None] * 100000
    return [i for i in candidates[2:] if i and i > 1000 and i < 9999]


def main():
    primes = primeSieve4digit(10000)
    for z in primes:
        x = z+3330
        y = z+2*3330
        if y in primes and x in primes \
           and set([a for a in str(z)]) == set([a for a in str(x)]) == set([a for a in str(y)]):
            print z,z+3330,z+2*3330 
            


if __name__ == "__main__":
    main()
