#include <iostream>
using namespace std;

// struct name (
//     int v;
//     name 
// )
int i;

int main() {
    int n;
    cout << "Enter size of array: ";
    cin >> n;
    int a[n];
    for (i = 0; i<n; i++) {
        cout << "enter Value: ";
        cin >> a[i];
    }
    for (i= 0; i< n; i++) {
        cout << "\n" << a[i]; 
    }
    return 0;
}