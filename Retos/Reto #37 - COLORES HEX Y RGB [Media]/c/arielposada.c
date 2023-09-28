#include <stdio.h>

void rgb_to_hex(int r, int g, int b, char *hex) {
    sprintf(hex, "#%02X%02X%02X", r, g, b);
}

void hex_to_rgb(const char *hex, int *r, int *g, int *b) {
    sscanf(hex, "#%02x%02x%02x", r, g, b);
}

int main() {
    char hex[8];
    int r, g, b;

    printf("Examples:\n");

    printf("RGB to HEX (midnight blue):\n");
    rgb_to_hex(25, 25, 112, hex);
    printf("%s\n", hex);

    printf("HEX to RGB (royal blue):\n");
    hex_to_rgb("#4169E1", &r, &g, &b);
    printf("(r: %d, g: %d, b: %d)\n", r, g, b);

    return 0;
}
