#include <stdio.h>

void fizzbuzz(int a, int b ){
    int c = a*b;
    for (int i = 1; i <101; i++){
        if (i % c == 0) printf("fizzbuzz\n");
        else if (i % a  == 0) printf("fizz\n");
        else if (i % b == 0) printf("buzz\n");
        else printf("%i\n",i);
    }
}

int main(void){
    fizzbuzz(3,5);
    return 0;
}