#include <stdio.h>
#include <stdlib.h>

void build_triforce(int rows)
{
    int stars_row, bs_row, total_stars = rows * 2;
    int i, k;

    for (i = 1; i <= rows; i++)
    {
        stars_row = (i * 2) - 1;
        bs_row = ((total_stars - stars_row) / 2) + (total_stars / 2);

        for (k = 1; k <= bs_row; k++)
            printf(" ");

        for (k = 1; k <= stars_row; k++)
            printf("*");

        printf("\n");
    }

    for (i = 1; i <= rows; i++)
    {
        stars_row = (i * 2) - 1;
        bs_row = ((total_stars - stars_row) / 2);

        for (k = 1; k <= bs_row; k++)
            printf(" ");

        for (k = 1; k <= stars_row; k++)
            printf("*");

        for (k = 1; k <= (bs_row * 2) + 1; k++)
            printf(" ");

        for (k = 1; k <= stars_row; k++)
            printf("*");

        printf("\n");
    }
}

int main(int args, char **argv)
{
    if (args != 2)
    {
        printf("Debe proporcionar el número de filas.");
        return 1;
    }

    int rows = atoi(argv[1]);

    if (rows < 3 || rows > 50)
    {
        printf("Filas no correctas: %d", rows);
        return 1;
    }

    build_triforce(rows);
}