#include <iostream>
using namespace std;


// Doubly Circular Linked List
int main(){

struct node{
    node* prev;
    int dt;
    node* next;
};

node* temp= nullptr;
node* start= nullptr;
node* p= nullptr;

int data;
int ch= 1;
int count = 1;

do{
    node* temp = new node();
    cout << "Enter the data: ";
    cin >> data;
    temp -> dt= data;
    if (start == nullptr){
        start = temp;
        p= temp;
    } else {
        p -> next = temp;
        temp -> prev= p;
        p= temp;
        start -> prev = temp;
    }
    cout<< "Enter 1 to continue: ";
    cin >> ch;
}while(ch == 1);
start -> prev ->next = start;

temp= start;
do{
    cout << "At "<< count << ": "<< temp->dt << "\n";
    temp= temp-> next;
    count++;
}while(temp != start);

return 0;
}