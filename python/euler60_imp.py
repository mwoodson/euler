#!/usr/bin/env python


z = 6550

row = [0] * z
pairs = [None] * z
for i in range(z):
    pairs[i] = row[:]

primes = [0] * z 

primes[0] = 2
primes[1]=3


def primeSieve(n):
    candidates = range(n+1)
    fin = int(n**.5)
    for i in xrange(2,fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)

    return [i for i in candidates[2:] if i ]

def isprime(n):
    global primes
    if n == 2: return True
    for p in primes:
        if p * p > n: return True
        if (n / p * p == n): return False
    return True

def main():
    global z, primes, pairs
    i=5
    primes = primeSieve(10000)[:z]
#    count = 2
#    while(count < z):
#        if isprime(i):
#            #print i
#            primes.insert(count,i)
#            count += 1
#        i += 2
#    while(count < z):
#        for p in primes:
#            if p * p > i: 
#                primes.insert(count,i)
#                count += 1
#                break
#            if (i / p * p == i): break
#        else:
#            primes.insert(count,i)
#            count += 1
#        i += 2

    ashift = 10
    for ai in range(z):
        a = primes[ai]
        if(a > ashift): ashift *= 10
        bshift = 10
        for bi in range(ai):
            b = primes[bi]
            if (b > bshift): bshift *= 10
            if(isprime(a * bshift + b) and isprime(b * ashift + a)):
                pairs[ai][bi] = True;
        for bi in range(ai):
            if not pairs[ai][bi]: continue
            for ci in range(bi):
                if not pairs[ai][ci] or not pairs[bi][ci]: continue
                for di in range(ci):
                    if not pairs[ai][di] or not pairs[bi][di] or \
                       not pairs[ci][di]: continue

                    #print primes[ai],primes[bi],primes[ci],primes[di]
                    for ei in range(di):
                        if not pairs[ai][ei] or not pairs[bi][ei] or \
                           not pairs[ci][ei] or not pairs[di][ei]: continue
                        print primes[ai],primes[bi],primes[ci],primes[di],primes[ei]
                        print sum([primes[ai],primes[bi],primes[ci],primes[di],primes[ei]])
                        raise SystemExit








if __name__ == "__main__":
    main()
