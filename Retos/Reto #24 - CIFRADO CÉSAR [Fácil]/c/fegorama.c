/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Constantes y macros
#define MAX_LENGTH 50
#define MAX_ALPHABET 26
#define OFFSET 3
#define POSMOD(i, n) (i % n + n) % n // https://stackoverflow.com/a/14997413/5032550

const char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

/*
 * Función para cifrado y descifrado del código César
 */
int cease(char *s, int decrypt)
{
    char c;

    // Para cada carácter de la cadena pasada...
    for (int i = 0; i < strlen(s); i++)

        // Si está fuera del alfabeto de mayúsculas, error
        if (s[i] < 65 || s[i] > 90)
        {
            fprintf(stderr, "Error: Solo letras de la A a la Z.");
            exit(1);
        }

        // Si está dentro...
        else
        {
            // Se resta su código ASCII para comenzar por cero el índice del alfabeto
            c = s[i] - 65;

            // Se calcula como carácter + número de posiciones a sumar o restar, si es codificar o decodificar, 
            // y se realiza su módulo positivo (aritmética circular) para poder rotar entre el alfabeto 
            // (si es Z y se codifica como Z + 2 posiciones, el resultado será B)
            s[i] = decrypt == 0 ? alphabet[POSMOD(c + OFFSET, MAX_ALPHABET)] : alphabet[POSMOD(c - OFFSET, MAX_ALPHABET)];
        }

    return 0;
}

/*
 * Función principal
 */
int main(int argc, char **argv)
{
    char s[MAX_LENGTH];
    int decrypt = 0;
    // Si contiene un argumento y este es "-d", desencripta
    if (argc > 1 && strcmp(argv[1], "-d") == 0)
        decrypt = 1;

    // Se recoge la entrada estándar
    fgets(s, MAX_LENGTH, stdin);

    // Si la longitud es mayor que cero, se sustituye el retorno de carro final
    // por el carácter de fin de línea (\0)
    if ((strlen(s) > 0) && (s[strlen(s) - 1] == '\n'))
        s[strlen(s) - 1] = '\0';

    // Llamada a la función e impresión del mensaje
    cease(s, decrypt);
    printf("%s", s);

    exit(0);
}