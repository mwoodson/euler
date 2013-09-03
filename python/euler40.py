#!/usr/bin/env python


'''
dn reprensents the nth digit of the fractional part, find the value 
of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
'''


def main():
    d1  = 1
    d10 = 1
    d100 =  0
    d1000 = 0
    d10000 = 0 
    d100000 = 0 
    d1000000 = 0
    a = []
    #for i in xrange(1,1002):
    for i in xrange(1,1000001):
        a.append(str(i))
    c = ''.join(a)
    #d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
    b = [c[0] , c[10-1] , c[100-1] , c[1000-1] , c[10000-1] , c[100000-1] , c[1000000-1]]
    print reduce(lambda x,y: int(x)*int(y), b)


if __name__ == "__main__":
    main()
