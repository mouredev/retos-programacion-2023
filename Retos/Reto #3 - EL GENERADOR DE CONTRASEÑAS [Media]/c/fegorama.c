/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <string.h>
#include <assert.h>

#define UPPER 1
#define NUMBERS 2
#define SYMBOLS 4

const char alpha_lower[] = "abcdefghijklmnopqrstuvwxyz";
const char alpha_upper[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const char numbers[] = "0123456789";
const char symbols[] = "!$%&/()=?^*¨Ç;:_<>|@#~[]{}";

void build_passwd(const unsigned int conf, unsigned char *str_passwd)
{
    unsigned int max_str = 16;
    unsigned int x, c;
    time_t t;

    if ((conf >> 8) != 0)
        max_str = conf >> 8;

    srand((unsigned)time(&t));

    unsigned int i;
    for (i = 0; i < max_str; i++)
    {
        x = rand() % 2;
        if (conf == 0 || x == 0)
            c = alpha_lower[rand() % 26];
        else
            switch (conf & 15)
            {
            case UPPER | NUMBERS | SYMBOLS:
                x = rand() % 3 + 1;
                if (x == 2)
                    c = alpha_upper[rand() % 26];
                else if (x == 3)
                    c = numbers[rand() % 10];
                else
                    c = symbols[rand() % 26];
                break;
            case SYMBOLS | NUMBERS:
                x = rand() % 2 + 1;
                if (x == 1)
                    c = symbols[rand() % 26];
                else
                    c = numbers[rand() % 10];
                break;
            case UPPER | SYMBOLS:
                x = rand() % 2 + 1;
                if (x == 1)
                    c = alpha_upper[rand() % 26];
                else
                    c = symbols[rand() % 26];
                break;
            case SYMBOLS:
                c = symbols[rand() % 26];
                break;
            case UPPER | NUMBERS:
                x = rand() % 2 + 1;
                if (x == 1)
                    c = alpha_upper[rand() % 26];
                else
                    c = numbers[rand() % 10];
                break;
            case NUMBERS:
                c = numbers[rand() % 10];
                break;
            case UPPER:
                c = alpha_upper[rand() % 26];
                break;
            }

        str_passwd[i] = c;
    }

    str_passwd[i] = '\0';
}

int main(int argc, char **argv)
{
    unsigned int conf = 0;
    int c, v, len_passwd = 0;
    unsigned char str_passwd[17];

    while ((c = getopt(argc, argv, "l:uns?")) != -1)
        switch (c)
        {
        case 'l':
            v = atoi(optarg);
            if (v < 8 || v > 16)
            {
                fprintf(stderr, "La longitud del password es de 8 a 16.\n");
                abort();
            }
            len_passwd = atoi(optarg) << 8;
            conf = conf + len_passwd;
            break;
        case 'u':
            conf = conf | UPPER;
            break;
        case 'n':
            conf = conf | NUMBERS;
            break;
        case 's':
            conf = conf | SYMBOLS;
            break;
        case '?':
            printf("Sintaxis: pass [-l 8..16] [-u|-n|-s]\n");
            return EXIT_SUCCESS;
        default:
            printf("default: c = %d", c);
            abort();
        }

    build_passwd(conf, str_passwd);
    printf("%s", str_passwd);

    return EXIT_SUCCESS;
}
