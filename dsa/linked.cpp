#include <iostream>
#include <string.h>
using namespace std;

int main(){
    struct node{
        int dt;
        node* next;
    };
    int ch = 1;
    int data;

    node* p= nullptr;
    node* t = nullptr;
    node* h = nullptr;

    do {
        node* t = new node();
        cout<< "Enter nodes data: ";
        cin>> data;
        t -> dt = data;
        if (h == nullptr){
            h = t; 
            p = h;
        }else {
            p -> next = t;
            p = t;
        }
        cout<< "do you want to continue, Enter 1 to continue: ";
        cin>> ch;
    }while (ch == 1);
    t = h;
    cout<< t->dt<< "\n";
    do{
        cout<< t->next->dt<< "\n";
        t = t->next;
    }while(t->next != nullptr);

    return 0;
}


// int main(){
//     string name= "hello";
//     string *pname = &name;
//     cout << "Your address of name is: " << &name << ":" << pname;
//     int arr1[5]= {2,5,6,7,7};
//     cout<<'\n'<< arr1[4];
//     cout<<'\n'<<&arr1;

//     return 0;
// }