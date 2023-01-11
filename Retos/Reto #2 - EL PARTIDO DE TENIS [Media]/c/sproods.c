/* Reto #2 - EL PARTIDO DE TENIS */

#include <stdio.h>
#include <string.h>

typedef struct
{
    char nombre[30];
    int puntaje;
} jugador;

void datos(jugador *);          // Prototipos de funciones
void puntos(jugador *);
void tabla_Puntuaciones(jugador *);

void main(void)
{
    jugador nombre[2];
    int i;

    nombre[0].puntaje = 0;
    nombre[1].puntaje = 0;

    datos(nombre);

    while (nombre[0].puntaje < 3 && nombre[1].puntaje < 3)
    {
        puntos(nombre);
        tabla_Puntuaciones(nombre);
    }
}

void datos(jugador name[2])
{
    int i;

    for (i = 0; i < 2; i++)
    {
        printf("\nEscriba el nombre del jugador %d: ", i + 1);
        gets(name[i].nombre);
        fflush(stdin);
    }
}

void puntos(jugador name[2])
{
    int i;

    do
    {
        printf("\nDigite quién hizo punto - (1. %s o 2. %s): ", name[0].nombre, name[1].nombre);
        scanf("%d", &i);
    }
    while (i != 1 && i != 2);

    name[i - 1].puntaje++;
}

void tabla_Puntuaciones(jugador name[2])
{
    int len1, len2, i;

    len1 = strlen(name[0].nombre);
    len2 = strlen(name[1].nombre);

    printf("\n%s\t%s\n", name[0].nombre, name[1].nombre);
    for (i = 0; i < len1 / 2; i++)
        printf(" ");
    printf("%d", name[0].puntaje);
    for (i = 0; i < len1 / 2; i++)
        printf(" ");
    printf("\t");
    for (i = 0; i < len2 / 2; i++)
        printf(" ");
    printf("%d", name[1].puntaje);
}