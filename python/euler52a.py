#!/usr/bin/env python




'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''

start = "100"
end = "170"
found = False
while True:
    print "range -> %s to %s"%(int(start), int(end))
    for i in range(int(start)+2,int(end)):
        x = str(i)
        x2 = str(i*2)
        x6 = str(i*6)
        x5 = str(i*5)
        x4 = str(i*4)
        x3 = str(i*3)
        xs = set(x)
        #print "candidate => %s" % i
        for z in xs:
            xc = x.count(z)
            if xc == x6.count(z) and \
               xc == x5.count(z) and \
               xc == x4.count(z) and \
               xc == x3.count(z) and \
               xc == x2.count(z):
            #if xc == x2.count(i):
                continue
            else:
                break
        else:
            print i
            found = True
            break
        #if len(x2s.difference(set(x6))) == 0:
        #if len(x2s.difference(set(x5))) == 0:
            #if len(x2s.difference(set(x4))) == 0:
                #if len(x2s.difference(set(x3))) == 0:
                        #test each of them
    else:
        start += "0"
        end += "0"
        print start

    if found:
        break

    if int(start) > 100000000000:    
        print "NOT FOUND"
        break

