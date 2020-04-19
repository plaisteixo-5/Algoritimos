#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

_Bool valida(int *x, int *y, int posi, int n){

    int i,flag1,flag2,flag3,flag4;
    flag1 = 0; flag2 = 0; flag3 = 0; flag4 = 0;

    for(i = 0 ; i < n ; i++){
        if(i != posi){
            if(x[i] == x[posi] && y[i] > y[posi]) flag1 = 1;
            else if(x[i] == x[posi] && y[i] < y[posi]) flag2 = 1;
            else if(x[i] > x[posi] && y[i] == y[posi]) flag3 = 1;
            else if(x[i] < x[posi] && y[i] == y[posi]) flag4 = 1;
        }
    }
    if(flag1 && flag2 && flag3 && flag4) return true;
    else return false;
    
}

int main(){

    int i,n,total;
    total = 0;

    scanf("%d",&n);

    int* x = (int*) malloc(sizeof(int)*n);
    int*y = (int*) malloc(sizeof(int)*n);

    for(i = 0 ; i < n ; i++) scanf("%d %d",&x[i],&y[i]);
    for(i = 0 ; i < n ; i++){
        if(valida(x,y,i,n)) total++;
    }
    printf("%d\n",total);

    free(x);
    free(y);

    return 0;
}