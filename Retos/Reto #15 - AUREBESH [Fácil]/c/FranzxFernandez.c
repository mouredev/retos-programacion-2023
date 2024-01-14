/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

static char *spanish_to_aurebesh(const char *texto);
static char *aurebesh_to_spanish(const char *texto);

int main(int argc, char const *argv[])
{
    char *str = "HOLA.";
    char *str_1 = "Hola, mundo!";
    char *str_2 = "Me llamo Max Mustermann";
    char *str_3 = "Esto es una prueba.";
    char *str_4 = "Tu tienes un piano, pero yo tengo una flauta.";
    char *str_5 = "Manana voy a ver el partido de futbol, y tu que vas hacer manana?";

    //----------------------------------------------//
    char *mensaje = spanish_to_aurebesh(str);
    char *original = aurebesh_to_spanish(mensaje);
    //----------------------------------------------//
    char *mensaje_1 = spanish_to_aurebesh(str_1);
    char *original_1 = aurebesh_to_spanish(mensaje_1);
    //----------------------------------------------//
    char *mensaje_2 = spanish_to_aurebesh(str_2);
    char *original_2 = aurebesh_to_spanish(mensaje_2);
    //----------------------------------------------//
    char *mensaje_3 = spanish_to_aurebesh(str_3);
    char *original_3 = aurebesh_to_spanish(mensaje_3);
    //----------------------------------------------//
    char *mensaje_4 = spanish_to_aurebesh(str_4);
    char *original_4 = aurebesh_to_spanish(mensaje_4);
    //----------------------------------------------//
    char *mensaje_5 = spanish_to_aurebesh(str_5);
    char *original_5 = aurebesh_to_spanish(mensaje_5);
    //----------------------------------------------//

    printf("- Mensaje traducido 1: %s\n", mensaje);
    printf("- Mensaje original: %s\n", original);
    printf("\n");

    printf("- Mensaje traducido 2: %s\n", mensaje_1);
    printf("- Mensaje original: %s\n", original_1);
    printf("\n");

    printf("- Mensaje traducido 3: %s\n", mensaje_2);
    printf("- Mensaje original: %s\n", original_2);
    printf("\n");

    printf("- Mensaje traducido 4: %s\n", mensaje_3);
    printf("- Mensaje original: %s\n", original_3);
    printf("\n");

    printf("- Mensaje traducido 5: %s\n", mensaje_4);
    printf("- Mensaje original: %s\n", original_4);
    printf("\n");

    printf("- Mensaje traducido 6: %s\n", mensaje_5);
    printf("- Mensaje original: %s\n", original_5);
    printf("\n");

    free(mensaje);
    free(original);
    free(mensaje_1);
    free(original_1);
    free(mensaje_2);
    free(original_2);
    free(mensaje_3);
    free(original_3);
    free(mensaje_4);
    free(original_4);
    free(mensaje_5);
    free(original_5);

    return 0;
}
static char *spanish_to_aurebesh(const char *texto) 
{
    const char *alpha[] = {
        "Aurek",
        "Besh",
        "Cresh",
        "Dorn",
        "Esk",
        "Forn",
        "Grek",
        "Herf",
        "Isk",
        "Jenth",
        "Krill",
        "Leth",
        "Mern",
        "Nern",
        "Osk",
        "Peth",
        "Qek",
        "Resh",
        "Senth",
        "Trill",
        "Usk",
        "Vev",
        "Wesk",
        "Xesh",
        "Yirt",
        "Zerek",
    };

    // Codigo para calcular el tamano requerido para allocar memoria en el heap.
    int tamano = 1;
    for (int i = 0; texto[i] != '\0'; i++)
    {
        if (isalpha(texto[i]))
        {
            int position = tolower(texto[i]) - 'a';
            tamano += strlen(alpha[position]);
        }
        else
        {
            tamano++; // Para caracteres no alfabéticos
        }
    }

    int j = 0;
    char *array = (char *)malloc(tamano * sizeof(char)); // n * 1B

    if (array == NULL)
    {
        printf("Failed to allocate memory in the heap!\n");
        return NULL;
    }

    for (int i = 0; texto[i] != '\0'; i++)
    {
        char ch = tolower(texto[i]);
        if (ch >= 'a' && ch <= 'z')
        {
            int position = ch - 'a'; 
            const char *character = alpha[position];
            while (*character)
            {
                array[j++] = *character++;
            }
        }
        else
        {
            array[j++] = ch;
        }
    }
    array[j] = '\0';

    return array; 
}

static char *aurebesh_to_spanish(const char *texto)
{
    const char *alpha[] = {
        "Aurek",
        "Besh",
        "Cresh",
        "Dorn",
        "Esk",
        "Forn",
        "Grek",
        "Herf",
        "Isk",
        "Jenth",
        "Krill",
        "Leth",
        "Mern",
        "Nern",
        "Osk",
        "Peth",
        "Qek",
        "Resh",
        "Senth",
        "Trill",
        "Usk",
        "Vev",
        "Wesk",
        "Xesh",
        "Yirt",
        "Zerek",
    };

    int tamano = 1; 
    for (int i = 0; texto[i] != '\0'; i++)
    {
        if (isalpha(texto[i]))
        {
            int position = tolower(texto[i]) - 'a';
            tamano += strlen(alpha[position]);
        }
        else
        {
            tamano++;
        }
    }

    char *array = (char *)malloc(tamano * sizeof(char)); 
    if (array == NULL)
    {
        printf("Failed to allocate memory in the heap!\n");
        return NULL;
    }

    int count = 0;
    for (int i = 0; texto[i] != '\0'; i++)
    {
        if (texto[i] >= 'A' && texto[i] <= 'Z')
        {
            array[count++] = texto[i];
        }
        else
        {
            if (texto[i] == ' ' || texto[i] == ',' || texto[i] == '.' || texto[i] == '!' || texto[i] == '?')
            {
                array[count++] = texto[i];
            }
            continue;
        }
    }
    array[count] = '\0';

    return array;
}