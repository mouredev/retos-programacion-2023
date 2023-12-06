/*
 * # Reto #4: PRIMO, FIBONACCI Y PAR
 * #### Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23
 *
 * ## Enunciado
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 * .....................................................................................................................
 * Author: kyrex23
 * Date:   10/02/2023
 */

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

const u_int32_t MIN_VALUE = 0;
const u_int32_t MAX_VALUE = UINT32_MAX;

int is_even(u_int32_t num);
int is_prime(u_int32_t num);
int is_fibonacci(u_int32_t num);

// ---------------------------------------------------------------------------------------------------------------------

int main(int argc, char *argv[]) {
	if (argc < 2) {
		printf("[ERROR] Missing required argument <number>\n Usage: %s <number>\n", argv[0]);
		return EXIT_FAILURE;
	}

	// I want to check if the argument is greater than `MAX_VALUE` which is defined as `UINT32_MAX`
	// If I convert the input number to `u_int32_t` the conversion will be truncated to fit within the range
	// so I am converting the number to `u_int64_t` and then only casting it to `u_int32_t` if it is within range
	u_int64_t raw_number = strtoull(argv[1], NULL, 10);
	if (raw_number > UINT32_MAX) {
		printf("[ERROR] The number: '%s' is out of range [%u, %u]\n", argv[1], MIN_VALUE, MAX_VALUE);
		return EXIT_FAILURE;
	}
	u_int32_t number = (u_int32_t)raw_number;

	printf("%u %ses primo, %ses fibonacci y %ses par\n", number, is_prime(number) ? "" : "no ",
		   is_fibonacci(number) ? "" : "no ", is_even(number) ? "" : "no ");
}

// ---------------------------------------------------------------------------------------------------------------------

int is_even(u_int32_t num) {
	return num % 2 == 0;
}

int is_prime(u_int32_t num) {
	int prime = (num > 1);	// numbers 0 and 1 are not prime numbers by definition

	u_int64_t current_divisor = 2;
	while (prime && current_divisor * current_divisor <= num)
		prime = (num % current_divisor++ != 0);

	return prime;
}

int is_fibonacci(u_int32_t num) {
	if (num == 0 || num == 1) return 1;

	u_int32_t previous_element = 1;
	u_int64_t current_element = 2;

	while (current_element < num) {
		u_int32_t aux = current_element;
		current_element += previous_element;
		previous_element = aux;
	}

	return current_element == num;
}
