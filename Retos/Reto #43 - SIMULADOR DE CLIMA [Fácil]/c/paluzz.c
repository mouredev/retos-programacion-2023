/*
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
 *     siguiente disminuye en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

void iniciarTimer(void);
int randomTemp(int);
int max(int *, int);
int min(int *, int);
void clima(int, float, int);

int main(void)
{
    clima(24, 0.9, 10);
    clima(26, 0.5, 7);
    clima(29, 0.3, 14);

    return 0;
}

void iniciarTimer(void)
{
    srand(time(NULL));
}

int randomTemp(int temp)
{
    int prob = rand() % 20;
    // asignamos una Prob de 5% de aumentar y un 5% de disminuir
    if (prob == 1)
    {
        temp += 2;
    }
    else if (prob == 2)
    {
        temp -= 2;
    }

    return temp;
}

int max(int *p, int cant)
{
    int i, max = 0;
    for (i = 0; i < cant; i++)
    {
        if (*(p + i) > max)
        {
            max = *(p + i);
        }
    }
    return max;
}

int min(int *p, int cant)
{
    int i, min = *(p + 0);
    for (i = 0; i < cant; i++)
    {
        if (*(p + i) < min)
        {
            min = *(p + i);
        }
    }
    return min;
}

void clima(int tempActual, float plluvia, int cantDias)
{
    iniciarTimer();

    int llueve = 0, i;
    int maxTemp = 0, minTemp;
    int *dia;
    // asignamos memoria dinamica
    dia = (int *)malloc(sizeof(int) * cantDias);
    if (dia == NULL)
    {
        printf("Error asignacion memoria\n");
        exit(1);
    }

    for (i = 0; i < cantDias; i++)
    {
        if (plluvia >= 1)
        {
            llueve++;
            tempActual -= 1;
        }
        if (tempActual > 25)
        {
            plluvia += 0.2;
        }
        else if ((maxTemp - tempActual) >= 5)
        {
            plluvia -= 0.2;
        }
        // guardamos la temperatura actual
        dia[i] = tempActual;
        // calculamos la temp maxima
        maxTemp = max(dia, (i + 1));
        // actualizamos la temperatura
        tempActual = randomTemp(tempActual);
    }

    minTemp = min(dia, cantDias);

    printf("Temperatura maxima: %d°C\n", maxTemp);
    printf("Temperatura minima: %d°C\n", minTemp);
    if (llueve > 0)
    {
        printf("Llueve %d dias\n", llueve);
    }
    else
    {
        printf("No ha llovido\n");
    }
    free(dia);
}