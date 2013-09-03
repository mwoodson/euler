#!/usr/bin/env python
#import pdb 
"""
Triangle words

1,3,6,10,15,21,28,36,45,55

SKY = 19 + 11 + 25 = 55
"""
#triangle numbers
tri_nums = [.5*x * (x+1) for x in range(100)]
mydict = dict()

for  x in range(65,65+26):
    mydict[chr(x)] = x-64

with open("words.txt") as fd:
    words = fd.read().split(',')

print len(filter(lambda x: x in tri_nums, [sum([mydict[letter] for letter in word.replace('"',"")]) for word in words]))

#OR

#count = 0 
#for word in words:
#    word = word.replace('"',"")
#    s = sum([mydict[letter] for letter in word])
#    if s in tri_nums:
#        count += 1
#    
#print count
