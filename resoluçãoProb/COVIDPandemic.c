#include<stdio.h>
#define MAX 101

int main(){
    int N,T,A[MAX][MAX];
    int i,j,cont,flag,flag2;
    cont = 0;
    flag = 0;
    flag2 = 0;

    scanf("%d",&T);
    for(i = 0 ; i < T ; i ++){
        scanf("%d",&N);
        for(j = 0 ; j < N ; j++){
            scanf("%d",&A[i][j]);
            // printf("Numb: %d\n",A[i][j]);
            if(flag) cont++;
            if(A[i][j] == 1){
                if(!flag){
                    cont = 1;
                    flag = 1;
                }
                else if(flag){
                    if(cont < 6) {
                        cont = 0;
                        flag2 = 1;
                    }
                    else cont = 0;
                }
            }
            // printf("Cont: %d\n",cont);
        }
        
        if(!flag2) printf("YES\n");
        else printf("NO\n");
        cont = 0;
        flag2 = 0;
        flag = 0;
    }

    return 0;
}