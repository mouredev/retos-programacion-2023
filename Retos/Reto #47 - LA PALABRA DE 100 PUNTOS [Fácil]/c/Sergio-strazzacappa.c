/*
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */
 
/* NOTA:
 * El compilador de un warning con el uso del carácter especial, ñ pero
 * ejecuta sin problemas. Para deshabilitar el warning se puede compilar
 * con el flag -w
 */

#include <stdio.h>
#include <string.h>

#define MAX_LONG_WORD (100)

int word_value(char *word){
    int value = 0;

    for (int i = 0; i < strlen(word); i++) {
        switch (word[i]) {
            case 'a':
            case 'A':
                value += 1;
                break;
            case 'b':
            case 'B':
                value += 2;
                break;
            case 'c':
            case 'C':
                value += 3;
                break;
            case 'd':
            case 'D':
                value += 4;
                break;
            case 'e':
            case 'E':
                value += 5;
                break;
            case 'f':
            case 'F':
                value += 6;
                break;
            case 'g':
            case 'G':
                value += 7;
                break;
            case 'h':
            case 'H':
                value += 8;
                break;
            case 'i':
            case 'I':
                value += 9;
                break;
            case 'j':
            case 'J':
                value += 10;
                break;
            case 'k':
            case 'K':
                value += 11;
                break;
            case 'l':
            case 'L':
                value += 12;
                break;
            case 'm':
            case 'M':
                value += 13;
                break;
            case 'n':
            case 'N':
                value += 14;
                break;
            case (char)'ñ':
            case (char)'Ñ':
                value +=15;
                break;
            case 'o':
            case 'O':
                value += 16;
                break;
            case 'p':
            case 'P':
                value += 17;
                break;
            case 'q':
            case 'Q':
                value += 18;
                break;
            case 'r':
            case 'R':
                value += 19;
                break;
            case 's':
            case 'S':
                value += 20;
                break;
            case 't':
            case 'T':
                value += 21;
                break;
            case 'u':
            case 'U':
                value += 22;
                break;
            case 'v':
            case 'V':
                value += 23;
                break;
            case 'w':
            case 'W':
                value += 24;
                break;
            case 'x':
            case 'X':
                value += 25;
                break;
            case 'y':
            case 'Y':
                value += 26;
                break;
            case 'z':
            case 'Z':
                value += 27;
                break;
        }    
    }
    return value;
}   

void input(char *word) {
    printf("Ingrese una palabra: ");
    scanf("%s", word);
}

int main() {
    int value = 0;

    printf("************************\n");
    printf("LA PALABRA DE 100 PUNTOS\n");
    printf("************************\n");

    do {
        char word[MAX_LONG_WORD];
        input(word);
        value = word_value(word);
        printf("El valor de la palabra %s es: %d\n", word, value);
        } while (value != 100);

    printf("Felicidades!!!\n");

    return 0;
}
