#include <stdio.h>

int a, b, n, m, d, e;
char st1[];
char st2[];

int main() {
    printf("Enter first string: ");
    scanf("%s", st1);
    printf("Enter second string: ");
    scanf("%s", st2);

    for(a=0; st1[a]!='\0'; a++){
        st1[a];
    }
    for (b=0; st2[b]!='\0'; b++){
        st2[b];
        }
    if (a==b){
        for(n=0; st1[n]!='\0'; n++){
            d= st1[n];
            e= st2[n];
            if (d==e){
                printf("Pass\n");
            }
            else if(d!=e){
                printf("Fail\n");
            }
        }
    }
    return 0;
}
//recieve n number of inputs for an array and find out the average for the given numbers by passing array as an argument to the function average
