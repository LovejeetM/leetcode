#include <stdio.h>


int main(){
    int x, y, s, s1;
    printf("Enter array size: ");
    scanf("%d", &x);
    printf("Enter array size: ");
    scanf("%d", &y);

    int marks[x][y];

    for(int j=0; j<x; j++){
        for(int h=0; h<y; h++){
        printf("Enter value of %d th term %d in array: ", j, h);
        scanf("%d", &marks[j][h]);
        }
    }
    for(int i=0; i<x; i++){
        for(int k=0; k<y; k++){
    printf(" %d\t", marks[i][k]);
        }
    printf("\n");
    }
    for (int i=0; i<x; i++) {
        s=0;
        for (int k=0; k<y; k++) {
        if(i==k)
        s = s+ marks[i][k];
        if((i+k)==2)
        s1 = s1+ marks[i][k];
        }
    printf("\n");
    }
    printf("sum for row %d = %d", s);
    printf("sum for row %d = %d", s1);

    return 0;
}
//Q:: there are 5 students in a class teacher conducted 3 test in class for them
//and a result has been generated including total marks and average marks
//division is also calculated based on the marks percentage
//bellow 40 fail,  40-59 pass, 60 = 79 first, 80 and above marit
