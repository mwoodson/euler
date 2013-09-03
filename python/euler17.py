#!/usr/bin/env python

import math

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''


#count = 0
#word_len = 0
#for x in xrange(1000, 1, -1):
    #if x % 1000 == 0:
        #word_len += len("one thousand")
    #if 

num_dict = {0 : len("zero"),
            1 : len("one"), 
            2 : len("two"), 
            3 : len("three"),
            4 : len("four"),
            5 : len("five"),
            6 : len("six"),
            7 : len("seven"),
            8 : len("eight"),
            9 : len("nine"),
            10 : len("ten"),
            11 : len("eleven"),
            12 : len("twelve"),
            13 : len("thirteen"),
            14 : len("fourteen"),
            15 : len("fifteen"),
            16 : len("sixteen"),
            17 : len("seventeen"),
            18 : len("eighteen"),
            19 : len("nineteen"),
            20 : len("twenty"),
            30 : len("thirty"),
            40 : len("forty"),
            50 : len("fifty"),
            60 : len("sixty"),
            70 : len("seventy"),
            80 : len("eighty"),
            90 : len("ninety"),
            100: len("hundred"),
            1000: len("thousand")}

def get_count(astring):
    anum = 0
    #print "processing: %s"%astring
    if len(astring) == 4:
        first_num = astring[0]
        #print "1000: %s"%first_num
        anum +=  num_dict[int(first_num)] + num_dict[1000]
        if int(astring) %1000 == 0:
            print "DOES % to ZERO"
            return anum
        astring = astring[1:]
        #print "passing: %s"%astring
    if len(astring) == 3:
        first_num = astring[0]
        #print "100: %s"%first_num
        anum +=  num_dict[int(first_num)] + num_dict[100] 
        if int(astring) %100 == 0:
            print "DOES % to ZERO"
            return anum
        anum += 3# for "and"
        astring = astring[1:]
        #print "passing: %s"%astring
    if len(astring) == 2:
        if int(astring) > 9 and int(astring) < 20 or \
         int(astring) in num_dict.keys():
            anum += num_dict[int(astring)]
            return anum
        first_num = str(astring)[0]
        #print "10: %s"%first_num
        #print first_num
        anum +=  num_dict[int(first_num) * 10]
        astring = astring[1:]
        #print "passing: %s"%astring
    if len(astring) == 1:
        if astring == "0":
            return anum
        #print astring
        #print "1: %s"%astring
        anum += num_dict[int(astring)]
    return anum
    
count = 0
for x in xrange(1, 1001):
    count += get_count(str(x))
    num = get_count(str(x))
    print "%s:%s"%(x,num)
        
print count


