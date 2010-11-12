#!/usr/bin/env python
import collections
import math
import decimal
decimal.getcontext().prec = 10000

'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    ^(1)/_(2)   =       0.5
    ^(1)/_(3)   =       0.(3)
    ^(1)/_(4)   =       0.25
    ^(1)/_(5)   =       0.2
    ^(1)/_(6)   =       0.1(6)
    ^(1)/_(7)   =       0.(142857)
    ^(1)/_(8)   =       0.125
    ^(1)/_(9)   =       0.(1)
    ^(1)/_(10)  =       0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that ^(1)/_(7) has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^(1)/_(d) contains the longest recurring cycle in its decimal fraction part.

'''

def get_repeating(anum):
    solutions = []
    for i in range(1, 10):
        res = anum.split("%s"%i)
        if len(res) >= 2:
            solutions.append(res)
    highest = 0
    for x in solutions:
        if len(x) > 3:
            if x[2] == x[3] and x[3] == x[4]:
                if len(x[4])+1 > highest:
                    highest = int(len(x[4]))+1
    return highest    


max = 0
value = 0
for i in range(1, 1001):
    d = (decimal.Decimal(1)/decimal.Decimal(i))
    fract = d.to_eng_string().split(".")
    if len(fract) > 1:
        fract = fract[1]
    else:       
        fract = fract[0]
    num = get_repeating(fract)
    if num > max:
        max = num
        value = i
            
            
print value
print max
    
