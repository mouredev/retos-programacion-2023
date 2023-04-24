#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>


int main(int argc, char const *argv[]) {
    for (int i = 1; i <= 100; i++) {
        bool non_multiple = true;
        if ((i % 3) == 0) {
            printf("fizz");
            non_multiple = false;
        }
        if ((i % 5) == 0) {
            printf("buzz");
            non_multiple = false;
        }
        if (non_multiple) {
            printf("%d", i);
        }
        printf("\n");
    }
    return 0;
}
