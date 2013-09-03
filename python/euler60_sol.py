#!/usr/bin/env python

from copy import copy
from math import sqrt
#import psyco
#psyco.full()

primes = [2,3,5,7,11,13]
def nextprime():
    next_num = primes[-1] + 2
    nnsqrt = int(sqrt(next_num))
    isprime = False
    while not isprime:
        isprime = True
        for prime in primes:
            if prime > nnsqrt: break
            if next_num % prime == 0:
                next_num += 2
                isprime = False
                break
    primes.append(next_num)
    return next_num

def is_prime(num):
    # Uncommenting the following line approximately doubles
    # the time taken for this program!
    #if num in primes: return True
    nsqrt = int(sqrt(num))
    if num == nsqrt * nsqrt: return False
    last_prime = primes[-1]
    # Make sure we have enough prime numbers to test this.
    while last_prime < nsqrt:
        last_prime = nextprime()
    for prime in primes:
        if prime > nsqrt: break
        if num % prime == 0: return False
    return True

concatmem = {}
def concat2(a, b):
    # NB: Always called with a > b.
    key_pair = (a, b)
    if key_pair in concatmem.keys(): return concatmem[key_pair]
    stra = str(a)
    strb = str(b)
    result = is_prime(int(stra + strb)) \
         and is_prime(int(strb + stra))
    concatmem[key_pair] = result
    return result

def concat(set, lvl):
    # 'set' is a five-element list, but we only want to
    # compare elements set[0]..set[lvl-1] with set[lvl]
    for i in xrange(lvl):
        if not concat2(set, set[lvl]): return False
    return True

def find_set():
    min_sum_start = 999999999999 # Large enough?
    min_sum = min_sum_start
    i = 4
    set = [0, 0, 0, 0, 0]
    while True:
        i += 1
        # primes should get bigger faster than I need it.
        set[0] = primes
        for j in xrange(i - 1, 3, -1):
            set[1] = primes[j]
            if not concat(set, 1): continue
            for k in xrange(j - 1, 2, -1):
                set[2] = primes[k]
                if not concat(set, 2): continue
                for l in xrange(k - 1, 1, -1):
                    set[3] = primes[l]
                    if not concat(set, 3): continue
                    for m in xrange(l - 1, 0, -1):
                        set[4] = primes[m]
                        if not concat(set, 4): continue
                        sum_set = sum(set)
                        if min_sum > sum_set:
                            min_sum = sum_set
                            min_set = copy(set)
        if min_sum < min_sum_start: return min_sum, min_set

sum_of_set, set = find_set()
print 'Sum of prime set:', sum_of_set, ' Prime set:', set
