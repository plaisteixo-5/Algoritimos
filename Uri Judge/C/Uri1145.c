#include<stdio.h>

int main(){
    int x,y;
    int i,j;
    int n;
    n = 1;
    
    scanf("%d %d",&x,&y);

    for(i = 0 ; n < y ; i++){
        for(j = 0 ; j < x ; j++){
            if(n <= y){
                if(j == x-1) printf("%d\n",n);
                else printf("%d ",n);
            }
            else{
                printf("\n");
            }
            n++;
        }
    }

    return 0;
}