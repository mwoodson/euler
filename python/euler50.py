#!/usr/bin/env python

import math

'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

def primeSieve(n):
    candidates = range(n+1)
    fin = int(n**.5)
    for i in xrange(2,fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)

    #can filter out all 200k's, 400's, 600's, 800's
    for i in range(2,9,2):
        candidates[i*100000:(i+1)*100000] = [None] * 100000
    return [i for i in candidates[2:] if i ]


def main():
    most = 20
    prime = 0
    primes = primeSieve(1000000)
    for z in range(1000,21, -1):
        for i in range(len(primes)):
            if most >= z: break
            x = sum(primes[i:i+z])
            if x >= 1000000: break
            if x in primes:
                print "len=%s prime=%s"%(z,x)
                most = z
                prime = i
        if prime != 0: break




if __name__ == "__main__":
    main()
