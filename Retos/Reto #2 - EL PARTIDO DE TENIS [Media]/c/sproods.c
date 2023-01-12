/* Reto #2 - EL PARTIDO DE TENIS */

#include <stdio.h>
#include <string.h>
#include <math.h>

typedef struct
{
    char nombre[30];
    int puntaje;
    char nomen[5];
} jugador;

void datos(jugador *);          // Prototipos de funciones
void puntos(jugador *);
void nomenclatura(jugador *);
void tabla_Puntuaciones(jugador *);

void main(void)
{
    jugador player[2];
    int i;

    player[0].puntaje = 0;
    strcpy(player[0].nomen, "Love");
    player[1].puntaje = 0;
    strcpy(player[1].nomen, "Love");

    datos(player);

    while (((player[0].puntaje != 3 && player[1].puntaje != 3) && (player[0].puntaje <= 3 || player[1].puntaje <= 3)) || (fabs(player[0].puntaje - player[1].puntaje)) < 2)
    {
        puntos(player);
        nomenclatura(player);
        tabla_Puntuaciones(player);
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

void nomenclatura(jugador name[2])
{
    int i;
    char N[4][5] = {"Love", "15", "30", "40"};

    while ((name[0].puntaje < 3 && name[1].puntaje <= 3) || (name[0].puntaje <= 3 && name[1].puntaje < 3))
    {
        for (i = 0; i < 2; i++)
        {
            if (name[i].puntaje == 0)
                strcpy(name[i].nomen, "Love");
            else
                if (name[i].puntaje == 1)
                    strcpy(name[i].nomen, "15");
                else
                    if (name[i].puntaje == 2)
                        strcpy(name[i].nomen, "30");
                    else
                        if (name[i].puntaje == 3)
                            strcpy(name[i].nomen, "40");
        }
    }
}

void tabla_Puntuaciones(jugador name[2])
{
    int len1, len2, i;

    len1 = strlen(name[0].nombre);
    len2 = strlen(name[1].nombre);

    printf("\n%s\t%s\n", name[0].nombre, name[1].nombre);
    for (i = 0; i < len1 / 2; i++)
        printf(" ");
    printf("%s", name[0].nomen);
    for (i = 0; i < len1 / 2; i++)
        printf(" ");
    printf("\t");
    for (i = 0; i < len2 / 2; i++)
        printf(" ");
    printf("%s", name[1].nomen);
    printf("\n");
}