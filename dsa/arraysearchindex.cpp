#include <iostream>
using namespace std;

int main(){
    int d, b, c, e;
    cout << "Enter array size: ";
    cin>> b;
    b=b-1;
    int a[b];
    for (d= 0; d<=b; d++){
        cout<< "Enter Value at "<<d+1<<" :";
        cin>> e;
        a[d]= e;
    }
    cout<<"Array Is: ";
    for(d=0; d<=b;d++){
        cout<<a[d]<<'\n';
    }
    cout<<"Enter value to search: ";
    cin>> c;
    for(d=0; d<=b;d++){
        if (c==a[d]){
            cout<<"The value is found at index:"<<d+1;
        }
    }
}