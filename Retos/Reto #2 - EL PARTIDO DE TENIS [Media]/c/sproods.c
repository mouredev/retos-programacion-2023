/* Reto #2 - EL PARTIDO DE TENIS */

#include <stdio.h>

typedef struct
{
    char nombre[30];
    int puntaje;
} jugador;

void main(void)
{
    jugador nombre_puntos[2];
    int i;

    for (i = 0; i < 2; i++)
    {
        printf("\nDigite el nombre del jugador %d: ", i + 1);
        gets(nombre_puntos[i].nombre);

        printf("Digite el puntaje del jugador %d: ", i + 1);
        scanf("%d", &nombre_puntos[i].puntaje);
        fflush(stdin);
    }

    for (i = 0; i < 2; i++)
        printf("\nNombre_jugador%d:\t%s\nPuntos_jugador%d:\t%d\n", i + 1, nombre_puntos[i].nombre, i + 1, nombre_puntos[i].puntaje);
}
