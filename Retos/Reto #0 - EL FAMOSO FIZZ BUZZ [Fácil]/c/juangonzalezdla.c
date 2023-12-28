#include <stdio.h>

int main()
{
    for(int n = 1; n <= 100; n++) {
        if (n % 3 == 0 && n % 5 == 0) {
            printf("%d fizzbuzz\n", n);
        } else if (n % 3 == 0) {
            printf("%d fizz\n", n);
        } else if (n % 5 == 0) {
            printf("%d buzz\n", n);
        } else {
            printf("%d\n", n);
        }
    }
    
    return 0;
}