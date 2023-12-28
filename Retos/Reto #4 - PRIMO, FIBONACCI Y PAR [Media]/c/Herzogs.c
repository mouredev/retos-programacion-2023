#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
#include <stdbool.h>

static inline bool isPar(const uint64_t num){
    return num%2 == 0;
}

static inline bool isPrimo(uint64_t num){
    uint8_t cantPrimo = 0;
    if(num > 2){
        for (uint32_t i = 1; i <= num; i++) {
            if(num % i == 0)
                cantPrimo ++;
        }
    }
    return cantPrimo == 2;
}

static inline bool perteneceAFibonacci(uint64_t valor){
    uint64_t num1 = 0, num2 = 1, term = 0;
    do {
        if(valor > term)
            term = num1 + num2;
        num1 = num2;
        num2 = term;
    } while (valor > term);
    return valor == term;
}

int main(int argc, char *argv[]) {
    uint64_t number = 5;
    fprintf(stdout,"El numero %"PRIu64"\n", number);
    fprintf(stdout, "\n%s", isPar(number)==true?"Es par":"No es par");
    fprintf(stdout, "\n%s",(isPrimo(number) == true ? "Es Primo":"No es Primo"));
    fputs((perteneceAFibonacci(number) == true)? "\nPertenece a la secuencia" : "\nNo pertenece a Fibonnaci", stdout);
    return 0;
}
