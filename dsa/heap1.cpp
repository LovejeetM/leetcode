#include <iostream>
using namespace std;

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapify(int arr[], int i, int n){
    int smallest = i;
    int right= 2 * i + 2;
    int left = 2 * i + 1;

    if (left < n && arr[left] < arr[smallest]){
        smallest = left;
    }
    if (right < n && arr[right] < arr[smallest]){
        smallest = right;

    }

    if (smallest != i) {
        swap(&arr[i], &arr[smallest]);
        heapify(arr, n, smallest);
    }
}

void minheap(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
}


int main(){
    int h1[]= {10,20,5,7,18};
    int h2[]= {50,25,3,4,11};
    int n = sizeof(h1)/ sizeof(h1[0]);
    int n2 = sizeof(h2)/ sizeof(h2[0]);

    minheap(h1, n);

    cout << "MinHeap array: ";
    for (int i = 0; i < n; ++i) {
        cout << h1[i]<< " , ";
    };

    int h3[20];

    for (int i = 0; i < n; ++i) {
        h3[i] = h1[i];

        for(int j = n; j< n+n2; j++){
            h3[j] = h2[j];
        }
    };

    int k = n + n2;
    minheap(h3, k);


    cout << "MinHeap array merged: ";
    for (int i = 0; i < k; ++i) {
        cout << h3[i]<< " , ";
    };

    return 0;
}