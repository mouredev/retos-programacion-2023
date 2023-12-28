#include <stdio.h>
#include <string.h>

const char *alpha[] = {"4", "13", "[", ")", "3", "|=", "&", "#",
                       "I", ",_|", ">|", "1", "/\\/\\", "^/", "0",
                       "|*", "_,", "l2", "5", "7", "(_)", "\\/",
                       "\\/\\/", "><", "j", "2"};

void translate(char *s)
{
    int c;
    for (int i = 0; i < strlen(s) + 1; c = s[i++])
        if ((c >= 65 && c <= 90) || (c >= 97 && c <= 122))
            printf("%s", (c <= 90) ? alpha[c - 65] : alpha[c - 97]);
}

int main(int args, char** argv)
{
    if (args != 2)
    {
        printf("Debe proporcionar la cadena a traducir.");
        return 1;
    }
    else if (strlen(argv[1]) > 128)
    {
        printf("La cadena a traducir no puede superar los 128 caracteres.");
        return 1;
    }
    else
        translate(argv[1]);
}