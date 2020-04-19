#include<stdio.h>
#include<math.h>

int main(){
    int x1,x2,x3,y1,y2,y3;
    int i,n;
    double a,b,c,S,p;

    scanf("%d",&n);

    for(i = 0 ; i < n ; i++){
        scanf("%d %d %d %d %d %d",&x1,&y1,&x2,&y2,&x3,&y3);
        a = sqrt(pow((x1 - x2),2) + pow((y1-y2),2));
        // printf("%.2f\n",a);
        b = sqrt(pow((x2 - x3),2) + pow((y2-y3),2));
        c = sqrt(pow((x1 - x3),2) + pow((y1-y3),2));
        p = (a+b+c)/2;
        S = sqrt(p*(p-a)*(p-b)*(p-c));
        printf("%.3lf\n",S);
    }   

    return 0;
}