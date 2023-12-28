/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 * THE AUTOR OF THIS DISASTER: Raddock360
 * 31/01/2023
*/

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

/* CHECK NUMBER
 * Check if the given number is even, prime or fibonacci
 * INPUT: *n     -> pointer to number variable
 *        *par   -> pointer to par variable
 *        *primo -> pointer to prime variable
 *        *fibo  -> pointer to fibonacci variable
 * OUPUT: EXIT_SUCCES 
 */
int checkNumber(long int *n, unsigned char *par, unsigned char *primo, unsigned char *fibo) {
    unsigned char prime_counter = 0;

    // Check if given number is even
    if((*n % 2) == 0) { *par = 1; }

    // Check if given number is prime
    for(unsigned long int i = 1; i <= *n; ++i) {
        if((*n % i) == 0) { ++prime_counter; } 
    }
    if(prime_counter == 2) { *primo = 1; }

    // Check if given number is fibonacci
    unsigned long int result = 1;
    unsigned long int op1 = 0;
    unsigned long int op2 = 0;

    while(result <= *n) {
        if(result == *n) { *fibo = 1; }
        op2 = result;
        result += op1;
        op1 = op2;
    }

    return EXIT_SUCCESS;
}

/*
 * HERE BEGIN THE CODE OF THE DISASTER xDDDDDDD
 *  Please be patient and forgive the mistakes of a novice like me.
 *  Any suggestions or positive comments are welcome.
 *  Enjoy coding the world and THX!!!!!!!!!
 */
int main(int argc, char **argv) {
    long int number = 0;
    unsigned char par = 0, primo = 0, fibonacci = 0;
    char *end;
    errno = 0;

    if(argc < 2) {
        printf("Program usage: [executable_name] [number to test]\nExample: %s 21\n", argv[0]);
        return EXIT_FAILURE;
    }
    number = strtol(argv[1], &end, 10);

    if(errno == ERANGE) {
        printf("ERROR %d: number too big, excedes the data type range\n", errno);
        return EXIT_FAILURE;
    }
    if(number <= 0) { // Check if the given number is unsigned
        printf("ERROR: number must be greater than ZERO\n");
        return EXIT_FAILURE;
    }

    checkNumber(&number, &par, &primo, &fibonacci);

    printf("The number %ld is ", number);
    par && printf("PAR ");
    primo && printf("PRIME ");
    fibonacci && printf("FIBONACCI ");
    !par && !primo && !fibonacci && printf("not PAR nor PRIME nor FIBONACCI ");
    printf("\n");
    

    return EXIT_SUCCESS; 
}
