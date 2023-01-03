/* Solución al "Reto #1 - Lenguaje Hacker" */

#include <stdio.h>
#include <string.h>
#include <ctype.h>

void escribe(char *);
void hackerman(char *, char *);
void imprime(char *);

void main(void)
{
    char texto[1000], *textoCodificado;
    escribe(texto);
    hackerman(texto, textoCodificado);
    imprime(textoCodificado);
}

void escribe(char *text)
{
    printf("\nEscribe el texto de tu preferencia:\n");
    gets(text);
}

void hackerman(char *text, char *textCode)
{
    int i, j;
    char A[36] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'};
    char code[4][36] = {"4", "I3", '[', ')', '3', 'N', '&', '#', '1', 'K', 'i', '1', 'i', 'f', '0', 'd', 'l', 'I', '5', '7', 'l', 'P', 'J', 'S', 'j', '2', 'L', 'R', 'E', 'A', 'S', 'b', 'T', 'B', 'g', 'o'};

    i = 0;
    while (text[i] != '\n')
    {
        for (j = 0; j < 36; j++)
            if (toupper(text[i]) == A[j])
            {
                strcat(textCode, code[j]);
                break;
            }

        i++;
    }
}

void imprime(char *text)
{
    printf("\nEl texto codificado es:\n");
    puts(text);
}
