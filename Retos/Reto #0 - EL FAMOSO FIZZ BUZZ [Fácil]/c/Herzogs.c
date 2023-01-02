#include <stdio.h>

int main(int argc, char *argv[]) {
    for (int i = 1; i <= 100; i++) {
        if (i%3 == 0 && i%5 == 0)
            fprintf(stdout, "%d - fizzbuzz \n", i);
        else if(i%3 == 0)
            fprintf(stdout, "%d - fizz \n", i);
        else if(i%5 == 0)
            fprintf(stdout, "%d - buzz \n", i);
        else
            fprintf(stdout, "%d\n", i);
    }
    return 0;
}
