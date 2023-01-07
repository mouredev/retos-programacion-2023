/* Solución al "Reto #1 - Lenguaje Hacker" */

#include <stdio.h>
#include <string.h>
#include <ctype.h>

void escribe(char *);
void hackerman(char *, char *);
void imprime(char *);

void main(void)
{
    char texto[250], textoCodificado[250] = "";
    escribe(texto);
    hackerman(texto, textoCodificado);
    imprime(textoCodificado);
}

// Función que ingresa el texto ha codificar
void escribe(char *text)
{
    printf("\nEscribe el texto de tu preferencia:\n");
    gets(text);
}

// Función que codifica el texto ingresado
void hackerman(char *text, char *textCode)
{
    int i, j;
    char A[37] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' '};
    char code[37][5] = {"4", "|3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "/\\/\\", "^/", "0", "|*", "(_,)", "|2", "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2", "L", "R", "E", "A", "S", "b", "T", "B", "g", "o", " "};

    i = 0;
    while (text[i] != '\0')
    {
        for (j = 0; j < 37; j++)
            if (toupper(text[i]) == A[j])           // Busqueda que los índices de cada caracter
            {
                strcat(textCode, code[j]);          // concatena cada nuevo caracter a la variable del textoCodificado
                break;
            }

         i++;
    }
}

// Función que muestra en pantalla el texto codificado
void imprime(char *text)
{
    printf("\nEl texto codificado es:\n");
    puts(text);
}