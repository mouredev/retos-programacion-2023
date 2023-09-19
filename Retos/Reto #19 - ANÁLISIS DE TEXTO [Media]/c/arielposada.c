
// Tested in: https://www.onlinegdb.com/online_c_compiler
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    char texto[] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
    int numPalabras = 0, longitudTotal = 0, numOraciones = 0, longitudPalabra = 0;
    int maxLongitudPalabra = 0;
    char palabraMasLarga[100] = "";
    char *palabra = strtok(texto, " ,");

    while (palabra != NULL) {
        numPalabras++;
        longitudPalabra = strlen(palabra);
        longitudTotal += longitudPalabra;

        if (strchr(palabra, '.') != NULL) {
            numOraciones++;
        }

        if (longitudPalabra > maxLongitudPalabra) {
            maxLongitudPalabra = longitudPalabra;
            strcpy(palabraMasLarga, palabra);
        }

        palabra = strtok(NULL, " ,");
    }

    printf("Número total de palabras: %d\n", numPalabras);
    printf("Longitud media de las palabras: %.2f\n", (float)longitudTotal / numPalabras);
    printf("Número de oraciones: %d\n", numOraciones);
    printf("Palabra más larga: %s\n", palabraMasLarga);

    return 0;
}

