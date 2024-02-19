/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>

static void solve(const char *texto);

int main(int argc, char const *argv[])
{
    // Test case 1:
    const char *texto = "Hola Mundo. Esto es un programa.";
    solve(texto);
    printf("\n");

    // Test case 2:
    const char *texto_2 = "Hello World. This is a test.";
    solve(texto_2);
    printf("\n");

    // Test case 3:
    const char *texto_3 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.";
    solve(texto_3);
    printf("\n");

    // Test case 4:
    const char *texto_4 = "SingleWord";
    solve(texto_4);
    printf("\n");

    return 0;
}

static void solve(const char *texto)
{
    int max_espacios = 0;
    char palabra[100] = {0};

    int word_length = 0;
    int counter = 0, palabras = 1, longitud_media = 0, letras = 1, oraciones = 0;
    int max_longitud = 0;              
    char palabra_mas_larga[100] = {0}; 

    while (texto[counter] != '\0') // solo un bucle
    {
        if (texto[counter] != ' ' && texto[counter] != '.' && texto[counter] != ',') 
        {
            palabra[word_length++] = texto[counter];
        }
        else
        {
            if (texto[counter] == ' ')
            {
                palabras++;
            }
            if (word_length > max_longitud)
            {
                max_longitud = word_length;
                strncpy(palabra_mas_larga, palabra, word_length);
            }
            word_length = 0; 
        }
        if (isalpha(texto[counter]))
        {
            letras++;
        }
        if (texto[counter] == '.')
        {
            oraciones++;
        }

        counter++;
    }
    longitud_media = letras / palabras; 

    printf("El numero total de palabras son: %d\n", palabras);
    printf("La longitud media de las palabras son: %d\n", longitud_media);
    printf("El numero de oraciones son: %d\n", oraciones);

    palabra_mas_larga[max_longitud] = '\0';
    printf("La palabra mas larga es: %s\n", palabra_mas_larga);
}