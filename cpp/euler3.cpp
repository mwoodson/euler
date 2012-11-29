#include <iostream>
#include <math.h>

using namespace std;

/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

bool is_prime(long long n)
{
    for(int i = 2; i <= int(sqrt(n)); i++)
    {
        if(n % i == 0)
          return false;
    }
    return true;
}


int main(int argv, char * argc[])
{
    long long num = 600851475143LL;

    
    long long i = 2LL;
    while(i < num)
    {
      //cout << i << endl;
//cout << "sqrt=>" << sqrt(i) << endl;
      if(num % i == 0)
      {
          long long z = num / i;
          if(is_prime(z))
          {
            cout << z << " is prime." << endl;
            break;
          }
      }
      i+=1;
    }

/*
    def isprime(n):
        for x in range(2, int(n**0.5)+1):
            if n % x == 0:
                return False
        return True

    big_num = 600851475143

    x = 1
    while (x < big_num):
        if big_num % x == 0:
            num =(big_num / x)
            if (isprime(num)):
                print num
                break
        x+=2
*/
} 
