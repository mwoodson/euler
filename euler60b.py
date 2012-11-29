#!/usr/bin/env python


'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


'''
def is_prime(x):
    x = int(x)
    for i in xrange(2,int(x**.5)):
        if x % i == 0:
            return False
    return True

def primeSieve(n):
    candidates = range(n+1)
    fin = int(n**.5)
    for i in xrange(2,fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)

    return [str(i) for i in candidates[2:] if i ]

import time

def check_set(a):
    global prime_set
    return len(set(a).intersection(prime_set)) > 0

start = time.time()
primes = primeSieve(100000000)[1:] # if len(set([c for c in str(z)])) != len(z)]
del(primes[1])
prime_set = set(primes)

def main():
    print "%s : Got primes"%str(time.time() - start)
    print "Starting phase 1"
    break_length = len(primes[-1])
    largest = 0
    for a in xrange(len(primes[:1000])-4):
        for b in xrange(a+1,len(primes[:1000])-3):
            #v w x y z
            v = primes[a]+primes[b]
            w = primes[b]+primes[a]
            if check_set(v) and check_set(w):
                v = primes[a]
                w = primes[b]
                for c in xrange(b+1,len(primes[:10000])-2):
                    if len(set([primes[c]+v,v+primes[c],primes[c]+w,w+primes[c]]).intersection(prime_set)) == 4:
                        x = primes[c]
                        for d in xrange(c+1,len(primes[:10000])-1):
                            if len(set([primes[d]+v,v+primes[d], \
                                        primes[d]+w,w+primes[d], \
                                        primes[d]+x,x+primes[d]]).intersection(prime_set)) == 6:
                                y = primes[d]
                                for e in xrange(d+1,len(primes[:10000])):
                                    if len(set([primes[e]+v,v+primes[e], \
                                                primes[e]+w,w+primes[e],\
                                                primes[e]+x,x+primes[e],\
                                                primes[e]+y,y+primes[e]]).intersection(prime_set)) == 8:
                                        print sum([int(abc) for abc in [v,w,x,y,primes[e]]])
                                        print v,w,x,y,primes[e]
                                        raise SystemExit


if __name__ == "__main__":
    main()


    '''
    if they must equal 10
    and there are 8 sets with the same number
    there must be a way to limit the search space based on #count

    By replacing any number of combinations of numbers



    set([('467', '587', '617', '6323', '9473'), ('3', '17', '449', '2069', '6353'), ('3', '17', '449', '2069', '6599'), ('3', '7', '109', '673', '20887'), ('3', '37', '67', '2377', '5923'), ('23', '311', '677', '827', '1871'), ('3', '17', '449', '6353', '6599'), ('7', '19', '97', '3727', '4507'), ('3', '7', '109', '673', '22921'), ('3', '7', '109', '673', '29059'), ('3', '7', '109', '673', '34303')])


    '''
    
