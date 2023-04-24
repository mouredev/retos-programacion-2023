#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    for(size_t i = 1; i <= 100; ++i) {
        if(i % 3 == 0) { printf("fizz"); }
        if(i % 5 == 0) { printf("buzz"); }
        if(i % 3 && i % 5) { printf("%zu", i); }

        printf("\n");
    }

    return EXIT_SUCCESS;
}
