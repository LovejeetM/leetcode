#include <stdio.h>


int main(){
    int total, s1;
    int marks[5][3];

    for(int j=0; j<5; j++){
        for(int h=0; h<3; h++){
        printf("Enter value of %d th term %d in array: ", j, h);
        scanf("%d", &marks[j][h]);
        }
    }
    for (int i=0; i<5; i++) {
        total=0;
        printf("Marks: ");
        for (int k=0; k<3; k++) {
                printf(" %d\t", marks[i][k]);
                total= total+marks[i][k];
        }
    s1= (total*100)/300;
    printf("Total: %d", total);
    printf("\tAverage: %d", s1);
    if(s1<=40){
        printf("\tFail");
    }
    else if(s1>40 && s1<=60){
        printf("\tPass");
    }
    else if(s1>60 && s1<=80){
        printf("\tFirst");
    }
    else if(s1>80 && s1<=100){
        printf("\tMerit");
    }
    printf("\n");
    }

    return 0;
}
//Q:: there are 5 students in a class teacher conducted 3 test in class for them
//and a result has been generated including total marks and average marks
//division is also calculated based on the marks percentage
//bellow 40 fail,  40-59 pass, 60 = 79 first, 80 and above marit
