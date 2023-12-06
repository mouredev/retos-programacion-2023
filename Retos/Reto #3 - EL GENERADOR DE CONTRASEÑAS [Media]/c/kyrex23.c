/*
 * # Reto #3: EL GENERADOR DE CONTRASEÑAS
 * #### Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23
 *
 * ## Enunciado
 *
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 *
 * .....................................................................................................................
 *
 * Author: kyrex23
 * Date:   07/02/2023
 *
 * NOTE: You can run this program without arguments to see the usage
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/param.h>
#include <time.h>

const int MIN_LENGTH = 8;
const int MAX_LENGTH = 16;

const char *LENGTH_FLAG = "--length";
const char *UPPERS_FLAG = "--uppers";
const char *NUMBERS_FLAG = "--numbers";
const char *SYMBOLS_FLAG = "--symbols";

// Define the allowed symbols to use
const char *SYMBOLS = "+-*!#$&./<:=_>@[]{}()";

void show_usage(const char *);
int parse_input(char *[], int, int *, int *, int *);
char *generate_password(int, int, int, int);

// ---------------------------------------------------------------------------------------------------------------------

int main(int argc, char *argv[]) {
	if (argc < 2) {
		printf("[ERROR] At least one argument is required\n\n");
		show_usage(argv[0]);
		return 1;
	}

	int uppers_enabled = 0, numbers_enabled = 0, symbols_enabled = 0;
	int length = parse_input(argv, argc, &uppers_enabled, &numbers_enabled, &symbols_enabled);

	srand(time(NULL));
	char *password = generate_password(length, uppers_enabled, numbers_enabled, symbols_enabled);
	printf("Password: %s\n", password);

	free(password);
}

// ---------------------------------------------------------------------------------------------------------------------

void show_usage(const char *executable_name) {
	printf(("USAGE: %s [OPTIONS]\n"
			"OPTIONS:\n"
			" %-10s <num>   determines the length of the password. <num> in range [%d, %d] (default: %d)\n"
			" %-10s         determines if uppercase letters must be included (default: disabled)\n"
			" %-10s         determines if numbers must be included (default: disabled)\n"
			" %-10s         determines if symbols must be included (default: disabled)\n"),
		   executable_name, LENGTH_FLAG, MIN_LENGTH, MAX_LENGTH, MIN_LENGTH, UPPERS_FLAG, NUMBERS_FLAG, SYMBOLS_FLAG);
}

int parse_input(char *args[], int num_args, int *out_uppers, int *out_numbers, int *out_symbols) {
	int length = 0;
	for (int i = 0; i < num_args; ++i) {
		length |= (i < num_args - 1) && strcmp(args[i], LENGTH_FLAG) == 0 ? atoi(args[++i]) : 0;
		*out_uppers |= (strcmp(args[i], UPPERS_FLAG) == 0);
		*out_numbers |= (strcmp(args[i], NUMBERS_FLAG) == 0);
		*out_symbols |= (strcmp(args[i], SYMBOLS_FLAG) == 0);
	}
	// ensuring the length is always between [MIN_LENGTH, MAX_LENGTH]
	// if the entered length is lower than MIN_LENGTH then MIN_LENGTH will be used
	// if the entered length is greater than MAX_LENGTH then MAX_LENGTH will be used
	return MIN(MAX(length, MIN_LENGTH), MAX_LENGTH);
}

int generate_random(int min, int max) {
	return min + (rand() % (max - min + 1));
}

void shuffle_array(char *arr, int length) {
	for (int i = 0; i < length; ++i) {
		int random_index = generate_random(0, length - 1);
		int aux = arr[i];
		arr[i] = arr[random_index];
		arr[random_index] = aux;
	}
}

char *generate_password(int length, int uppers_enabled, int numbers_enabled, int symbols_enabled) {
	char *password = malloc(sizeof(char) * (length + 1));  // +1 for the null character '\0' at the end

	// we will ensure all the enabled options are used
	// means if symbols is enabled, password always will contain at least one symbol
	int uppers_limit = uppers_enabled ? generate_random(1, length - 3) : 0;
	int numbers_limit = numbers_enabled ? generate_random(uppers_limit + 1, length - 2) : uppers_limit;
	int symbols_limit = symbols_enabled ? generate_random(numbers_limit + 1, length - 1) : numbers_limit;

	int current_length = 0;
	while (current_length < uppers_limit)
		password[current_length++] = generate_random('A', 'Z');
	while (current_length < numbers_limit)
		password[current_length++] = generate_random('0', '9');
	while (current_length < symbols_limit)
		password[current_length++] = SYMBOLS[generate_random(0, strlen(SYMBOLS) - 1)];
	while (current_length < length)
		password[current_length++] = generate_random('a', 'z');

	shuffle_array(password, length);

	password[length] = '\0';
	return password;
}
