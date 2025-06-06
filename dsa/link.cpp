#include <iostream>
#include <string.h>
using namespace std;

int main(){
    struct node{
        int dt;
        node* next;
    };

    node* temp = nullptr;
    node* head= nullptr;
    node* prev= nullptr;

    int ch;
    int data;

    do{
        cout<< "Enter node data: ";
        cin >> data;
        node* temp= new node();
        temp->dt = data;
        if (head == nullptr){
            head = temp;
            prev= temp;
        }else{
            prev->next= temp;
            prev = temp;
        }
        cout<<"enter choice: ";
        cin>>ch;
    }while(ch==1);
    
    temp = head;
    cout<< temp->dt <<"\n";
    do{
        cout<< temp->next->dt << "\n";
        temp= temp->next;
    }while(temp->next != nullptr);
    return 0;
}
