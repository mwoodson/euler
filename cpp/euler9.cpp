#include <iostream>
#include <cstdio>
#include <math.h>

using namespace std;

/*
    A pythagorean triplet is a set of three natural numbers, a < b < c, for which,
     a^(2) + b^(2) = c^(2)
        
    For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
        
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc.
*/

int main()
{
//a^2 + b^2 = c^2
    bool found = false;

    //for a in xrange(1, 1000):
    for(int a = 1; a < 1000; a++)
    {
        //for b in xrange(1, 1000):
        for(int b = a+1; b < 1000; b++)
        {
            int num = a*a + b*b;
            int c = sqrt(num);
            //if(a + b + c == 1000)
            //if(c > b && b > a && (a + b + c == 1000) && num == c*c)
            if((a + b + c == 1000) && num == c*c)
            {
                num = a * b * c;
                printf("a, b, c => %d,%d,%d.  num=>%d\n",a,b,c,num);
                found = true;
                break;
            }
        }
        if(found) break;
    }
}
