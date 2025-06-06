#include <iostream>
#include <string>
using namespace std;

int main(){
    int i, n, b, c, d, e, g;
    char aname, f;
    cout << "Enter size of array: ";
    cin >> n;
    int a[n];
    for (int i = 0; i<n; i++) {
        cout << "enter Value: ";
        cin >> a[i];
    }
    for (int i= 0; i< n; i++) {
        cout << " " << a[i]<< ", "; 
    }
    cout<< "Enter value of d: ";
    while (int d =! 7){
        switch(d){
            case 1:
                //insert
                cout<<"Enert where to insert the value in the array(index form 1 to array length): ";
                cin>> c;
                cout<< "value inserted.";
            case 2:
                //delete
                cout<<"Enter index from where you want to delete: ";
                cin >> c;
                for(i= 0; i<=n; i++){
                    if (i==c){
                        for(int i=n; i<=c; i++){
                            a[i]=a[i+1];
                        }
                    }
                }
                cout<<"Element deleated ";
            case 3:
                //create
                cout<<"Enter arry name";
                aname= cin.get();
                cout << "Enter size of array: ";
                cin >> g;
                int aname[g];
                for (int i = 0; i<g; i++) {
                    cout << "enter Value: ";
                    cin >> aname[i];
                }
                for (int i= 0; i< g; i++) {
                    cout << " " << aname[i]<< ", "; 
                }
            case 4:
                //triverse
                for (int i= 0; i< n; i++) {
                    cout << " " << a[n]<< ", "; 
                }
            case 5:
                //search
                cout<<"Enter value to search: ";
                cin>> e;
                for(i=0; i<=n;i++){
                    if (e==a[i]){
                        cout<<"The value is found at index:"<<i+1;
                    }
                }
            case 6:
                //sort
            case 7:
                //exit
                d= 7;
                exit;
            default:
                cout<< "Invalid Input";
        }
    }
    return 0;
}