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


def main():
    squares = [2*i**2 for i in range(1000)]
    odds = range(35,10000,2)
    primes = primeSieve(8000)
    candidates = set(odds) - set(primes)
    all_c = []
    #for a in squares:
        #for b in primes:
            #all_c.append(a+b)
    for i in list(candidates)[:10000]:
        for z in squares[1:]:
            if z > i: continue
            if i - z in primes: break
        else:
            print i
            break


    '''
        #print i
        found = False
        for y in primes:
            if y > i:  break
            tmp = i - y
            if tmp % 2 != 0:  continue
            #print "tmp=",tmp
            #print "y=",y
            for z in sqaures:
                #print "z=",z
                if z>tmp:  break
                #if z == tmp:  print "y=%s z=%s i=%s"%(y,z,i)
                if z == tmp:  
                    found = True
                    break
            else:
                print "Did not find it for i=%s"% i
            if found == True:  break
            
        #if i%5==0:  print i
    '''

        



if __name__ == "__main__":
    main()
