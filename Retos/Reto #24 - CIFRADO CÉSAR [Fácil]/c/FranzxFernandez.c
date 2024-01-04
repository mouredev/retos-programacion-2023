/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

static char *cifrado(char *texto, int desplazamientos);
static char *descifrado(char *texto_cifrado, int desplazamientos);

int main()
{
    char *texto = "Hola";
    char *texto1 = "ABCDEF";
    char *texto2 = "Hola, soy leon ";

    int desplazamientos = 2, desplazamientos1 = 5, desplazamientos2 = 3;

    char *msg_cifrado = cifrado(texto, desplazamientos);
    char *msg_descifrado = descifrado(msg_cifrado, desplazamientos);

    char *msg_cifrado1 = cifrado(texto1, desplazamientos1);
    char *msg_descifrado1 = descifrado(msg_cifrado1, desplazamientos1);

    char *msg_cifrado2 = cifrado(texto2, desplazamientos2);
    char *msg_descifrado2 = descifrado(msg_cifrado2, desplazamientos2);

    

    printf("- Mensaje original: %s\n", texto);
    printf("- Mensaje cifrado: %s\n", msg_cifrado);
    printf("- Mensaje descifrado: %s\n",msg_descifrado);
    printf("\n");

    printf("- Mensaje original: %s\n", texto1);
    printf("- Mensaje cifrado: %s\n", msg_cifrado1);
    printf("- Mensaje descifrado: %s\n",msg_descifrado1);
    printf("\n");

    printf("- Mensaje original: %s\n", texto2);
    printf("- Mensaje cifrado: %s\n", msg_cifrado2);
    printf("- Mensaje descifrado: %s\n",msg_descifrado2);

    free(msg_cifrado);
    free(msg_descifrado);
    free(msg_cifrado1);
    free(msg_descifrado1);
    free(msg_cifrado2);
    free(msg_descifrado2);

    return 0;
}

static char *cifrado(char *texto, int desplazamientos) 
{
    char alphabet[] = "abcdefghijklmnopqrstuvwxyz";
    int n = strlen(texto), j = 0;

    char *cifrado = (char *)malloc((n + 1) * sizeof(char)); // n * 1B

    for (int i = 0; texto[i] != '\0'; i++)
    {
        char ch = tolower(texto[i]);
        if (ch >= 'a' && ch <= 'z')
        {
            int position = (ch - 'a');                      // 104(h) - 97(a) = 7
            int result = (position + desplazamientos) % 26; // 10
            cifrado[j++] = alphabet[result];
        }
        else
        {
            cifrado[j++] = ch; // Para comas, espacios, puntos etc.
        }
    }
    cifrado[j] = '\0';

    return cifrado;
}
static char *descifrado(char *texto_cifrado, int desplazamientos)
{
    char alphabet[] = "abcdefghijklmnopqrstuvwxyz";
    int n = strlen(texto_cifrado), j = 0;

    char *descifrado = (char *)malloc((n + 1) * sizeof(char)); // n * 1B

    for (int i = 0; texto_cifrado[i] != '\0'; i++)
    {
        char ch = tolower(texto_cifrado[i]);
        if (ch >= 'a' && ch <= 'z')
        {
            int position = (ch - 'a');                      
            int result = (position - desplazamientos) % 26; 
            descifrado[j++] = alphabet[result];
        }
        else
        {
            descifrado[j++] = ch; // Para comas, espacios, puntos etc.
        }
    }
    descifrado[j] = '\0';

    return descifrado;
}