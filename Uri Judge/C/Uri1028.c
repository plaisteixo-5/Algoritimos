#include<stdio.h>

int MDC(){

    int aux,aux1;
    int x,y;
    
    scanf("%d %d",&x,&y);
    // printf("%d %d\n",x,y);

    if(x > y){
        aux = x;
        x = y;
        y = aux;
    }

    while(x%y != 0){
        aux = y;
        y = x%y;
        x = aux;
        // printf("Ta aqui\n");
    }

    return y;
}

int main(){

    int n,x,y,i;

    scanf("%d",&n);
    for(i = 0 ; i < n ; i++){
        printf(("%d\n"),MDC());
    }

    return 0;
}