#include <stdio.h>
#include <locale.h>

#define MAX_ARRAY_LENGTH 7

static int getNumberOf0(char *text){
    int n=0;
    while (*text == 'O' && *text != '\0') {
            n++;
            text++;
        }
    return n;
}

int main(int argc, char *argv[]) {
    char *abaco[] = {"O---OOOOOOOO","OOO---OOOOOO","---OOOOOOOOO","OO---OOOOOOO","OOOOOOO---OO","OOOOOOOOO---","---OOOOOOOOO"};
    printf("Resultado: ");
    setlocale(LC_NUMERIC, "");
    for (int idx = 0; idx < MAX_ARRAY_LENGTH; idx++) {
        printf("%d", getNumberOf0(abaco[idx]));
        if(idx % 3 == 0 && idx + 1 < MAX_ARRAY_LENGTH)
            printf(".");
    }
    printf("El número formateado es: %'d\n", num);
    return 0;
}
