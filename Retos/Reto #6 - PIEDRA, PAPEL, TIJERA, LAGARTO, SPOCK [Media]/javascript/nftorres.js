/* This script shows the solution to the exercise "Reto #6: PIEDRA, PAPEL O TIJERA" from Brais Moure's official website.
 */

/**
 * This class represents a game of 'Piedra, Papel, Tijera, Lagarto, Spock'
 */
class Game {
    /**
     * This method initializes the players' scores and establishes the duels and weak opponents of each player.
     * @param {Array} duels
     */
    constructor(duels) {
        this.duels = duels;
        this.p1_score = 0;
        this.p2_score = 0;

        this.weakOpponents = {
            piedra: ["tijera", "lagarto"],
            papel: ["piedra", "spock"],
            tijera: ["papel", "lagarto"],
            lagarto: ["papel", "spock"],
            spock: ["tijera", "piedra"],
        };
    }

    /**
     * This method checks if the pieces played are valid in the game.
     * @param {String} piece1 piece played by player1
     * @param {String} piece2 piece played by player2
     * @returns Bool
     */
    #checkPieces(piece1, piece2) {
        /* This method checks if the pieces played are valid in the game.

        Args:
            piece1 (str): piece played by player1
            piece2 (str): piece played by player2
        Returns:
            bool: True is returned if the pieces played are valid, othercase, False if returned
        */
        this.piece1 = piece1.toLowerCase();
        this.piece2 = piece2.toLowerCase();

        if (
            this.piece1 in this.weakOpponents &&
            this.piece2 in this.weakOpponents
        ) {
            return true;
        }
        return false;
    }

    /**
     * This method updates the players' scores during the game.
     */
    updateScores() {
        try {
            for (const duel of this.duels) {
                let piece1 = duel[0].toLowerCase();
                let piece2 = duel[1].toLowerCase();
                if (this.#checkPieces(piece1, piece2)) {
                    if (this.weakOpponents[piece1].includes(piece2)) {
                        this.p1_score += 1;
                    } else if (this.weakOpponents[piece2].includes(piece1)) {
                        this.p2_score += 1;
                    } else {
                        this.p1_score += 0;
                        this.p2_score += 0;
                    }
                } else {
                    throw new Error(
                        "Sólo se puede jugar con 'Piedra', 'Papel', 'Tijera', 'Lagarto' o 'Spock'"
                    );
                }
            }
        } catch (error) {
            return "Error: " + error;
        }
    }

    /**
     * This method determines the winner of the game.
     * @returns String
     */
    sayWinner() {
        this.result = new String();
        if (this.p1_score === this.p2_score) {
            this.result = "Tie!";
        } else if (this.p1_score > this.p2_score) {
            this.result = "Player 1 has won!";
        } else {
            this.result = "Player 2 has won!";
        }
        return this.result;
    }
}

// Definiting the duels
duels = [
    ["Piedra", "Papel"],
    ["Tijera", "Papel"],
    ["Piedra", "Tijera"],
    ["Tijera", "Piedra"],
];

var game = new Game(duels);
game.updateScores();
result = game.sayWinner();
console.log("Result: " + result);
