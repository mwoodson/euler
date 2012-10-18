#!/usr/bin/env python


'''
p is the perimeter of a right angle triangle with integral sides, {a,b,c}.
There are exactly three solutions for p = 120.  

For which value of p<= 1000 is the number of solutions maximized?

'''


def main():
    counter = {}
    largest = (0,0)
    for p in range(4,1001,2):
        counter[p] = 0
        for a in range(3, p/4 + 1):
            for b in range(a+1,(p-a)/2):
                z = a**2 + b**2
                c = z**.5
                if a + b + c == p:
                    counter[p] += 1
        if counter[p] > largest[1]:
            largest = (p,counter[p])


    print largest


if __name__ == "__main__":
    main()
