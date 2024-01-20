/*
# Reto #0: EL FAMOSO "FIZZ BUZZ"
#### Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23

## Enunciado
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */


#include<stdio.h>
#include<string.h>

void fizz_buzz();

int main(){

    fizz_buzz();
    return 0;
}


void fizz_buzz(){

    for(int i = 0; i < 100; i++){
        if(i % 3 == 0 && i % 5 == 0){
            printf("fizzbuzz\n");
        }else if(i % 5 == 0){
            printf("buzz\n");
        }else if(i % 3 == 0){
            printf("fizz\n");
        }else{
            printf("%d\n",i);
        }
    }
}
