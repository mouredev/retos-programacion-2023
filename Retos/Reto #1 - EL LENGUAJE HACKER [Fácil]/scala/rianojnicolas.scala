/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
*/
object Reto1 extends App {
    val dict_leet = Map[Char, String]('A' -> "4",
        'B' -> "I3", 
        'C' -> "[", 
        'D' -> ")", 
        'E' -> "3", 
        'F' -> "|=", 
        'G' -> "&",
        'H' -> "#",
        'I' -> "1", 
        'J' -> ",_|", 
        'K' -> ">|", 
        'L' -> "1",
        'M' -> "/\\/\\", 
        'N' -> "^/", 
        'O' -> "0", 
        'P' -> "|*", 
        'Q' -> "(_,)", 
        'R' -> "I2", 
        'S' -> "5", 
        'T' -> "7",
        'U' -> "(_)", 
        'V' -> "\\/", 
        'W' -> "\\/\\/", 
        'X' -> "><", 
        'Y' -> "j", 
        'Z' -> "2",
        '1' -> "L", 
        '2' -> "R", 
        '3' -> "E", 
        '4' -> "A", 
        '5' -> "S", 
        '6' -> "b", 
        '7' -> "T", 
        '8' -> "B",
        '9' -> "g", 
        '0' -> "o"
    )

    println("Ingresa una frase o texto: ")
    val input_1  = scala.io.StdIn.readLine()
    val input_mayus = input_1.toUpperCase()
    val outputMod = input_mayus
        .map {char => dict_leet.getOrElse(char, char)}
        .mkString
    println("Tu frase codificada es: ")
    println(outputMod)
}