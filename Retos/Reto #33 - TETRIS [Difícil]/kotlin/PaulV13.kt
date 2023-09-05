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

fun main(){
    val board = Array(10){
        Array(10) { "\uD83D\uDD32" }
    }
    var rowStart = 0
    var colStart = 0
    var rotation = 0
    var limitColumn = 0
    var limitRow = 0
    var horizontal = true

    createBoard(board,rowStart,colStart,rotation)
    println()

    println("-------Movements--------")
    println("Left: a")
    println("Down: s")
    println("Right: d")
    println("Rotate: r")
    println("Exit: e")
    println("---------------")

    while (true){
        println("Insert a movement: ")
        val movement = readlnOrNull()

        if(movement == "e"){
            println("Game finished!!!")
            return
        }
        else if(movement == "r"){
            horizontal = !horizontal
            rotation += 1

            if(rotation == 4) rotation = 0

            when (rotation) {
                0 -> {
                    if(limitColumn == 8) colStart = 7
                    limitColumn = colStart
                    limitRow = rowStart
                }
                1 -> {
                    if(limitRow == 8) rowStart = 7
                    limitColumn = colStart+1
                    limitRow = rowStart
                }
                2 -> {
                    if(limitColumn == 0) colStart = 0
                    limitColumn = colStart
                    limitRow = rowStart+1
                }
                3 -> {
                    limitColumn = colStart
                    limitRow = rowStart
                }
            }
            createBoard(board, rowStart, colStart, rotation)
        }
        else if(movement == "s"){
            if(horizontal){
                if(limitRow in 0..7){
                    rowStart += 1
                    createBoard(board, rowStart,colStart,rotation)
                    limitRow += 1
                    if(limitRow == 8) {
                        println()
                        println("Game finished!!!")
                        return
                    }
                }
            }
            else{
                if(limitRow in 0..6){
                    rowStart += 1
                    createBoard(board, rowStart,colStart,rotation)
                    limitRow += 1
                    if(limitRow == 7) {
                        println()
                        println("Game finished!!!")
                        return
                    }
                }
            }
        }
        else if(movement == "d"){
            if(horizontal){
                if(limitColumn in 0..6){
                    colStart += 1
                    createBoard(board, rowStart,colStart,rotation)
                    limitColumn += 1
                }
            }
            else{
                if(limitColumn in 0..7){
                    colStart += 1
                    createBoard(board, rowStart,colStart,rotation)
                    limitColumn += 1
                }
            }
        }
        else if(movement == "a"){
            if(horizontal){
                if(limitColumn in 1..7){
                    colStart -= 1
                    createBoard(board, rowStart,colStart,rotation)
                    limitColumn -= 1
                }
            }
            else{
                if(limitColumn in 1..8){
                    colStart -= 1
                    createBoard(board, rowStart,colStart,rotation)
                    limitColumn -= 1
                }
            }
        }
    }
}

fun createBoard(board: Array<Array<String>>, rowStart: Int, columnStart: Int, rotation: Int){
    board.forEachIndexed { indexRow, row ->
        row.forEachIndexed { indexCol, col ->
            when(rotation){
                0 -> {
                    if(indexRow == rowStart+1 && indexCol >= columnStart && indexCol <= columnStart+2 || indexRow == rowStart && indexCol == columnStart){
                        print("\uD83D\uDD33")
                    } else print(col)
                }
                1 -> {
                    if(indexCol == columnStart+1 && indexRow >= rowStart && indexRow <= rowStart+2 || indexRow == rowStart && indexCol == columnStart+2){
                        print("\uD83D\uDD33")
                    } else print(col)
                }
                2 -> {
                    if(indexRow == rowStart+1 && indexCol >= columnStart && indexCol <= columnStart+2 || indexRow == rowStart+2 && indexCol == columnStart+2){
                        print("\uD83D\uDD33")
                    } else print(col)
                }
                3 -> {
                    if(indexCol == columnStart+1 && indexRow >= rowStart && indexRow <= rowStart+2 || indexRow == rowStart+2 && indexCol == columnStart){
                        print("\uD83D\uDD33")
                    } else print(col)
                }
            }
        }
        println()
    }
}
