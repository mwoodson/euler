#!/usr/bin/env python
import collections
import math
'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - 1  
[0, 1, 2, 3, 4, 5, 6, 7, 9, 8] - 2  [10 -> 9]
[0, 1, 2, 3, 4, 5, 6, 8, 7, 9] - 3  [8 -> 9]
[0, 1, 2, 3, 4, 5, 6, 8, 9, 7] - 
 - 

[0, 2, 1, 3, 4, 5, 6, 7, 8, 9]
[0, 2, 3, 1, 4, 5, 6, 7, 8, 9]
[0, 2, 3, 4, 1, 5, 6, 7, 8, 9]
...
'''
perms = 1
done = False
limit = 22
while (perms < limit):
    #do switch
    anum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in xrange(len(anum)-1, 0, -1):
        move_num = anum[i]
        for x in range(len(anum)-1,  0, -1):
            anum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            anum[i] = anum[x]
            anum[x] = move_num
            #acpy = anum.replace(anum.index(anum[i]), anum.index(anum[x]))
            #anum = anum.replace(anum[x], move_num)
            #anum = anum.replace(anum[i], anum[x])
            #anum = anum.replace(anum[x], move_num)
            print anum
            print perms
            perms += 1
            if perms >= limit:
                done = True
                break
        if done:
            break
        
    



