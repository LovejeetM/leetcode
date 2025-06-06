#include <iostream>
using namespace std;

int n, c, d;

int add(int a, int b){
    return (a+b);
}
int sub(int a, int b){
    return (a-b);
}
int mult(int a, int b){
    return (a*b);
}
int divi(int a, int b){
    return (a/b);
}

int main(){
    cout<< "Enter your number: ";
    cin >> n;
    cout<< "Enter number 2: ";
    cin>> c;
    d = add(n, c);
    cout<<"Sum is: "<<d;  
    return 0;
}