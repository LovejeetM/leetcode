#include <stdio.h>


int main(){
    int x, y, s;
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
        s = s+ marks[i][k];
        }
    printf("sum for row %d = %d", i+1, s);
    printf("\n");
    }

    return 0;
}
