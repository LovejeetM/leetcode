#include "bits/stdc++.h" 
using namespace std;

// Function that prints the 
// value of pi upto N 
// decimal places 
void printValueOfPi(int N)
{

	// Find value of pi upto 
	// using acos() function 
	double pi = 2 * acos(0.0);

	// Print value of pi upto 
	// N decimal places 
	printf("%.*lf\n", N, pi);
}
int main()
{
	int N = 5;

	
	printValueOfPi(N);
	return 0;
}

