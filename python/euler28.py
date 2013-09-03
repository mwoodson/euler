#!/usr/bin/env python
'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

101

31 32 33 34 35 36
30 13 14 15 16 17
29 12  3  4  5 18
28 11  2  1  6 19
27 10  9  8  7 20
26 25 24 23 22 21

170

36 + 16 + 4 + 2 + 10 + 26
31 + 13 + 3 + 1 + 7 + 21

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''
size = 1001
sides = 4
count_sides = 1
minus = size - 1
num = size*size
total = 0
total += num
while num > 1:
    print "total",total
    for i in range(0, size):
        if count_sides % 5 == 0:
            count_sides = 1
            minus -= 2
        num = num - minus
        total += num
        #print "minus",minus
        #print num
        #raw_input()
        count_sides += 1
        #print "total",total
        if num == 1:
            break
print total
        
#4 + 4 + 4 + 4 + 2 + 2 + 2 + 2 
#16 + 8 = 24
