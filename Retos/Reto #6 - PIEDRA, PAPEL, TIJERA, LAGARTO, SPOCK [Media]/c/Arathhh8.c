/* # Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
#### Dificultad: Media | Publicación: 06/02/23 | Corrección: 13/02/23

## Enunciado

/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

#include <stdio.h>
#include <string.h>

#define MAX_GAMES 100

// Function prototypes
int determine_winner(char player1, char player2);
void evaluate_games(char games[][2], int num_games);

int main(void) {
    // Example input
    char games[MAX_GAMES][2] = {
        {'S', 'R'}, // Rock vs Scissors
        {'S', 'R'}, // Scissors vs Rock
        {'P', 'S'}, // Paper vs Scissors
        {'L', 'P'}, // Lizard vs Paper
        {'V', 'R'}  // Spock vs Rock
    };
    int num_games = 5;

    evaluate_games(games, num_games);

    return 0;
}

// Function to determine the winner of a single game
// R: Rock, P: Paper, S: Scissors, L: Lizard, V: Spock
int determine_winner(char player1, char player2) {
    if (player1 == player2) {
        return 0; // Tie
    }

    switch (player1) {
        case 'R': // Rock
            return (player2 == 'S' || player2 == 'L') ? 1 : 2;
        case 'P': // Paper
            return (player2 == 'R' || player2 == 'V') ? 1 : 2;
        case 'S': // Scissors
            return (player2 == 'P' || player2 == 'L') ? 1 : 2;
        case 'L': // Lizard
            return (player2 == 'P' || player2 == 'V') ? 1 : 2;
        case 'V': // Spock
            return (player2 == 'R' || player2 == 'S') ? 1 : 2;
        default:
            return -1; // Invalid input
    }
}

// Function to evaluate all games and determine the overall winner
void evaluate_games(char games[][2], int num_games) {
    int player1_wins = 0;
    int player2_wins = 0;

    for (int i = 0; i < num_games; i++) {
        int result = determine_winner(games[i][0], games[i][1]);
        if (result == 1) {
            player1_wins++;
        } else if (result == 2) {
            player2_wins++;
        }
    }

    if (player1_wins > player2_wins) {
        printf("Player 1 wins\n");
    } else if (player2_wins > player1_wins) {
        printf("Player 2 wins\n");
    } else {
        printf("Tie\n");
    }
}



