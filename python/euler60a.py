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

primes = primeSieve(100000000)[1:] # if len(set([c for c in str(z)])) != len(z)]
del(primes[1])
print primes[:5]
prime_set = set(primes)

def main():
    start = time.time()
    candidates = set([])
    print "%s : Got primes"%str(time.time() - start)
    print "Starting phase 1"
    break_length = len(primes[-1])
    largest = 0
    for a in xrange(len(primes[:1000])-1):
        for b in xrange(a+1,len(primes[:1000])):
            z = primes[a]+primes[b]
            if check_set(z) and check_set(primes[b]+primes[a]):

                result = sorted([primes[a],primes[b]], key=int)
                candidates.add(tuple(result))

    print "%s : part1 finished"%str(time.time() - start)
    c3 = set([])
    clist = list(candidates)
    print len(candidates)
    for astr in primes[:5000]:
        for z in clist:
            if len(set([astr+z[1],z[1]+astr,astr+z[0],z[0]+astr]).intersection(prime_set)) == 4:
                result = sorted([z[0],z[1],astr], key=int)
                c3.add(tuple(result))
                
    print "%s : part2 finished"%str(time.time() - start)
    clist = list(c3)
    candidates = set([])
    for astr in primes[:10000]:
        for z in clist:
            if len(set([astr+z[2],z[2]+astr,astr+z[1],z[1]+astr,astr+z[0],z[0]+astr]).intersection(prime_set)) == 6:
                result = sorted([z[0],z[1],z[2],astr], key=int)
                candidates.add(tuple(result))
        
    print candidates

    print "%s : part3 finished"%str(time.time() - start)
    c3 = set([])
    clist = list(candidates)
    print "len=>%s"%len(clist)
    for astr in primes[:10000]:
        for z in clist:
            if len(z[-1] + astr) > break_length: break
            if astr+z[3] in prime_set and z[3]+astr in prime_set and \
               astr+z[2] in prime_set and z[2]+astr in prime_set and \
               astr+z[1] in prime_set and z[1]+astr in prime_set and \
               astr+z[0] in prime_set and z[0]+astr in prime_set:
                result = sorted([z[0],z[1],z[2],z[3],astr], key=int)
                c3.add(tuple(result))
            else:
                if is_prime(astr+z[3]) and is_prime(z[3]+astr) and \
                   is_prime(astr+z[2]) and is_prime(z[2]+astr) and \
                   is_prime(astr+z[1]) and is_prime(z[1]+astr) and \
                   is_prime(astr+z[0]) and is_prime(z[0]+astr):
                    result = sorted([z[0],z[1],z[2],z[3],astr], key=int)
                    candidates.add(tuple(result))

    print "%s : part4 finished"%str(time.time() - start)
    print c3

    lowest = int(primes[-1])
    pointer = None
    for result in list(c3):
        tmp = sum([int(x) for x in result])
        if tmp < lowest:
            lowest = tmp
            print lowest
            print result


if __name__ == "__main__":
    main()


    '''
    if they must equal 10
    and there are 8 sets with the same number
    there must be a way to limit the search space based on #count

    By replacing any number of combinations of numbers



    set([('467', '587', '617', '6323', '9473'), ('3', '17', '449', '2069', '6353'), ('3', '17', '449', '2069', '6599'), ('3', '7', '109', '673', '20887'), ('3', '37', '67', '2377', '5923'), ('23', '311', '677', '827', '1871'), ('3', '17', '449', '6353', '6599'), ('7', '19', '97', '3727', '4507'), ('3', '7', '109', '673', '22921'), ('3', '7', '109', '673', '29059'), ('3', '7', '109', '673', '34303')])


    '''
    
