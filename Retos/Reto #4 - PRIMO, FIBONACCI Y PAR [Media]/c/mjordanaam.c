/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool is_prime(int number);
int fibonacci(int number);
bool is_fibonacci(int number);
bool is_fibonacci(int number);
void check_number(int number);

int main(){
    check_number(2);
    check_number(7);
    check_number(8);
    check_number(16);
    check_number(17);
    check_number(0);
    check_number(89);
    check_number(97);
    check_number(100);
    check_number(1);
    check_number(-1);
    
    return 0;
}

bool is_prime(int number){
    if(number > 1){
        for(int i = 2; i < number; i++){
            if (number % i == 0){
                return false;
            }
        }
        return true;
    }
    else {
        return false;
    }
}

int fibonacci(int number){
    if (number == 0){
        return 0;
    }
    else if (number == 1){
        return 1;
    } 
    else{
        return fibonacci(number-1) + fibonacci(number-2);
    }
}

bool is_fibonacci(int number){
    int *sequence;
    sequence = (int *)malloc(16*sizeof(int));
    sequence[0] = fibonacci(0);
    int counter = 0;
    
    while(sequence[counter] < number){
        counter++;
        sequence[counter] = fibonacci(counter);
    }
    
    if(sequence[counter] == number){
        return true;
    }
    free(sequence);

    return false;
}

bool is_even(int number){
    if(number % 2 == 0){
        return true;
    }
    return false;
}

void check_number(int number){
    if(number > -1){
        printf("%d is ", number);

        if(is_prime(number) == false){
            printf("not ");
        }

        printf("prime, ");

        if(is_fibonacci(number) == false){
            printf("is not ");
        }
        printf("fibonacci and is ");

        if(is_even(number)){
            printf("even");
        }
        else{
            printf("odd");
        }
    }
    else{
        printf("Negative number");
    }
    printf("\n");
}

