/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
 */

class tennisGame {
    private score: string;

    constructor() {
        this.score = 'Love - Love';
    }

    public getScore(): string {
        return this.score;
    }

    public resetScore(): void {
        this.score = 'Love - Love';
    }

    public setScore(playerWin: string): void {
        const scorePlayer1: string = this.score.split(' - ')[0];
        const scorePlayer2: string = this.score.split(' - ')[1];
        if (playerWin == 'P1') {
            switch (scorePlayer1) {
                case 'Love':
                    this.score = '15 - ' + scorePlayer2;
                    break;
                case '15':
                    this.score = '30 - ' + scorePlayer2;
                    break;
                case '30':
                    this.score = '40 - ' + scorePlayer2;
                    break;
                case '40':
                    if (scorePlayer2 == '40') {
                        this.score = 'Deuce';
                    } else if (scorePlayer2 == 'Deuce') {
                        this.score = 'Ventaja P1';
                    } else {
                        this.score = 'Ha ganado el P1';
                    }
                    break;
                case 'Deuce':
                    this.score = 'Ventaja P1';
                    break;
                case 'Ventaja P1':
                    this.score = 'Ha ganado el P1';
                    break;
                default:
                    break;
            }
        } else if (playerWin == 'P2') {
            switch (scorePlayer2) {
                case 'Love':
                    this.score = scorePlayer1 + ' - 15';
                    break;
                case '15':
                    this.score = scorePlayer1 + ' - 30';
                    break;
                case '30':
                    this.score = scorePlayer1 + ' - 40';
                    break;
                case '40':
                    if (scorePlayer1 == '40') {
                        this.score = 'Deuce';
                    } else if (scorePlayer1 == 'Deuce') {
                        this.score = 'Ventaja P2';
                    } else {
                        this.score = 'Ha ganado el P2';
                    }
                    break;
                case 'Deuce':
                    this.score = 'Ventaja P2';
                    break;
                case 'Ventaja P2':
                    this.score = 'Ha ganado el P2';
                    break;
                default:
                    break;
            }
        }
    }
}

// pruebas
const game = new tennisGame();
console.log(game.getScore());
game.setScore('P1');
console.log(game.getScore());
game.setScore('P1');
console.log(game.getScore());
game.setScore('P2');
console.log(game.getScore());
game.setScore('P2');
console.log(game.getScore());
game.setScore('P1');
console.log(game.getScore());
game.setScore('P2');
console.log(game.getScore());
game.setScore('P1');
console.log(game.getScore());
game.setScore('P1');
console.log(game.getScore());
game.setScore('P1');
console.log(game.getScore());
game.resetScore();
console.log(game.getScore());
