#include <stdio.h>

int main(int argc, char *argv[]) {
    for (int i = 1; i <= 100; i++) {
        if (i%3 == 0 && i%5 == 0)
            fprintf(stdout, "fizzbuzz\n");
        else if(i%3 == 0)
            fprintf(stdout, "fizz\n");
        else if(i%5 == 0)
            fprintf(stdout, "buzz\n");
        else
            fprintf(stdout, "%d\n", i);
    }
    return 0;
}
