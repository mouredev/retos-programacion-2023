/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

static void RGB_TO_HEX(const int r, const int g, const int b);
static void HEX_TO_RGB(const char *hex_str);

int main(int argc, char const *argv[])
{
    // Test case 1:
    RGB_TO_HEX(255, 1, 100);
    HEX_TO_RGB("#FF0164");
    printf("\n");

    // Test case 2:
    RGB_TO_HEX(10, 100, 50);
    HEX_TO_RGB("#0A6432");
    printf("\n");

    // Test case 3:
    RGB_TO_HEX(0, 0, 0);
    HEX_TO_RGB("#000000");
    printf("\n");

    // Test case 4:
    RGB_TO_HEX(20,-50,2);
    HEX_TO_RGB("ZZZZZZZ");
    printf("\n");
    return 0;
}
static void RGB_TO_HEX(const int r, const int g, const int b)
{
    if ((r < 0 || r > 255) || (g < 0 || g > 255) || (b < 0 || b > 255))
    {
        printf("ERROR. Please give values between (0-255)\n");
        return;
    }
    printf("- RGB: (%d, %d, %d) -> ", r, g, b);
    printf("HEX: #%02X%02X%02X\n", r, g, b);
}
static void HEX_TO_RGB(const char *hex_str)
{
    if (hex_str[0] != '#' || (strlen(hex_str) != 7))
    {
        printf("ERROR. Please give a valid HEX value\n");
        return;
    }
    int r, g, b;
    bool is_Hex = false;
    for (int i = 1; hex_str[i] != '\0'; i++)
    {
        if (isxdigit(hex_str[i]) != 0) // is a hexadecimal character
        {
            is_Hex = true;
        }
        else
        {
            is_Hex = false;
            break;
        }
    }

    if (is_Hex)
    {
        sscanf(hex_str, "#%02X%02X%02X", &r, &g, &b);
        printf("- HEX: %s -> ", hex_str);
        printf("RGB: (%d, %d, %d)\n", r, g, b);
    }
}