#include <stdio.h>

struct student{
    int rollno;
    int age;
    char gen;
    char name[20];
};

int main(){
    struct student std[5];
    int i, j;
    printf("Data for 5 students\n");
    for(i=0; i<=4; i++){
        j=i+1;
        printf("Input Roll no of std %d: ", j);
        scanf("%d", &std[i].rollno);
        printf("Input Age no of std %d: ", j);
        scanf("%d", &std[i].age);
        fflush(stdin);
        printf("Input Gender no of std %d: ", j);
        scanf("%c", &std[i].gen);
        printf("Input Name no of std %d: ", j);
        scanf("%s", std[i].name);
        fflush(stdin);
    }
    printf("RollNo\tAge\tGen\tName\n");
    for (i=0; i<=4; i++){
        printf("%d\t%d\t%c\t%s\n", std[i].rollno, std[i].age, std[i].gen, std[i].name);
    }
    return 0;
}
// array 1d, 2d, string, string functions and handling, functions user defined, structures, pointers.
