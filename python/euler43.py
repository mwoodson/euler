#!/usr/bin/env python

import pdb
import itertools

'''
the number, 1406357289, is a 0 to 9 pandigital number because it is
made up of each of the digits 0 to 9 in some order, but it also has a
rather interesting sub-string divisibility property.

Find the sum of all 0 to 9 pandigital number with this property.

'''


def main3():
    total = 0
    found = None
    dlist = ["9","8","7","6","5","4","3","2","1","0"]
    #for y in range(len(dlist)):
    dstr = "".join(dlist)
    for i in itertools.permutations(dstr,len(dstr)):
        z = "".join(i)
        #print z
        if (int(z[-3:])   % 17) != 0: continue
        if (int(z[-4:-1]) % 13) != 0: continue
        if (int(z[-5:-2]) % 11) != 0: continue
        if (int(z[-6:-3]) % 7) != 0: continue
        if (int(z[-7:-4]) % 5) != 0: continue
        if (int(z[-8:-5]) % 3) != 0: continue
        if (int(z[-9:-6]) % 2) != 0: continue

        total += int(z)

    print total


if __name__ == "__main__":
    #a = set(main2()) 
    #b = set(main3())
            #
    main3()
    #print a-b
