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
    cout << "Enter number to delete: ";
    cin >> c;
    for(d= 0; d<=b; d++){
        if (a[d]==c){
            for(int i=d; i<=b; i++){
                a[i]=a[i+1];
            }
        }
    }
    cout<<"Array after deletion: "<<'\n';
    for(d=0; d<=b;d++){
        cout<<a[d];
    }
    return 0;
}