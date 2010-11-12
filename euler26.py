#!/usr/bin/env python
#import collections
#import math
from decimal import Decimal
from decimal import getcontext
import pdb
'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2     =       0.5
1/3     =       0.(3)
        1/4     =       0.25
        1/5     =       0.2
        1/6     =       0.1(6)
        1/7     =       0.(142857)
        1/8     =       0.125
        1/9     =       0.(1)
        1/10    =       0.1
        Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

        Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
0.14285714285714285714285714285714285714285714285714
1
14
142
1428
14285
142857


#start looking at characters.  see if a char repeats itself
#def find_repeat(x):
#    if "." in str(x):
#        num = str(x)[2:]
#    else:
#        return 0
#    if len(num) == 1:
#        return 1
#    same = 0
#    last_char = ""
#    pattern = ""
#    pattern1 = ""
#    for i in xrange(len(num)):
#        if num[i] == '0':
#            continue
#        else:
#            break
#    num = num[i:]
#
#    if len(num) > 10:
#        while(True):
#            if num[0] not in num[1:]:
#                num = num[1:]
#            else:
#                break
#
##pdb.set_trace()
#    for pos, char in enumerate(num):
#        pattern += char
#        if last_char == char:
#            same += 1
#            if same == 3:
#                return 1
#        else:
#            same = 0
#        if pos+1 <= len(num)-1 and pos > 1:
#            if num[:pos+1] == pattern: 
#                if pattern == num[pos+1:pos+1+len(pattern)]:
#                    return len(pattern)
#        last_char = char
#    return len(num)




#def find_pattern(x):
#    num = str(x)[2:-2]
#    for i in xrange(len(num)-1,-1,-1):
#        if num[i:] == num[i-len(num[i:]):i]:
#            return len(num[i:])
#    return -1
        

        
getcontext().prec = 2000
#0.14285714285714285714285714285714285714285714285714
most = 0
high = 0
num = 0
rval = 0
for i in xrange(11,1001):
#ans = Decimal(1)/Decimal(i)
    num = str(Decimal(1)/Decimal(i))[:-1]
    rval = -1
    for z in xrange(len(num)-1,-1,-1):
        if num[z:] == num[z-len(num[z:]):z]:
            rval = len(num[z:])
            break
    if rval > most:
        most = rval
        high = i

print "num=",high
print "pattern len=",most
