/*
 * Crea un programa capaz de gestionar una pieza de Tetris.
 * - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
 * - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
 *   🔳
 *   🔳🔳🔳
 * - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
 *   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 * - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
 *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla de juego.
 * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
 * - Debes tener en cuenta los límites de la pantalla de juego.
 */

const readline = require('readline');

class Tetris {
    constructor(rows, cols) {
        // Board settings
        this.rows = rows;
        this.cols = cols;

        // Piece's information
        this.piece = [
            [1, 0, 0],
            [1, 1, 1],
        ];
        this.pieceWidth = this.piece[0].length;
        this.pieceHeight = this.piece.length;

        // Piece's position
        this.x = 0;
        this.y = 0;
    }

    printOptions() {
        console.log('\nEnter an option:');
        console.log(' - A: Move left');
        console.log(' - D: Move right');
        console.log(' - S: Move down');
        console.log(' - W: Rotate piece');
        console.log(' - ESC: Exit\n');
    }

    printBoard(piece = this.piece) {
        this.board = Array.from({ length: this.rows }, () => Array(this.cols).fill(0));
        
        const createBoard = () => {
            // Initialize the board
            for (let i = 0; i < this.board.length; i++) {
                for (let j = 0; j < this.board[i].length; j++) {
                    if (this.board[i][j] === 0) {
                        this.board[i][j] = '🔲';
                    }
                }
            }

            // Print the piece
            for (let i = 0; i < piece.length; i++) {
                for (let j = 0; j < piece[i].length; j++) {
                    if (piece[i][j] === 1) {
                        this.board[this.y+i][this.x+j] = '🔳';
                    }
                }
            }
        }

        createBoard();

        for (let i = 0; i < this.board.length; i++) {
            console.log(this.board[i].join(''));
        }
    }

    // Piece's movements

    moveLeft() {
        const canMove = this.x - 1 >= 0;
        
        if (canMove) {
            this.x--;
        } else {
            console.log('You\'ve reached left limit.');
        }
    }

    moveRight() {
        const canMove = this.x + 1 + this.pieceWidth <= this.cols;
    
        if (canMove) {
            this.x++;
        } else {
            console.log('You\'ve reached rigth limit.');
        }
    }

    moveDown() {
        const canMove = this.y + 1 + this.pieceHeight <= this.rows;

        if (canMove) {
            this.y++;
        } else {
            console.log('You\'ve reached down limit.');
        }
    }

    turnPiece() {
        const rotate90Degrees = (piece) => {
            return piece[0].map((_, idx) => piece.map(row => row[idx]).reverse());
        }

        // Check if piece can be turned
        if (
            (this.pieceWidth > this.pieceHeight && this.y + this.pieceWidth <= this.rows) ||
            (this.pieceHeight > this.pieceWidth && this.x + this.pieceHeight <= this.cols) ||
            (this.pieceWidth === this.pieceHeight)
        ) {
            this.piece = rotate90Degrees([...this.piece]);
            // Update piece's dimension
            this.pieceWidth = this.piece[0].length;
            this.pieceHeight = this.piece.length;
        } else {
            console.log('Piece\'s dimension doesn\'t allow turning this piece.');
        }
    }
}


const tetris = new Tetris(10, 10);

readline.emitKeypressEvents(process.stdin);

if (process.stdin.isTTY) {
    process.stdin.setRawMode(true);
}

// Print the options and initialized board
tetris.printOptions();
tetris.printBoard();

// Manage user's actions
process.stdin.on('keypress', (_, key) => {
    tetris.printOptions();

    if (key && key.name === 'escape') {
        process.exit();
    }

    if (key.name === 'a') {
        tetris.moveLeft();
    } else if (key.name === 'd') {
        tetris.moveRight();
    } else if (key.name === 's') {
        tetris.moveDown();
    } else if (key.name === 'w') {
        tetris.turnPiece();
    } else {
        console.log('\nERROR: not a valid key pressed!');
        printOptions();
    }

    tetris.printBoard();

    if (tetris.y + tetris.pieceHeight === tetris.rows) {
        process.exit();
    }
});