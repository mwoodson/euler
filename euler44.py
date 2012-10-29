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

def do_pent(x):
    return x*(3*x-1) / 2

def do_reverse(x):
    return round(.16666+.1666666 * math.sqrt(24*x + 1))

def main():
    found = False
    d = defaultdict(int)
    for n in range(1, 5000):
        pn = do_pent(n)
        d[n] = pn
        for p in d.keys():
            pnp1 = pn-d[p]
            t1 = pnp1 == do_pent(do_reverse(pnp1))
            if not t1: continue
            pnp2 = pn+d[p]
            t2 = pnp2 == do_pent(do_reverse(pnp2))
            if not t2: continue
            if n == p: continue
            print n,p,pnp1
                #print pnp1,pnp2
                #print p,n,d[p],d[n]
            found = True
            break
        

        if found: break




if __name__ == "__main__":
    main()
