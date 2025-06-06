#include <iostream>
using namespace std;

int i;

int main() {
    int a[10];
    for (i = 0; i<9; i++) {
        cout << "enter Value: ";
        cin >> a[i];
        cout << "\n  Entered " << a[i] << "\n";
    }
    cout << "the value of " << 7 << " is " << a[8] << "\n";
    return 0;
}


