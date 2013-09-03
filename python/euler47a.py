#!/usr/bin/env python

import math

'''
What is the smallest odd composite that cannot be written as the sum of a prime and 
twice a square?
'''

def main():
    total=1000000
    n_factor = [0] * total

    for i in xrange(2,total):
        if n_factor[i] == 0:
            for j in range(2*i, total, i):
                n_factor[j] += 1
        
        
    goal = [4] * 4
    for i in range(2,total):
        if n_factor[i:i+4] == goal:
            print i
            break

        



if __name__ == "__main__":
    main()
