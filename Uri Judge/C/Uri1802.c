#include<stdio.h>
#define MAX 1000


void merge(int arr[], int l, int m, int r){ 
    int i, j, k; 
    int n1 = m - l + 1; 
    int n2 =  r - m; 

    int L[n1], R[n2]; 
  
    for (i = 0; i < n1; i++) 
        L[i] = arr[l + i]; 
    for (j = 0; j < n2; j++) 
        R[j] = arr[m + 1+ j]; 
  
    
    i = 0;
    j = 0; 
    k = l; 
    while (i < n1 && j < n2) 
    { 
        if (L[i] >= R[j]) 
        { 
            arr[k] = L[i]; 
            i++; 
        } 
        else
        { 
            arr[k] = R[j]; 
            j++; 
        } 
        k++; 
    } 
  
    
    while (i < n1) 
    { 
        arr[k] = L[i]; 
        i++; 
        k++; 
    } 
  
    
    while (j < n2) 
    { 
        arr[k] = R[j]; 
        j++; 
        k++; 
    } 
} 
  

void mergeSort(int arr[], int l, int r) { 
    if (l < r){ 
        int m = l+(r-l)/2; 

        mergeSort(arr, l, m); 
        mergeSort(arr, m+1, r); 
  
        merge(arr, l, m, r); 
    } 
} 

void printaPaNois(int valores[][MAX], int q){
    int i,j;
    for(i = 0 ; i < 5 ; i++) {
        for(j = 0 ; j < q ; j++) printf("%d ",valores[i][j]);
        printf("\n");
    }
}

int main(){
    int i,j,k,l,m,q,K,cont,total;
    int valores[MAX][MAX];
    int soma[100000];
    cont = 0;
    total = 0;

    for(i = 0 ; i < 5 ; i++) {
        scanf("%d",&q);
        for(j = 0 ; j < q ; j++) scanf("%d",&valores[i][j]);
    }

    for(i = 0 ; i < q ; i++){
        for(j = 0 ; j < q ; j++){
            for(k = 0 ; k < q ; k++){
                for(l = 0 ; l < q ; l++){
                    for(m = 0 ; m < q ; m++){
                        soma[cont] = valores[0][i]+valores[1][j]+valores[2][k]+valores[3][l]+valores[4][m];
                        cont += 1;
                    }
                }
            }
        }
    }
    mergeSort(soma,0,cont);

    scanf("%d",&K);

    for(i = 0 ; i < K ; i++) total += soma[i];
    printf("%d\n",total);

    return 0;
}