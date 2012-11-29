#include <iostream>

using namespace std;

/*
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not exceed four million.
*/

int main(int argv, char * argc[])
{

    long total = 2;
    int length = 10000;
    int results[length];
    int *filler = &results[0];
    *filler++ = 1;
    *filler++ = 2;
    int i = 2;
    for(i; i < length; i++)
    {
      //results[i] = results[i-1] + results[i-2];
      *filler = results[i-1] + results[i-2];
      //if(results[i] >= 4000000) break;
      if(*filler >= 4000000) break;
      //cout << "Results[" << i << "] = " << results[i] << endl;
      //if(results[i] % 2 == 0)
      if(*filler % 2 == 0)
      {
        cout << "Filler=>" << *filler << endl;
        total += *filler;
      }
      *filler++;
    }

    cout << "Total: " << total << endl;
}