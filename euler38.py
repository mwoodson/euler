#!/usr/bin/env python


'''
pandigital numbers

what is the largest 1 to 9 pandigital 9 digit number that can be formed 
as the concatenated product of an integer with (1,2,..,n) where n>1?


'''


def main():
    largest = 0

    for i in range(9999,1,-1):
        z = ""
        x = set([])
        for y in range(1,100):
            t = str(i * y)
            z += t
            if int(z[0]) != 9:
                break 
            if len(z) == 9:
                [x.add(c) for c in t]
                if len(x) == 9:
                    if "0" in z:
                        break
                    if int(z) > largest:
                        largest = int(z)
                    #print i,y,z
                break
            if len(z) >= 9:
                break
    print largest


if __name__ == "__main__":
    main()
