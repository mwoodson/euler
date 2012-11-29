#include <iostream>

using namespace std;

//If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
//Find the sum of all the multiples of 3 or 5 below 1000.
int main(int argv, char * argc[])
{

    int numsum = 0;
    for (int i = 0; i < 1000; i++)
        if ((i % 3 == 0) || (i % 5 == 0)) numsum += i;


    cout << "Sum of all multiples 3 or 5 is " << numsum << endl;
}
