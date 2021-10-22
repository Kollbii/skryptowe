#include <stdio.h>
#include <stdlib.h>

/*
Linia 1
Linia 2
Linia 3
*/
int suma (int x, int y){
    return x+y;
}

/*
Some more comments
In more lines
*/

void printArr (int **arr, int n){
    for (int i= 0; i < n; i++){
        for (int j = 0; j < n; j++){
            j + 1 == n ? printf("%d\n", arr[i][j]) : printf("%d ", arr[i][j]);
        }
    }
}

int sumOnBorder (int **arr, int n, int i, int j, int radius){
    int sum_on_border = 0;
    int left_limit, right_limit, up_limit, down_limit;

    /*
    Set border
    */
    left_limit = j - radius;
    right_limit = j + radius;
    up_limit = i - radius;
    down_limit = i + radius;

    for (int i = left_limit; i < right_limit; i++){
        sum_on_border += arr[up_limit][i];
    }

    for (int i = up_limit; i < down_limit; i++){
        sum_on_border += arr[i][right_limit];
    }

    for (int i = right_limit; i > left_limit; i--){
        sum_on_border += arr[down_limit][i];
    }

    for (int i = down_limit; i > up_limit; i--){
        sum_on_border += arr[i][left_limit];
    }

    return sum_on_border;
}


int main (void){
    int n, sum_to_find, counter = 0;
    int answer[128][2] = {};

    printf("Insert n and sum\n>");
    scanf("%d %d",&n, &sum_to_find);

    /*
    Some comments inside
    old c program
    */

    int **arr = (int**)malloc(sizeof(int*)*(unsigned)n);
    for (int i = 0; i < n; i++){
        arr[i] = (int*)malloc(sizeof(int)*(unsigned)n);
        for(int j = 0; j < n; j++){
            scanf("%d", &arr[i][j]);
        }
    }
}