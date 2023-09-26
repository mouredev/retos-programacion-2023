#include <stdio.h>

int main() {
    // Punto 1: Hola, mundo!
    printf("Hola, mundo!\n");

    // Punto 2: Crea una variable de texto o string
    char miTexto[] = "¡Hola desde C!";

    // Punto 3: Crea una variable de número entero
    int miEntero = 42;

    // Punto 4: Crea una variable de número con decimales
    float miDecimal = 3.14;

    // Punto 5: Crea una variable de tipo booleano (C no tiene tipo booleano, se usa int)
    int miBooleano = 1;  // 1 representa verdadero, 0 representa falso

    // Punto 6: Crea una constante (no es directamente soportado en C)

    // Punto 7: Usa un if, else if y else
    if (miEntero > 50) {
        printf("El número es mayor que 50\n");
    } else if (miEntero < 50) {
        printf("El número es menor que 50\n");
    } else {
        printf("El número es igual a 50\n");
    }

    // Punto 8: Crea un Array
    int miArray[] = {1, 2, 3, 4, 5};

    // Punto 9: Crea una lista (Array en C)
    char *miLista[] = {"Manzana", "Banana", "Naranja"};

    // Punto 10: Crea una tupla (no aplicable en C)

    // Punto 11: Crea un set (no aplicable en C)

    // Punto 12: Crea un diccionario (no es directamente soportado en C)

    // Punto 13: Usa un ciclo for
    for (int i = 0; i < sizeof(miArray) / sizeof(miArray[0]); i++) {
        printf("%d\n", miArray[i]);
    }

    // Punto 14: Usa un ciclo foreach (no es soportado directamente en C)

    // Punto 15: Usa un ciclo while
    int contador = 0;
    while (contador < 3) {
        printf("Contador: %d\n", contador);
        contador++;
    }

    // Punto 16: Crea una función sin parámetros que no retorne nada
    void funcionSinParametros() {
        printf("Función sin parámetros\n");
    }

    // Punto 17: Crea una función con parámetros que no retorne nada
    void funcionConParametros(int param1, char *param2) {
        printf("Parámetro 1: %d\n", param1);
        printf("Parámetro 2: %s\n", param2);
    }

    // Punto 18: Crea una función con parámetros que retorne valor
    int funcionConRetorno(int a, int b) {
        return a + b;
    }

    // Punto 19: Crea una estructura
    struct Persona {
        char nombre[50];
        int edad;
    };

    // Punto 20: Muestra control de excepciones (no es directamente soportado en C)

    return 0;
}
