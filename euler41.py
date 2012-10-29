#!/usr/bin/env python

import pdb

'''
What is the largest n-digit pandigital prime that exists?
'''

def primeSieveO(n):
    candidates = range(n+1)
    fin = int(n**.5)
    for i in xrange(2,fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)

    #can filter out all 200k's, 400's, 600's, 800's
    for i in range(2,9,2):
        candidates[i*100000:(i+1)*100000] = [None] * 100000
    return [i for i in candidates[2:] if i], candidates

def primeSieve(start, n):
    #pdb.set_trace()
    candidates = range(start, n+1)
    fin = int(n**.5)
    #for i in xrange(2,fin+1):
    for i in xrange(2,fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * ((n-start)//i - 1)

    candidates[0] = None
    #can filter out all 200k's, 400's, 600's, 800's
    #for i in range(2,9,2):
        #candidates[i*100000:(i+1)*100000] = [None] * 100000
    return [i for i in candidates[2:] if i]#, candidates
    #return filter(lambda x: x if x else None, candidates), candidates

def main():
    #for i in primeSieve(10000000)[0]:
    for i in primeSieveO(987654321)[0]:
        #check if pandigital
            
        z = str(i)
        x = set([a for a in z])
        if len(x) != len(z): continue
        #if i == 2143:
            #pdb.set_trace()

        for y in range(1,len(z)+1):
            if str(y) not in z:
                break
        else:
             print i
            

def main2():
    last = 0
    pall = []
    for i in xrange(last, 1000, 100):
        pall.extend(primeSieve(last,i))
        #print primeSieve(last,i)[0]
        last = i
    return pall

def is_prime(x):
    for i in xrange(2,int(x**.5)+1):
        if x % i == 0: return False
    return True

def main3():
    found = None
    import itertools
    dlist = ["9","8","7","6","5","4","3","2","1"]
    for y in range(len(dlist)):
        dstr = "".join(dlist[y:])
        for i in itertools.permutations(dstr,len(dstr)):
            a=int("".join(i))
            if is_prime(a): 
                print a
                found = a
                break
        if found: break


if __name__ == "__main__":
    #a = set(main2()) 
    #b = set(main3())
            #
    main3()
    #print a-b
