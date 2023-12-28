/*
 * # Reto #1: EL "LENGUAJE HACKER"
 * #### Dificultad: Fácil | Publicación: 02/01/23 | Corrección: 09/01/23
 *
 * ## Enunciado
 *
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 *
 * Author: kyrex23
 * Date:   22/01/2023
 *
 * Usage (without arguments -> it will ask you for the input): ./kyrex23
 * Usage (with arguments -> first argument will be the input): ./kyrex23 <your_string>
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define BUFFER_SIZE 256

const char *KEYS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const char *VALUES[] = {
    "4", "I3", "[", ")", "3", "|=", "&", "#", "1", ",_|",
    ">|", "1", "/\\/\\", "^/", "0", "|*", "(_,)", "I2", "5", "7",
    "(_)", "\\/", "\\/\\/", "><", "j", "2"
};

void read_input(char*, int);
void leet_encode(char*, char*);

// ---------------------------------------------------------------------------------------------------------------------

int main(int argc, char *argv[]) {
    char original_input[BUFFER_SIZE] = {0};
    char encoded_input[BUFFER_SIZE * 4] = {0}; // ensuring enough capacity (longest encoded values need 4 characters)

    if(argc < 2) { // ask input if it is not passed as argument
        printf("Enter a string to encode: ");
        read_input(original_input, BUFFER_SIZE);
    } else strncpy(original_input, argv[1], BUFFER_SIZE);

    leet_encode(original_input, encoded_input);

    printf("Original input: %s\n", original_input);
    printf("Encoded input : %s\n", encoded_input);
}

// ---------------------------------------------------------------------------------------------------------------------

void read_input(char* buffer, int capacity) {
    fgets(buffer, capacity, stdin);

    if(buffer[strlen(buffer) - 1] == '\n') // if the size of input is less than the capacity
        buffer[strlen(buffer) - 1] = '\0'; // remove the final enter character from the string
    else while(getchar() != '\n');         // if not, there is still garbage in the stdin buffer, clean it up
}

void leet_encode(char* input, char* output) {
    char *p_char = input;

    while(*p_char != '\0') {
        char upper_char = toupper(*p_char);
        int char_index = -1;

        for(int i = 0; i < strlen(KEYS) && char_index == -1; ++i)
            if(KEYS[i] == upper_char) char_index = i;

        if(char_index > -1) strcat(output, VALUES[char_index]);
        else strncat(output, p_char, 1);

        ++p_char;
    }
}
