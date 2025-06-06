#include <iostream>
using namespace std;

int i;

int main() {
    int n;
    int b;
    int ind;
    cout<< "Enter array size: ";
    cin >> n;
    int a[n];
    for (i = 0; i<n; i++) {
        cout << "enter Value: ";
        cin >> a[i];
    }
    cout<< "Enter the value to insert and where to insert: ";
    cin >> b;
    cout<< "where to insert index: ";
    cin >> ind;
    a[n+1];
    for (i=n; i>ind; i--) {
        a[i+1]= a[i];        
    }
    a[ind]= b;
    for (i= 0; i< n+1; i++) {
        cout << "\n" << a[i]; 
    }
    return 0;
}