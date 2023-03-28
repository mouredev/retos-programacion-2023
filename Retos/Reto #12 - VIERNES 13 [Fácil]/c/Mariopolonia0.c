#include <stdio.h>
#include <time.h>

struct tm readDate() {
    struct tm date = {0};

    printf("Enter the number of the month:");
    scanf("%d", &date.tm_mon);

    printf("Enter year:");
    scanf("%d", &date.tm_year);

    // Ajustar el mes a partir de 0 enero a 0 enero
    date.tm_mon--;

    return date;
}

void isFriday13(struct tm date) {
    // Ajustar el año a partir de 1900 a partir del año 0
    date.tm_year -= 1900;

    // Ajustar el mes a partir de 0 enero a 0 enero
    date.tm_mon--;

    // Establecer el día del mes en 13
    date.tm_mday = 13;

    // Convertir la fecha en un tiempo UNIX
    time_t t = mktime(&date);

    // Convertir el tiempo UNIX en una estructura tm
    struct tm* ptm = localtime(&t);

    if (ptm->tm_wday != 5)
        printf("The 13th is Friday\n");
    else
        printf("The 13th is not Friday\n");
}

int main() {
    struct tm date = readDate();
    isFriday13(date);

    return 0;
}
