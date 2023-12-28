#include <stdio.h>
#include <stdlib.h>

//////////////////////////////////////////////////////////////////////////////////
/// CONSTANTS
/// 
enum {
    MAX_LENGHT = 100 , // Text buffer max lenght                      
};

//////////////////////////////////////////////////////////////////////////////////
/// GAME STRUCT
/// 
typedef struct {
    unsigned short p1;  // Balls won by player 1
    unsigned short p2;  // Balls won by player 2
    unsigned short secuence[MAX_LENGHT]; // Secuence of balls won by each player
    unsigned short points_played;   // Total number of balls played
} T_game;

/// POINTS INCREMENTS
unsigned short increments[3] = { 15, 15, 10 };

//////////////////////////////////////////////////////////////////////////////////
/// INPUT DATA
///     Receives the game secuence given by user and stores it into T_game
///     data structure.
///     A humble error checking is made during procces.
/// INPUT: char* sec -> pointer to string buffer.
/// OUPUT: EXIT_FAILURE (0) if an error detected in data input
///        EXIT_SUCCESS (1) on succes 
///
int input_data(T_game* g) {
    char secuencia[MAX_LENGHT] = {0}; // Buffer for store user input
    size_t i = 0;                     // Index for loops
    unsigned int player = 0;          // Temporary store individual value parsed from buffer
    g->points_played = 0;             // Total number of points played

    // Captures the user input and store into buffer
    printf("Input play secuence (Ej: p1 p2 p1 p1 ...) separated by a space:\n -> ");
    while((secuencia[i] = getchar()) != EOF && secuencia[i] != '\n') { ++i; }

    // Parses the buffer, checking for errors and, if all it's ok, stores the secuence and
    // the number of points played into the game structure
    for(i = 0; i < MAX_LENGHT; i += 3) {
        int result = 0;
        result = sscanf(secuencia+i, " %*c%1u[1-2] ", &player);

        if(result != EOF && result != 0) {
            if(player == 1 || player == 2) {
                // Store game secuence into T_game structure
                g->secuence[g->points_played] = player;
                ++g->points_played;
            } else {
                printf("Player input error.\n");
                return EXIT_FAILURE;
            }
        } else if(result != 1 && result != EOF) {
            printf("Play secuence input error.\n");
            return EXIT_FAILURE;
        }
   }
        if(g->points_played < 4) {
            printf("Insuficient number of points played!\n");
            return EXIT_FAILURE;
        }
 
    return EXIT_SUCCESS;
}

//////////////////////////////////////////////////////////////////////////////////
/// PLAY GAME
///     Simulates the game parsing the game secuence stored into the T_game 
///     structure.
/// INPUT: T_game* g -> pointer to T_game structure
/// OUTPUT: EXIT_SUCCESS if all it's ok
///         EXIT_FAILURE otherwise 
///
int play_game(T_game *g) {
    size_t p1 = 0, p2 = 0; // Offset for points increment

    printf("The game begins!\n P1\t\tP2\n Love\t\tLove\n");

    // Moves through game secuence parsed from player input and calculates
    // the players points
    for(size_t i = 0; i <= g->points_played; ++i) {
        switch (g->secuence[i]) {
            case 1:
                g->p1 += increments[p1];
                p1 < 2 ? ++p1 : p1;
                break;
            case 2:
                g->p2 += increments[p2];
                p2 < 2 ? ++p2 : p2;
                break;
        }

        // Printing results depending on each ball played result
        if((g->p1 >= 40) && (g->p2 >= 40)) {
            if(g->p1 == g->p2) {
                g->p1 = 40;
                g->p2 = 40;
                printf("    DEUCE\n");
            } else if(g->p1 - g->p2 == 10) {
                printf("    Advantage P1\n");
            } else if(g->p2 - g->p1 == 10) {
                printf("    Advantage P2\n");
            } else if(g->p1 - g->p2 > 10) {
                printf("    P1 WIN!!!\n");
                return EXIT_SUCCESS;
            } else if(g->p2 - g->p1 > 10) {
                printf("    P2 WIN!!\n");
                return EXIT_SUCCESS;
            }
        } else if(g->p1 < 50 && g->p2 < 50) {  
            printf("%u\t\t%u\n", g->p1, g->p2); 
        } else if(g->p1 == 50) { 
            printf("    P1 WINS!!!\n"); 
            return EXIT_SUCCESS;
        } else if(g->p2 == 50) {
            printf("    P2 WINS!!!\n");
            return EXIT_SUCCESS;
        }
    } 
    return EXIT_SUCCESS;
}

int main(int argc, char *argv[]) {
    T_game game = {0};

    if(input_data(&game) == EXIT_SUCCESS) { play_game(&game); }
    else EXIT_FAILURE;
    

    return EXIT_SUCCESS;
}
