/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

static int len(char *str)
{
    int count = 0;
    while (str[count] != '\0')
    {
        count++;
    }
    return count;
}

int main(int argc, char const *argv[])
{
    char *url = "https://retosdeprogramacion.com?year=2023&challenge=0";
    int n = len(url); 

    char *params = (char*)malloc(n * sizeof(char)); // Allocating dynamically 10 * 1B = 10Bytes

    if (params == NULL)
    {
        printf("Failed allocating memory in the Heap!\n");
        return -1;
    }
    
    int j = 0;
    bool state = false;
    for (int i = 0; i < n; i++) 
    {
        if (url[i] == '=')
        {
            state = true;
            continue; // Saltando el '='

        }else if (url[i] == '&' || url[i] == '\0' )
        {
            if (state)
            {
                params[j++] = ',';
            }
            state = false;
        }else if (state)
        {
            params[j++] = url[i];
        }
    }
   if (j > 0 && params[j - 1] == ',') { j--; } 
    params[j] = '\0'; // End of string

    printf("[");
    for (int z = 0; z < j; z++)
    {
        if (params[z] == ',')
        {
            printf("\", \"");
        }
        else
        {
            printf("%c", params[z]);
        }
    }
    printf("\"]\n");

    free(params);
    return 0;
}