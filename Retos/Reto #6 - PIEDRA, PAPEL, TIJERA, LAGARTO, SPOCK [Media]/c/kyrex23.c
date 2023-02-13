/*
 * # Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
 * #### Dificultad: Media | Publicación: 06/02/23 | Corrección: 13/02/23
 *
 * ## Enunciado
 * Crea un programa que calcule quien gana más partidas al piedra, papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel), "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 * .....................................................................................................................
 * Author: kyrex23
 * Date:   11/02/2023
 *
 * As it can be tedious to manually input the data, I have included a couple of usage examples for running it:
 * (both quoted and unquoted arguments are allowed and invalid inputs are handled)
 * - ./kyrex23 "🗿 📄 ✂️ 🦎 🖖 📄"
 * - ./kyrex23 📄 🦎 🖖 🗿 🖖 ✂️
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum { ERROR = -1, ROCK = 0, PAPER = 1, SCISSORS = 2, LIZARD = 3, SPOCK = 4 } Play;
typedef enum { DRAW = 0, PLAYER_1 = 1, PLAYER_2 = 2 } Winner;

const char *STR_WINNER_TIE = "Tie";
const char *STR_WINNER_PLAYER_1 = "Player 1";
const char *STR_WINNER_PLAYER_2 = "Player 2";

// According to numeric values of Play enum, RULES[i][j] contains the winner between the Play `i` against Play `j`
// ex: RULES[2][4] means who is the winner between: SCISSORS (PLAYER_1) vs SPOCK (PLAYER_2) => PLAYER_2
const Winner RULES[5][5] = {
	{	 DRAW, PLAYER_2, PLAYER_1, PLAYER_1, PLAYER_2},
	{PLAYER_1,	   DRAW, PLAYER_2, PLAYER_2, PLAYER_1},
	{PLAYER_2, PLAYER_1,	 DRAW, PLAYER_1, PLAYER_2},
	{PLAYER_2, PLAYER_1, PLAYER_2,	   DRAW, PLAYER_1},
	{PLAYER_1, PLAYER_2, PLAYER_1, PLAYER_2,	 DRAW}
};

/**
 * Converts a c-string input ({"🗿" "📄" "✂️" "🦎" "🖖"}) into a valid Play enumeration value
 * @param[in] input c-string with the play to convert
 * @return enum value according to the input or ERROR if the input is invalid
 */
Play convert_input(const char *input);

/**
 * Splits a c string into tokens by the space character
 * @param[in] str original c string to split (this string will be modified)
 * @param[out] tokens pointer (pass by reference) to a c-string array where tokens will be stored (should be freed)
 * @return an unsigned integer value with the number of stored tokens
 */
size_t split_string(char str[], char **tokens[]);

/**
 * Parses a c-string array which will contain the following values: {"🗿" "📄" "✂️" "🦎" "🖖"}
 * into another array of enumeration plays {ROCK, PAPER, SCISSORS LIZARD SPOCK}.
 * @brief Any input that doesn't match with some of the allowed plays, won't be included into the generated array
 * @param[in] input c-string array with the plays to parse ("🗿" "📄" "✂️" "🦎" "🖖")
 * @param[in] input_size number of elements to parse in the input array
 * @param[out] output pointer (passed by reference) to a Play array to store the converted plays (should be freed)
 * @return an unsigned integer with the number of parsed elements in the `output` array
 */
size_t parse_input(char *input[], size_t input_size, Play **output);

/**
 * Calculates the winner of the game represented by the passed plays
 * @param plays array of plays played by each player alternatively
 * @param num_plays size of the array
 * @return an enum value with the winner of this game {TIE (if no winner), PLAYER_1, PLAYER_2}
 */
Winner calculate_winner(Play *plays, size_t num_plays);

// ---------------------------------------------------------------------------------------------------------------------

int main(int argc, char *argv[]) {
	if (argc < 2) {
		printf("[ERROR] Missing required argument/s: <plays>\n"
			   "Usage: %s\n",
			   argv[0]);
		return EXIT_FAILURE;
	}

	// the input will always be used as a c-string array so
	// if the input argument is a quoted string (ex: "🗿 📄 ✂️ 🦎 🖖"), it will be split into tokens
	int only_one_argument = (argc == 2);  // this flag is important to know if we have to free memory or not
	char **user_inputs = &argv[1];		  // skip the executable name which is always stored in argv[0]
	size_t num_user_inputs = only_one_argument ? split_string(user_inputs[0], &user_inputs) : argc - 1;

	if (num_user_inputs % 2 == 0) {
		Play *parsed_inputs;
		size_t num_parsed_inputs = parse_input(user_inputs, num_user_inputs, &parsed_inputs);

		Winner winner = calculate_winner(parsed_inputs, num_parsed_inputs);
		printf("The winner is: %s\n", winner == PLAYER_1 ? STR_WINNER_PLAYER_1 :
									  winner == PLAYER_2 ? STR_WINNER_PLAYER_2 :
														   STR_WINNER_TIE);

		if (parsed_inputs) free(parsed_inputs);
	} else printf("[ERROR] The input plays are odd...\n");

	// if only one argument was passed, user_inputs contains a dynamic array -> free it
	if (only_one_argument && user_inputs) {
		for (size_t i = 0; i < num_user_inputs; ++i)
			free(user_inputs[i]);
		free(user_inputs);
	}

	return EXIT_SUCCESS;
}

// ---------------------------------------------------------------------------------------------------------------------

Play convert_input(const char *input) {
	if (strcmp(input, "🗿") == 0) return ROCK;
	if (strcmp(input, "📄") == 0) return PAPER;
	if (strcmp(input, "✂️") == 0) return SCISSORS;
	if (strcmp(input, "🦎") == 0) return LIZARD;
	if (strcmp(input, "🖖") == 0) return SPOCK;
	return ERROR;
}

size_t split_string(char str[], char **tokens[]) {
	size_t num_tokens = 0;

	char **local_tokens = NULL;
	char *token_init = strtok(str, " ");
	while (token_init) {
		local_tokens = realloc(local_tokens, sizeof(char *) * (num_tokens + 1));
		local_tokens[num_tokens] = malloc(sizeof(char) * (strlen(token_init) + 1));
		strcpy(local_tokens[num_tokens++], token_init);
		token_init = strtok(NULL, " ");
	}
	*tokens = local_tokens;	 // In this way, original `tokens` content is discarded (if any)
	return num_tokens;
}

size_t parse_input(char *input[], size_t input_size, Play **output) {
	size_t num_outputs = 0;

	Play *local_output = NULL;
	for (size_t i = 0; i < input_size; ++i) {
		Play current_value = convert_input(input[i]);
		if (current_value != ERROR) {
			local_output = realloc(local_output, sizeof(Play) * (num_outputs + 1));
			local_output[num_outputs++] = current_value;
		}
	}
	*output = local_output;	 // In this way, original `output` content is discarded (if any)
	return num_outputs;
}

Winner calculate_winner(Play *plays, size_t num_plays) {
	int score_player_1 = 0;
	int score_player_2 = 0;

	for (size_t i = 0; i < num_plays; i += 2) {
		Winner current_winner = RULES[plays[i]][plays[i + 1]];
		switch (current_winner) {
			case PLAYER_1: ++score_player_1; break;
			case PLAYER_2: ++score_player_2; break;
		}
	}
	return score_player_1 > score_player_2 ? PLAYER_1 : (score_player_1 < score_player_2) ? PLAYER_2 : DRAW;
}
