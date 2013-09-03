#!/usr/bin/env python

import math

'''
pentagonal numbers are generate by the formula Pn=n(3n-1)/2. The first 
test numbers are: 
1,5,12,22,35,51,70,92,117,145

P4+P7 = 22 + 70 = 92 = P8.  However their diff, 70-22 = 48 is not pentagonal.

FInd the pair of pentagonal numbers, Pj and Pk, for which their sum and difference
is pentagonal and D = |Pk-Pj| is minimized; what is the value of D?
'''

from collections import defaultdict

def gen_pent(x):
    for n in xrange(1,x+1):
        yield n*(3*n-1) / 2

def gen_hex(x):
    for n in xrange(1,x+1):
        yield n*(2*n-1)

def gen_tri(x):
    for n in xrange(1,x+1):
        yield n*(n+1) / 2


def main():
    found = False
    all_pent = set(gen_pent(100000))
    all_hex = set(gen_hex(100000))
    #all_tri = set(gen_tri(10000))

    #print candidates
    #return
    for tnum in gen_tri(100000):
        if tnum < 40755: continue
        if tnum in all_pent and tnum in all_hex:
            print tnum
        



if __name__ == "__main__":
    main()
