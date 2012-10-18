#!/usr/bin/env python


'''
p is the perimeter of a right angle triangle with integral sides, {a,b,c}.
There are exactly three solutions for p = 120.  

For which value of p<= 1000 is the number of solutions maximized?

'''


def main():
    for p in range(1,1001):
        for x in range(1,p):
            for y in range(x,p):
                for z in range(y,p):
                    if x**2 + y**2 == z:
                        print x,y,z,p





if __name__ == "__main__":
    main()
