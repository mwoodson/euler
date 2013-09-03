#!/usr/bin/env python

'''
Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
'''

'''
Combination formula states:
for a 4x3 rectangle
possible solutions is C(n,r) = n! / (r! * (n-r)!
7 steps to find a solution 
so:
    C(7,4) = 7! / (4! * (7-4)!

so for 20x20 grid
possible combinations = C(40,20) = 40!/ (20! * (40-20)!
    fact(40) / (fact(20) * fact(40-20))
    137846528820L
'''
'''
Start d, d, d, d
choose any two to be r's
first iteration:
d, d, r, r
d, r, d, r
r, d, r, d
r, r, d, d


1, 2 
1, 3 
1, 4
2, 3
2, 4
3, 4

#ALL must have 50% Rs and Ds
'''
'''
[r, r, d, d]
alist[(0, 1), (0, 2), (1,2), (2,2)]
[r, d, r, d]
alist[(0, 1), (1, 1), (1,2), (2,2)]
[r, d, d, r]
alist[(0, 1), (1, 1), (2,1), (2,2)]
[d, r, d, r]
alist[(1, 0), (1, 1), (2,1), (2,2)]
[d, d, r, r]
alist[(1, 0), (2, 0), (2,1), (2,2)]
[d, r, r, d]
alist[(1, 0), (1, 1), (1,2), (2,2)]
'''

def fact(x): 
    return (1 if x==0 else x * fact(x-1))

#order does not matter

#print fact(40)/(fact(20) * fact(40-20))
#MAX_MOVES = 3 #2x2 grid, moves = 4 but zero based is 3
#MAX_MOVES = 5 #2x2 grid, moves = 4 but zero based is 3
MAX_MOVES = 20 #2x2 grid, moves = 4 but zero based is 3

#for i in xrange(0,MAX_MOVES):
    #alist.append([True for x in xrange(0,MAX_MOVES)])

#print alist
count = 0
blist = []
for i in xrange(0, MAX_MOVES+1):
    blist.append(True)
alist = blist
while (True):
    for x in xrange(0, MAX_MOVES-1):
        for y in xrange(MAX_MOVES, 0, -1):
            alist[x] = False
            alist[y] = False
            count += 1
            #print alist
            alist = blist
    break
print count


#counter=0
#def doPath(x, y, MAX):
#    global counter
#    if (x==MAX and y==MAX):
#        counter+=1
#        return
#    elif (x > MAX or y > MAX):
#        return
#    doPath(x+1,y, MAX)
#    doPath(x,y+1, MAX)
#
#doPath(0,0, 20)
#print counter
#size_of_grid = 20
#alist = []


