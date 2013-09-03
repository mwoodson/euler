#!/usr/bin/env python

import math

'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


'''

def primeSieve(n):
    candidates = range(n+1)
    fin = int(n**.5)
    for i in xrange(2,fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)

    return [str(i) for i in candidates[2:] if i ]

from collections import defaultdict
import pdb

def main():
    test = defaultdict(list)
    test_keys = set([])
    candidates = set([])
    primes = primeSieve(5000000) # if len(set([c for c in str(z)])) != len(z)]
    prime_set = set(primes)
    print "Starting phase 1"
    #find all that have a 7
    for a in range(len(primes[:5000])-1):
        for b in range(a+1,len(primes[:5000])):
            if len(set([primes[a]+primes[b], primes[b]+primes[a]]).intersection(prime_set)) == 2:
                if primes[b] in test[primes[a]]:
                    continue
                elif len(test[primes[a]]) == 0:
                    test[primes[a]].append(primes[b])
                    test_keys.add(primes[a])
                elif all([x for x in test[primes[a]] if x+primes[b] in prime_set and primes[b]+x in prime_set]):
                    test[primes[a]].append(primes[b])
                    test_keys.add(primes[a])
                    print test[primes[a]]
        if a%1000 == 0: print a

    return
    print "part1 finished"
    remove = set([])
    for a in range(len(primes)):
        for z in list(test_keys):
            if primes[a]+z in prime_set and z+primes[a] in prime_set:
                if all([x for x in test[z] if primes[a]+x in prime_set and x+primes[a] in prime_set]):
                    test[z].append(primes[a])
            else:
                remove.add(z)


    #diff = test_keys - remove 
    tmp_keys = list(test_keys)
    for key in tmp_keys:
        print key,test[key]


    '''


            if primes[a]+z[0] in prime_set and z[0]+primes[a] in prime_set:
               #primes[a]+z[1] in prime_set and z[1]+primes[a] in prime_set:
                c3.add((z[0],z[1],primes[a]))
                
    print "part2 finished"
    print c3
    clist = list(c3)
    candidates = set([])
    for z in clist:
        for a in range(len(primes)):
            if primes[a]+z[0] in prime_set and z[0]+primes[a] in prime_set and  \
               primes[a]+z[1] in prime_set and z[1]+primes[a] in prime_set and \
               primes[a]+z[2] in prime_set and z[2]+primes[a] in prime_set:
                candidates.add((z[0],z[1],z[2],primes[a]))

    print "part3 finished"
    print candidates
    c3 = set([])

    #candidates = set([('19', '97', '7', '4507'), ('3', '673', '7', '109'), ('7', '97', '19', '4507'), ('3', '37', '67', '2377'), ('7', '3727', '97', '19'), ('19', '3727', '97', '7'), ('7', '97', '4507', '19'), ('7', '109', '3', '673'), ('19', '3727', '7', '97'), ('37', '5923', '67', '3'), ('311', '677', '827', '23'), ('7', '19', '3727', '97'), ('3', '67', '2377', '37'), ('37', '2377', '3', '67'), ('23', '311', '677', '827'), ('67', '5923', '3', '37'), ('7', '673', '109', '3'), ('3', '2377', '37', '67'), ('97', '3727', '19', '7'), ('3', '109', '673', '7'), ('7', '109', '673', '3'), ('37', '67', '3', '2377'), ('3', '67', '37', '5923'), ('19', '97', '7', '3727'), ('3', '5923', '67', '37'), ('3', '109', '7', '673'), ('3', '2377', '67', '37'), ('109', '673', '3', '7'), ('37', '67', '2377', '3'), ('7', '97', '19', '3727'), ('677', '827', '23', '311'), ('3', '673', '109', '7'), ('19', '4507', '97', '7'), ('311', '677', '23', '827'), ('19', '97', '4507', '7'), ('97', '4507', '7', '19'), ('37', '67', '3', '5923'), ('7', '3727', '19', '97'), ('3', '37', '2377', '67'), ('67', '2377', '37', '3'), ('7', '19', '4507', '97'), ('23', '827', '677', '311'), ('109', '673', '7', '3'), ('3', '5923', '37', '67'), ('3', '37', '67', '5923'), ('311', '827', '23', '677'), ('37', '5923', '3', '67'), ('19', '97', '3727', '7'), ('7', '19', '97', '4507'), ('37', '67', '5923', '3'), ('19', '4507', '7', '97'), ('67', '2377', '3', '37'), ('311', '827', '677', '23'), ('97', '3727', '7', '19'), ('23', '311', '827', '677'), ('67', '5923', '37', '3'), ('23', '827', '311', '677'), ('7', '4507', '97', '19'), ('97', '4507', '19', '7'), ('3', '67', '37', '2377'), ('3', '7', '673', '109'), ('3', '37', '5923', '67'), ('7', '97', '3727', '19'), ('677', '827', '311', '23'), ('7', '19', '97', '3727'), ('3', '67', '5923', '37'), ('7', '673', '3', '109'), ('23', '677', '311', '827'), ('37', '2377', '67', '3'), ('3', '7', '109', '673'), ('7', '4507', '19', '97'), ('23', '677', '827', '311')])
    clist = list(candidates)

    for a in range(len(primes)):
        for z in clist:
            #print primes[a]+z[0] in prime_set,z[0]+primes[a] in prime_set, \
               #primes[a]+z[1] in prime_set , z[1]+primes[a] in prime_set,\
               #primes[a]+z[2] in prime_set , z[2]+primes[a] in prime_set,\
               #primes[a]+z[3] in prime_set , z[3]+primes[a] in prime_set
            if primes[a]+z[0] in prime_set and z[0]+primes[a] in prime_set and  \
               primes[a]+z[1] in prime_set and z[1]+primes[a] in prime_set and \
               primes[a]+z[2] in prime_set and z[2]+primes[a] in prime_set and \
               primes[a]+z[3] in prime_set and z[3]+primes[a] in prime_set:
                print "HERE"
                c3.add((z[0],z[1],z[2],z[3],primes[a]))
    print "part4 finished"
    print c3

    all_sums = []
    lowest = 10000000
    for z in c3:
        sz = sum(z)
        if sz < lowest: 
            lowest = sz

    print lowest
    '''

if __name__ == "__main__":
    main()


    '''
    if they must equal 10
    and there are 8 sets with the same number
    there must be a way to limit the search space based on #count

    By replacing any number of combinations of numbers
    '''
