#!/usr/bin/env python




'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''

start = "1000"
found = False
while True:
    for i in range(int(start)+2,int(start) + int(start)/6, 2):
        x2 = str(i*2)
        x6 = str(i*6)
        x2s = set(x2)
        if len(x2s.difference(set(x6))) == 0:
            x5 = str(i*5)
            if len(x2s.difference(set(x5))) == 0:
                x4 = str(i*4)
                if len(x2s.difference(set(x4))) == 0:
                    x3 = str(i*3)
                    if len(x2s.difference(set(x3))) == 0:
                        print "candidate => %s" % i
                        for i in x2s:
                            x2c = x2.count(i)
                            if x2c == x6.count(i) and \
                               x2c == x5.count(i) and \
                               x2c == x4.count(i) and \
                               x2c == x3.count(i):
                                continue
                            else:
                                break
                        else:
                            print i
                            found = True
                            break
                        #test each of them
    else:
        start += "0"
        print start

    if found:
        break

    if int(start) > 100000000000:    
        print "NOT FOUND"
        break

