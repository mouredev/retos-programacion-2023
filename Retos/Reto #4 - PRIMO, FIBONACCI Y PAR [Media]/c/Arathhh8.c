/* # Reto #4: PRIMO, FIBONACCI Y PAR
#### Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23

## Enunciado

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
*/

#include<stdio.h>
#include<stdint.h>
#include <stdbool.h>

bool checkInputNum(int* num);
bool isPrime(int num);
bool isFibonacci(int num);
bool isPair(int num);
void clearInputBuffer(); 


int main(void){

    int num;

    while (!checkInputNum(&num)); // esperar hasta que el usuario ingrese un numero válido
    

    if(isPrime(num)){
        printf("%d es primo, ", num);
    }else{
        printf("%d no es primo, ", num);
    }

    if(isFibonacci(num)){
        printf("fibonacci ", num);
    }else{
        printf("no es fibonacci ", num);
    }

    if(isPair(num)){
        printf("y es par\n", num);
    }else{
        printf("y es impar\n", num);
    }

    return 0;
}


bool checkInputNum(int* num){
    int result;

    while (true) {
        printf("Ingrese un numero entero: ");
        result = scanf("%d", num);

        if (result == 1) {
            // Entrada válida
            break;
        } else {
            // Entrada no válida, limpiar el búfer de entrada
            clearInputBuffer();
            printf("Entrada no valida. Por favor, ingrese un numero entero.\n");
        }
    }

    return true;
}

// Función para verificar si un número es primo
bool isPrime(int num) {
    // Los números menores o iguales a 1 no son primos
    if (num <= 1) {
        return false;
    }

    // Verificar si el número tiene divisores distintos de 1 y de sí mismo
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }

    return true;
}

// Funcion para verificar si un numero es fibonacci
bool isFibonacci(int num){

    int current_1 = 1; // guarda el numero anterior
    int current_2 = 0;
    int current = 0;

    if(num == 0 || num == 1 ){
        return true;
    }    

    //printf("Serie fibonacci: %d, %d,", current_2, current_1);

    for(int i = 1; i <= num; i++){
        current = current_1 + current_2;
        current_2 = current_1;
        current_1 = current;
        //printf("%d, ", current);
        if(num == current){
            return true;
        }
    }

    return false;
}

// Funcion para verificar si un numero es par
bool isPair(int num){

    if(num % 2 == 0){
        return true;
    }

    return false;
}

// Función para limpiar el búfer de entrada
void clearInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}