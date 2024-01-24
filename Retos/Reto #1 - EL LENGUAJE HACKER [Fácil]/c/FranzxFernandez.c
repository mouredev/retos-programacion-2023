/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

void lenguaje_hacker(char *texto);

int main(int argc, char const *argv[])
{
    char *msg = "HOLA, MUNDO";
    char *msg1 = "LEET";

    lenguaje_hacker(msg);
    printf("\n");

    lenguaje_hacker(msg1);

    return 0;
}

void lenguaje_hacker(char *texto)
{
    const char *alpha[] = {"4", "13", "[", ")", "3", "|=", "&", "#",
                           "1", ",_|", ">|", "1", "/\\/\\", "^/", "0",
                           "|*", "(_,)", "l2", "5", "7", "(_)", "\\/",
                           "\\/\\/", "><", "j", "2"};

    int n = strlen(texto), j = 0;
    ;
    char *array = (char *)malloc((n + 1) * sizeof(char)); // n * 1B

    for (int i = 0; texto[i] != '\0'; i++)
    {
        char ch = tolower(texto[i]);
        if (isalpha(ch)) 
        {
            int position = ch - 'a'; 
            const char *leetChar = alpha[position];
            while (*leetChar)
            {
                array[j++] = *leetChar++;
            }
        }
        else
        {
            array[j++] = ch;
        }
    }

    array[j] = '\0';

    printf("- Mensaje original: %s\n", texto);
    printf("- Mensaje hacker: %s\n", array);

    free(array);
}
