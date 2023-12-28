#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

int RandomInt(int upper, int defSeed) {
    ///Inspirado por https://www.geeksforgeeks.org/generating-random-number-range-c/
    srand(time(NULL) * upper + defSeed);
    int num = (rand() % (upper + 1));
    return num;
}

int setMayus() {
    
    char m[1];
    printf("¿Deseas que tu contraseña tenga mayusculas?\n[1]Si\n[0]No\n");
    fflush(stdout);
    scanf("%s", m);
    fflush(stdin);
    int mayus = atoi(m);
    switch (mayus) {
        case 0:
            return 0;
            break;

        case 1:
            return 1;
            break;
        
        default:
            printf("Error debe seleccionar [1]Si o [0]No\n\n");
            setMayus();
            break;
    }
}

int setNum() {
    
    char n[1];
    printf("¿Deseas que tu contraseña tenga numeros?\n[1]Si\n[0]No\n");
    fflush(stdout);
    scanf("%s", n);
    fflush(stdin);
    int num = atoi(n);
    switch (num) {
        case 0:
            return 0;
            break;

        case 1:
            return 1;
            break;
        
        default:
            printf("Error debe seleccionar [1]Si o [0]No\n\n");
            setNum();
            break;
    }
}

int setSym() {
    
    char s[1];
    printf("¿Deseas que tu contraseña tenga simbolos?\n[1]Si\n[0]No\n");
    fflush(stdout);
    scanf("%s", s);
    fflush(stdin);
    int sym = atoi(s);
    switch (sym) {
        case 0:
            return 0;
            break;

        case 1:
            return 1;
            break;
        
        default:
            printf("Error debe seleccionar [1]Si o [0]No\n\n");
            setSym();
            break;
    }
}

int setTam() {
    
    char tama[2];
    printf("Indique la longitud de su contraseña (entre 8 y 16 caracteres):\n");
    fflush(stdout);
    scanf("%s", tama);
    fflush(stdin);
    int tam = atoi(tama);
    return tam;
}

int setGenLength(int mayus, int num, int sym) {
    
    int genLength;

    if (mayus) {
        genLength = 52;
    } else {
        genLength = 26;
    }

    if (num) {
        genLength = genLength + 10;
    }

    if (sym) {
        genLength = genLength + 7;
    }

    return genLength;
}

char *setGen(int mayus, int num, int sym) {
    
    char *minusLetters = "abcdefghijklmnopqrstuvwxyz";
    char *letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char *numbers = "0123456789";
    char *symbols = ",.-#'?!"; 
    int length = setGenLength(mayus, num, sym);
    char *generator = (char *)malloc(sizeof(char) * length);
    if (mayus) {
        strcpy(generator, letters);
    } else {
        strcpy(generator, minusLetters);
    }

    if (num) {
        strcat(generator, numbers);
    }

    if (sym) {
        strcat(generator, symbols);
    }

    return generator;
}

int strLength(char *string) {
    
    int i = 0;
    while (string[i] != '\0') {
        i++;
    }
    return i;
}

char *passwordGen(int tam) {
    
    int defSeed = 73489438;

    if (tam < 8 || tam > 16) {
        printf("Debe seleccionar entre 8 y 16 caracteres\n\n");
        passwordGen(setTam());
    }

    char *password = (char *)malloc(sizeof(char) * tam + 1);
    char *generator = setGen(setMayus(), setNum(), setSym());

    int length = strLength(generator);
    
    for (int i = 0; i < tam; i++) {
        defSeed = RandomInt(length - 1, defSeed);
        password[i] = generator[RandomInt(length - 1, defSeed)];
    }
    password[tam] = '\0';

    printf("Tu contraseña es: %s\n", password);

    char ans[1];
    printf("¿Deseas generar otra?\n[1]Si\n[0]No\n");
    fflush(stdout);
    scanf("%s", ans);
    fflush(stdout);
    int repeat = atoi(ans);

    switch (repeat) {
    case 0:
        break;
    
    case 1:
        passwordGen(setTam());
    
    default:
        break;
    }

    return password;
    
}

int main() {
    
    passwordGen(setTam());
}