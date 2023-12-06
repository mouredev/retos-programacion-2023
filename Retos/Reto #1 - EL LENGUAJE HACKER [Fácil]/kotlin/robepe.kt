import java.lang.StringBuilder
import java.util.Scanner

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

/*
 * Variable global de tipo 'mapOf' para definir los valores 'leet' para cada carácter del abecedario 
 * natural y cada número.
 */
val abecedario = mapOf<Char, String>('a' to "4", 'b' to "I3", 'c' to "[", 'd' to ")",
    'e' to "3", 'f' to "|=", 'g' to "&", 'h' to "#", 'i' to "1", 'j' to ",_|", 'k' to ">|",
    'l' to "1", 'm' to "/\\/\\", 'n' to "^/", 'o' to "0", 'p' to "|*", 'q' to "(_,)", 'r' to "I2",
    's' to "5", 't' to "7", 'u' to "(_)", 'v' to "\\/", 'w' to "\\/\\/", 'x' to "><", 'y' to "j",
    'z' to "2", '0' to "o", '1' to "L", '2' to "R", '3' to "E", '4' to "A", '5' to "S", '6' to "b",
    '7' to "T", '8' to "B", '9' to "g",)

/*
 *  Función destinada a traducir un 'String' formado con números/letras naturales
 *  a su versión en lenguaje 'leet'
 * 
 *  @param cadena: 'String' introducido por teclado
 */
fun naturalToLeet(cadena : String) {
    // Instanciamos un objeto 'StringBuilder' para construir la cadena resultante posteriormente
    val sb = StringBuilder()

    // Bucle 'for' para recorrer cada caracter presente en la cadena proporcionada
    for (caracter in cadena){
        // Obtenemos y almacenamos el valor asignado para cada clave presente en la cadena en 'leetChar' (En caso de no existir, retornamos el valor introducido. Ej: 'ñ')
        val leetChar = abecedario.getOrDefault(caracter.toLowerCase(), caracter.toString())
        // Añadimos cada caracter leet obtenido al StringBuilder
        sb.append(leetChar)
    }
    // Imprimimos por pantalla el resultante, convirtiendolo a 'String'
    println(sb.toString())
}

/*
 *  Método de entrada al programa (Método Main)
 */
fun main() {
    do {
        val sc = Scanner(System.`in`)
        println("\nIntroduzca una cadena en lenguaje natural: \n('*' Para finalizar el programa)")
        val cadena = sc.nextLine()
        naturalToLeet(cadena)

    } while (!cadena.equals("*"))
    println("\nHasta la vista :)")
}
