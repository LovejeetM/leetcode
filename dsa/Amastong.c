#include <stdio.h>

int main() {
    int a, j, k=0, i;
    int n[50];
    char c;

    printf("Enter number length: ");
    scanf("%d", &a);
    for (i=0; i<=a; i++){
        printf("Enter nth value of the full number: ");
        scanf("%d", &n[i]);
    }
    fflush(stdin);
    printf("Do you want to check this number? Y/n: ");
    scanf("%c", &c);
    if (c=='y' || c=='Y'){
        for (i=0; i<=a; i++){
            j=n[a];
            k= (j*j*j)+k;
        }
        if (k==n){
            printf("It is armstrong number");
        }
    }
    return 0;
}
// receive roll number ,name, and marks in two different subjects, for n number of students, find out the result of a student
//based on the heighest marks scored in given two ca marks. all data need to be stored in the structure and print it in tabular format.
