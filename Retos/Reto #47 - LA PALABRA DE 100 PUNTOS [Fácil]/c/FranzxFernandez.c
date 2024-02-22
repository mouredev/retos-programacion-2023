/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */

#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char str[256];

    int index = 0, sum = 0;
    bool exit = false;

    while (!exit)
    {
        printf("Enter a word: ");
        fgets(str, sizeof(str), stdin);

        // Elminando salto de linea
        size_t len = strlen(str);
        if (len > 0 && str[len - 1] == '\n')
        {
            str[len - 1] = '\0';
        }

        for (int i = 0; str[i] != '\0'; i++)
        {
            char letra = tolower(str[i]);
            if (letra >= 'a' && letra <= 'z')
            {
                index = (letra - 'a') + 1;
                sum += index;
            }
            else
            {
                continue; // Saltarse todo lo que no sea minuscula
            }
        }
        if (sum > 100)
        {
            printf("Tu palabra contiene mas de %d Puntos. Intentalo otra vez!\n", sum);
        }
        else if (sum < 100)
        {
            printf("Tu palabra contiene menos de %d Puntos. Intentalo otra vez!\n", sum);
        }
        else
        {
            printf("Tu palabra contiene %d Puntos. Ganaste!\n", sum);
            exit = true;
        }

        sum = 0; // reseteando
    }
    
    return 0;
}