#include <stdio.h>
#include <string.h>

const char COMMA[] = ",";
const char *POINTS[] = {"Love", "15", "30", "40", "Deuce", "Ventaja"};

int match(char *game)
{
    int p1 = 0, p2 = 0;
    game = strtok(game, COMMA);

    if (game != NULL)
        while (game != NULL)
        {
            if (strncmp(game, "P1", sizeof(char) * 2) == 0)
                if (p1 == 3 && p2 == 4)
                    p2--;
                else
                    p1++;
            else if (strncmp(game, "P2", sizeof(char) * 2) == 0)
                if (p2 == 3 && p1 == 4)
                    p1--;
                else
                    p2++;
            else
                printf("Error en la introducción de una jugada.\n");

            if (p1 == 5)
                return 1;
            else if (p2 == 5)
                return 2;
            else
                if (p1 == 3 && p2 == 3)
                    printf("%s\n", POINTS[4]);
                else if (p1 == 4 || p2 == 4)
                    printf("Ventaja %s\n", (p1 == 4 ? "P1" : "P2"));
                else
                    printf("%s - %s\n", POINTS[p1], POINTS[p2]);

            game = strtok(NULL, COMMA);
        }

    return 1;
}

int main(int args, char **argv)
{
    int win;

    if (args != 2)
    {
        printf("Debe ingresar la jugada separada por comas y sin espacios (ejemplo: P1,P1,P2,P2,P1,P2,P1,P2,P1,P1).");
        return 1;
    }

    if (match(argv[1]) == 1)
        printf("P1 ganador\n");
    else
        printf("P2 ganador\n");

    return 0;
}