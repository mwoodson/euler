#!/usr/bin/env python

import math

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

#function works great!
# site: http://www.daniweb.com/code/snippet216558.html#
def primes(n):
  """ returns a list of prime numbers from 2 to < n """
  if n < 2:  return []
  if n == 2: return [2]
  # do only odd numbers starting at 3
  s = range(3, n, 2)
  # n**0.5 may be slightly faster than math.sqrt(n)
  mroot = n ** 0.5
  half = len(s)
  i = 0
  m = 3
  while m <= mroot:
    if s[i]:
      j = (m * m - 3)//2
      s[j] = 0
      while j < half:
        s[j] = 0
        j += m
    i = i + 1
    m = 2 * i + 3
  # make exception for 2
  return [2]+[x for x in s if x]

primeList = primes(1999999)
print sum(x for x in primeList)
#print "List of prime numbers from 2 to < %d:" % num
#print primeList

def isprime(n):
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True

#sum = 0
#for i in xrange(1, 1999999, 2):
    #if isprime(i):
        #print i
        #sum += i

#print sum+2
