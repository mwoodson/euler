#!/usr/bin/env python

import math

'''
What is the smallest odd composite that cannot be written as the sum of a prime and 
twice a square?
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
    return [i for i in candidates[2:] if i]

def prime_factors(x,primes):
    facts = []
    for i in primes:
        if x % i == 0:
            facts.append( i )
        if i > x/2:  break
            
    if 2 in facts and 4 in facts:
        #facts.remove(4)
        facts.remove(2)
    return set(facts)


def main():
    c = 4
    primes = primeSieve(1000000)[:10000]
    primes.insert(2,2**2)
    consecutive = []
    for i in xrange(1,500000):
        if i in primes:  
            consecutive = []
            continue
        f = prime_factors(i,primes)
        if len(f) == c:
            consecutive.append(i)
            #print f, i
        else:
            consecutive = []

        if len(consecutive) == c:
            break
        
    print consecutive
        
        

        



if __name__ == "__main__":
    main()
