/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

/* - heterograma:  Un heterograma es una palabra o frase en la que no se repite ninguna letra. Esto significa que cada letra en la palabra o frase aparece solo una vez. Por ejemplo, la palabra "murciélago" es un heterograma en español, ya que ninguna letra se repite.*/

/* - isograma: Un isograma es similar a un heterograma, pero se aplica específicamente a palabras o frases en las que no se repite ninguna letra, incluyendo espacios y signos de puntuación. Por lo tanto, un isograma puede contener varios espacios y caracteres especiales sin repetir ninguna letra. "*/

/* - pangrama: Un pangrama es una frase o texto que contiene todas las letras del alfabeto al menos una vez. En otras palabras, un pangrama utiliza cada letra posible del idioma en el que está escrito.
 */

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

static bool isHeterograma_Isograma(char *str);
static bool isIsograma(char *str); 
static bool isPangrama(char *str);
static int string_len(char *str);
char *make_lower_case(char *str);

int main(int argc, char const *argv[])
{
    char *msg = make_lower_case("murciélago");
    char *msg2 = make_lower_case("El veloz murcielago hindu comía feliz cardillo y kiwi");

    printf("Es un heterograma: %d\n", isHeterograma_Isograma(msg)); // 1 = True | 0 = False
    printf("Es un pangrama: %d\n", isPangrama(msg2)); // 1 = True | 0 = False

    free(msg);
    free(msg2);
    return 0;
}

static int string_len(char *str)
{
    int count = 0;
    while (str[count] != '\0')
    {
        count++;
    }

    return count;
}
char *make_lower_case(char *str) 
{
    int n = string_len(str);
    char *tolower = (char *)malloc(n * sizeof(char)); // n * 1B

    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] >= 'A' && str[i] <= 'Z')
        {
            tolower[i] = str[i] + 32; // Upper Case to Lower Case
        }
        else
        {
            tolower[i] = str[i];
        }
    }
    tolower[n] = '\0';

    return tolower;
}
static bool isHeterograma_Isograma(char *str) 
{
    int n = string_len(str);

    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j <= n; j++)
        {
            if (str[j] == str[i])
            {
                return false;
            }
        }
    }
    return true;
}
static bool isPangrama(char *str)
{
    int n = string_len(str);
    int idx = 0;
    bool letter_found[26] = {false};

    for (int i = 0; i < n; i++)
    {
        if (str[i] >= 'a' && str[i] <= 'z')
        {
            idx = str[i] - 'a';
            letter_found[idx] = true;
        }
    }

    for (int i = 0; i < 26; i++)
    {
        if (!letter_found[i])
        {
            return false; 
        }
    }

    return true;
}
