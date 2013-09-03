#!/usr/bin/env python

import math

'''
By replacing the 1st digit of *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

'''

def primeSieve(n):
    candidates = range(n+1)
    fin = int(n**.5)
    for i in xrange(2,fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)

    #can filter out all 200k's, 400's, 600's, 800's
    return [str(i) for i in candidates[2:] if i ]

from collections import defaultdict
import pdb

def main():
    primes = primeSieve(1000000) # if len(set([c for c in str(z)])) != len(z)]
    prime_set = set([x for x in primes if len(x) != len(set(x))])
    prime_set_length = len(prime_set)
    found = False
    for i in range(len(primes)):
        z = primes[i]
        results = []
        for x in z:
            for yind in range(10):
                tmp_z = z.replace(x,str(yind))
                if len(set([tmp_z]).intersection(prime_set)) > 0:
                    results.append(tmp_z)
            answer = set(results)
            if len(answer) == 8:# or len(answer) == 7:
                print z,len(answer),answer
                found = True
            break
        if found:
            break

if __name__ == "__main__":
    main()


    '''
    if they must equal 10
    and there are 8 sets with the same number
    there must be a way to limit the search space based on #count

    By replacing any number of combinations of numbers
    '''
