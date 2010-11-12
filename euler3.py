#!/usr/bin/env python

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

big_num = 600851475143

x = 1
while (x < big_num):
    if big_num % x == 0:
        num =(big_num / x)
        if (isprime(num)):
            print num
            break
    x+=2
    
