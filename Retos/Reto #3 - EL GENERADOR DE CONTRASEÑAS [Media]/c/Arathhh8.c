/* # Reto #3: EL GENERADOR DE CONTRASEÑAS
#### Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23

## Enunciado

 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define MAX_LEGTH                       16
#define MIN_LEGTH                       8
#define LETTERS_NUMBERS_DIGITES         0
#define LETTERS_NUMBERS_NODIGITES       1
#define LETTERS_NONUMBERS_DIGITES       2
#define LETTERS_NONUMBERS_NODIGITES     3
#define NOLETTERS_NUMBERS_DIGITES       4
#define NOLETTERS_NUMBERS_NODIGITES     5
#define NOLETTERS_NONUMBERS_DIGITES     6
#define NOLETTERS_NONUMBERS_NODIGITES   7

#define GENERATE_LOWER                  0
#define GENERATE_UPPER                  1
#define GENERATE_NUMBER                 2
#define GENERATE_DIGITE                 3

// Función para generar una letra minúscula aleatoria
char generateRandomLowercaseLetter() {
    return 'a' + (rand() % 26);
}

char generateRandomUppercaseLetter() {
    return 'A' + (rand() % 26);
}

char generateRandomNumbers() {
    return '0' + (rand() % 10);
}

char generateRandomDigites() {
    return '!' + (rand() % 11);
}

void passwordSettings(int* withLetters, int* withNumbers, int* withDigits, int* user_config);
void passwordGenerator(char* password, int config);
void printPassword(char* password, int length);

void clearInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}


int main() {
    // Inicializar el generador de números aleatorios con una semilla basada en el tiempo
    srand(time(NULL));
    int passwordLength = 0;
    int withLetters, withNumbers, withDigits, user_config;

    printf("Que tamano deseas que tenga tu contrasena (elige un numero entre 8 y 16): ");
    scanf("%d", &passwordLength);
    while (passwordLength < MIN_LEGTH || passwordLength > MAX_LEGTH)
    {
        printf("Valor invalido. Elige un numero entre 8 y 16: ");
        scanf("%d", &passwordLength);
    }
    
    char *password = (char*)malloc(passwordLength * sizeof(char));

    passwordSettings(&withLetters,&withNumbers, &withDigits, &user_config);

    passwordGenerator(password, user_config);

    printf("Contrasena generada: ");

    printPassword(password, passwordLength);

    free(password);

    return 0;
}


void passwordSettings(int* withLetters, int* withNumbers, int* withDigits, int* user_config){

    *user_config = 0;

    printf("Deseas que tu contrasena contenga letras?\n");
    printf("0. Si\n1. No\nUser selection: ");
    while (scanf("%d", withLetters) != 1 || *withLetters < 0 || *withLetters > 1) {
        clearInputBuffer(); // Limpia el búfer de entrada
        printf("Entrada no valida. Digita 0 para Si y 1 para NO: ");
    }

    printf("Deseas que tu contrasena contenga numeros?\n");
    printf("0. Si\n1. No\nUser selection: ");
    while (scanf("%d", withNumbers) != 1 || *withNumbers < 0 || *withNumbers > 1) {
        clearInputBuffer(); // Limpia el búfer de entrada
        printf("Entrada no valida. Digita 0 para Si y 1 para NO: ");
    }

    printf("Deseas que tu contrasena contenga digitos?\n");
    printf("0. Si\n1. No\nUser selection: ");
    while (scanf("%d", withDigits) != 1 || *withDigits < 0 || *withDigits > 1) {
        clearInputBuffer(); // Limpia el búfer de entrada
        printf("Entrada no valida. Digita 0 para Si y 1 para NO: ");
    }

    *user_config |= (*withLetters << 2);
    *user_config |= (*withNumbers << 1);
    *user_config |= (*withDigits << 0);
    
}

void passwordGenerator(char* password, int config){

    int operation = (rand() % 4);
    for(int i = 0; i < 16; i++){
        operation = (rand() % 4);
        while(config == LETTERS_NUMBERS_NODIGITES && operation == GENERATE_DIGITE){
            operation = (rand() % 4);
        }
        while(config == LETTERS_NONUMBERS_DIGITES && operation == GENERATE_NUMBER){
            operation = (rand() % 4);
        }
        while(config == LETTERS_NONUMBERS_NODIGITES && (operation == GENERATE_DIGITE || operation == GENERATE_NUMBER)){
            operation = (rand() % 4);
        }
        while(config == NOLETTERS_NUMBERS_DIGITES && (operation == GENERATE_LOWER || operation == GENERATE_UPPER)){
            operation = (rand() % 4);
        }
        while(config == NOLETTERS_NUMBERS_NODIGITES && operation != GENERATE_NUMBER){
            operation = (rand() % 4);
        }
        while(config == NOLETTERS_NONUMBERS_DIGITES && operation != GENERATE_DIGITE){
            operation = (rand() % 4);
        }
        while(config == NOLETTERS_NONUMBERS_NODIGITES && operation != GENERATE_LOWER){
            operation = (rand() % 4);
        }
        
        switch (operation)
        {
        case GENERATE_LOWER:
            password[i] = generateRandomLowercaseLetter();
            break;
        case GENERATE_UPPER:
            password[i] = generateRandomUppercaseLetter();
            break;
        case GENERATE_NUMBER:
            password[i] = generateRandomNumbers();
            break;
        case GENERATE_DIGITE:
            password[i] = generateRandomDigites();
            break;
        default:
            break;
        }
    }
}

void printPassword(char* password, int length){
    for(int i = 0; i < length; i++){
        printf("%c", password[i]);
    }
}