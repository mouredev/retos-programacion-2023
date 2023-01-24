/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

import java.util.*

fun main(){
    val scanner = Scanner(System.`in`)
    print("Ingresa una palabra: ")
    val word = scanner.nextLine()

    val leetWord = toLeet(word)
    println("La palabra en lenguaje leet es: $leetWord")

}

fun toLeet(word: String): String {
    val leet = word.replace('a', '4')
        .replace("b", "I3")
        .replace('c', '[')
        .replace('d', ')')
        .replace('e', '3')
        .replace("f", "|=")
        .replace('g', '&')
        .replace('h', '#')
        .replace('i', '1')
        .replace("j", ",_|")
        .replace("k", ">|")
        .replace('l', '1')
        .replace("m", "/\\/\\")
        .replace("n", "^/")
        .replace('o', '0')
        .replace("p", "|*")
        .replace("q", "(_,)")
        .replace("r", "I2")
        .replace('s', '5')
        .replace('t', '7')
        .replace("u", "(_)")
        .replace("v", "\\/")
        .replace("w", "\\/\\/")
        .replace("x", "><")
        .replace('y', 'j')
        .replace('z', '2')
        .replace('1','L')
        .replace('2', 'R')
        .replace('3', 'E')
        .replace('4', 'A')
        .replace('5', 'S')
        .replace('6', 'b')
        .replace('7', 'T')
        .replace('8', 'B')
        .replace('9', 'g')
        .replace('0', 'o')

    return leet
}

