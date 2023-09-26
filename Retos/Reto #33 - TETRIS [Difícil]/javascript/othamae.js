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
 *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
 * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
 * - Debes tener en cuenta los límites de la pantalla de juego.
 */


const readline = require('readline')

function gameTetrisPiece(){ 
    let piece= [
        [1,0,0],
        [1,1,1],
        [0,0,0]
    ]
    let x = 0
    let y = 0
    console.log('Please enter a correct move:') 
    console.log('a: Move left') 
    console.log('d: Move right') 
    console.log('s: Move down') 
    console.log('w: Rotate piece') 
    console.log('')
    printBoard( piece, x, y)   
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    })
   
rl.on('line', (input) => {    
       if (input === 'd'){
           x= moveRight(piece, x, y)
        } else if (input === 'a'){
           x= moveLeft(piece, x, y)
        } else if (input === 's'){
            y= moveDown(piece, x, y)           
        } else if (input === 'w'){
            piece = rotate(piece, x, y)        
        } else {
            console.log('Please enter a correct move: a, d, w, s')
        }              
    }
    )
}


// Print functions
function printTable(table){
    for (let i = 0; i < table.length; i++) {
        console.log(table[i].join(''))
    }
}

function printBoard(piece, x, y){   
    const table = Array.from({ length: row }, () => Array(col).fill(0)) 
    for (let i = 0; i < table.length; i++) {
        for (let j = 0; j < table[i].length; j++) {
            if (table[i][j] === 0){
                table[i][j] = '⬜'
            }
        }
    }
    for (let i = 0; i < piece.length; i++) {
        for (let j = 0; j < piece[i].length; j++) {
            if (piece[i][j] === 1){
                table[y+i][x+j] = '⬛'
            }
        }
    }
    printTable(table)
}

// Game functions
const row = 10
const col= 10
const table = Array.from({ length: row }, () => Array(col).fill(0)) 

function moveRight( piece, x, y){   
    canMoveToRight(piece, table, x, y) 
    ? x++
    :!isInLastColumn(piece) && hasLastColumnEmpty(piece, table, x, y) && x++ 
    printBoard( piece, x, y)
    return x
}

function moveLeft( piece, x, y){
    canMoveToLeft(table, x, y) 
    ?x-- 
    :!isInFirstColumn(piece) && x===0 && x--
    printBoard( piece, x, y)
    return x
}

function moveDown(piece, x, y) {
    const table = Array.from({ length: row }, () => Array(col).fill(0))
    canMoveDown(piece, table, x, y) 
    ? y++
    : hasLastRowEmpty(piece) && y++
    printBoard( piece, x, y)    
    return isInLastRow(piece, table, y) ? (console.log('Piece already on the bottom'), process.exit(0)) : y
   
}

function rotate(piece, x, y){
    return !canRotate(piece, table, x, y) ? (printBoard(piece, x, y), piece) : (printBoard(pieceRotated(piece), x, y), pieceRotated(piece))    
}

// Helper functions
function canMoveToRight(piece, table, x, y){
    return (x< table[y].length - piece.length) && (table[y][x+1] === 0)
}

function isInLastColumn(piece ){
    for (let i = 0; i < piece.length; i++) {
        if (piece[i][piece.length-1] === 1){
             return true  
        }        
    }
    return false
}

function canMoveToLeft(table, x, y){
    return (x> 0) && (table[x-1][y] === 0)
}

function hasLastColumnEmpty(piece, table,x , y){
    return (x === table[y].length - piece.length)
}

function isInFirstColumn(piece){
    for (let i = 0; i < piece.length; i++) {
        if (piece[i][0] === 1){
            return true
        }        
    }
    return false
}

function canMoveDown(piece, table, x, y){
    return (y < table.length - piece.length) && ((table[y + piece.length][x] === 0) || (x===-1))
}

function hasLastRowEmpty(piece){    
    for (let i = 0; i < piece[0].length; i++) {
        if (piece[piece.length - 1][i] === 1) {
            return false
        }
    }
    return true
}

function isInLastRow(piece, table, y){
   return (hasLastRowEmpty(piece) && (y > table.length - piece.length)) || (!hasLastRowEmpty(piece) && (y === table.length - piece.length))
}

function canRotate(piece, table, x, y){
    return !(x > (table.length )- piece.length || y > (table.length) -piece.length|| x < 0 || y < 0)
}

function pieceRotated(piece){
    let rotatePiece = []
    const size = piece.length
    for (let i = 0; i < size; i++) {
       rotatePiece.push([])
       for (let j = 0; j < size; j++) {
        rotatePiece[i].push(piece[size-1-j][i])
       }
    }
    return rotatePiece
}

// Start
gameTetrisPiece()