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
    player[1].puntaje = 0;

    datos(player);

    // while (((player[0].puntaje != 3 && player[1].puntaje != 3) || (fabs(player[0].puntaje - player[1].puntaje)) < 2)  && ((player[0].puntaje <= 3 && player[1].puntaje <= 3) || (fabs(player[0].puntaje - player[1].puntaje)) < 2))
    while (((player[0].puntaje != 3 && player[1].puntaje != 3) && (player[0].puntaje <= 3 && player[1].puntaje <= 3)) || ((fabs(player[0].puntaje - player[1].puntaje)) < 2))
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

    if ((name[0].puntaje < 3 && name[1].puntaje <= 3) || (name[0].puntaje <= 3 && name[1].puntaje < 3))
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

void tabla_Puntuaciones(jugador name[2])
{
    int len1, len2, i;

    len1 = strlen(name[0].nombre);
    len2 = strlen(name[1].nombre);

    if ((name[0].puntaje < 3 && name[1].puntaje <= 3) || (name[0].puntaje <= 3 && name[1].puntaje < 3))
    {
        if ((fabs(name[0].puntaje - name[1].puntaje) >= 2) && (name[0].puntaje > 2 || name[1].puntaje > 2))
        {
            if (name[0].puntaje > name[1].puntaje)
                printf("HA GANADO %s\n", name[0].nombre);
            if (name[1].puntaje > name[0].puntaje)
                printf("HA GANADO %s\n", name[1].nombre);
        }
        else
        {
            printf("\n%s\t%s\n", name[0].nombre, name[1].nombre);
            printf("%s", name[0].nomen);
            for (i = 0; i < len1; i++)
                printf(" ");
            printf("\t");
            printf("%s", name[1].nomen);
            printf("\n");
        }
    }
    else
    {
        if (name[0].puntaje == name[1].puntaje)
            printf("\nDEUCE\n");
        else
        {
            if (fabs(name[0].puntaje - name[1].puntaje) == 1)
            {
                if (name[0].puntaje > name[1].puntaje)
                    printf("\nVENTAJA %s\n", name[0].nombre);
                else
                    printf("\nVENTAJA %s\n", name[1].nombre);
            }
            if (fabs(name[0].puntaje - name[1].puntaje) == 2)
            {
                if (name[0].puntaje > name[1].puntaje)
                    printf("\nHA GANADO %s\n", name[0].nombre);
                if (name[1].puntaje > name[0].puntaje)
                    printf("\nHA GANADO %s\n", name[1].nombre);
            }
        }
    }
}