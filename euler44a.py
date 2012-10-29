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


def main():
    found = False
    all_pent = set(gen_pent(2500))
    for x in all_pent:
        for y in all_pent:
            if x+y in all_pent and x-y in all_pent:
                print x-y
                found = True
                break
        if found: break




if __name__ == "__main__":
    main()
