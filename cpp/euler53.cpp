#include <iostream>
#include <cstdio>
#include <math.h>

using namespace std;

/*
 * There are exactly ten ways of selecting three from five, 12345:
 *
 * 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
 *
 * In combinatorics, we use the notation, 5C3 = 10.
 *
 * In general,
 *
 * nCr =        * n!
 * r!(nr)!
 * ,where r  n, n! = n(n1)...321, and 0! = 1.
 * It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
 *
 * How many, not necessarily distinct, values of  nCr, for 1  n  100, are greater than one-million?
*/
long long Fact (long long n) 
{ 
    long long r = 1; 
    for (int i=2; i<=n; i++) 
        r *= i; 
    return r; 
} 


int main()
{
//a^2 + b^2 = c^2
    int count = 0;

    for(int n = 2; n < 100; n++)
    {
        //for b in xrange(1, 1000):
        for(int r = 1; r < n; r++)
        {
            cout << "n,r = " << n << "," << r << endl;
            long long fn = Fact(n);
            long long fr = Fact(r);
            long long fnr = Fact(n-r);
            long long z = fn / (fr * fnr);
            if(z > 1000000)
                count += 1;
        }
    }
    cout << "Count => " << count << endl;
}
