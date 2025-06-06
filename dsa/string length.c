#include <stdio.h>

int i, n,p;
char a[];
int main(){
    printf("Enter your Array: ");
    scanf("%s", a);

    for (i=0; a[i]!='\0'; i++){
        a[i];
    }
    printf("String Length= %d \n", i);
    for (n=i; n>=0; n--){
        printf("%c", a[n]);
    }

    return 0;
}
//write a program to reverse a string without using any string function

//write a program to compare two strings without using string function
