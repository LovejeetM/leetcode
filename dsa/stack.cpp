#include <iostream>
#include <string.h>
using namespace std;

// Global Variables ----------------------------------------------------------------------
struct node{
    string dt;
    node* next;
};

node* temp = nullptr;
node* last= nullptr;
node* p= nullptr;
node* top= nullptr;

int max = 9;
int count = -1;
// Global Variables ----------------------------------------------------------------------

// Functions of stack --------------------------------------------------------------------
void push(){
    string n;
    cout<<"Enter the element to add to the stack: ";
    cin >> n;
    node* temp = new node();
    temp ->dt = n;
    if (count != 9){
        if (last == nullptr){
            last = temp;
            top = temp;
            p= temp;
            count++;
        } else {
            temp->next =p;
            p= temp;
            top= temp;
            count++;
        }
    } else {
        cout<< "Stack is full\n";
    }
};

string pop(){
    temp = top-> next;
    string a= top-> dt;
    top= temp;
    count--;
    free(temp);
    return a;
};

string top1(){
    return top->dt;
};
// Functions of stack --------------------------------------------------------------------


int main(){
    push();
    push();
    push();
    cout<< "Top of the stack is: "<< top1()<< "\n";
    cout<<"Poped element: "<< pop()<<"\n";
    cout<< "Top of the stack is: "<< top1()<< "\n";
}