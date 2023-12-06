fun main() {

    /*
    * Reto #30 24/07/2023 EL TECLADO T9
    *
    * Los primeros dispositivos móviles tenían un teclado llamado T9
    * con el que se podía escribir texto utilizando únicamente su
    * teclado numérico (del 0 al 9).
    *
    * Crea una función que transforme las pulsaciones del T9 a su
    * representación con letras.
    * - Debes buscar cuál era su correspondencia original.
    * - Cada bloque de pulsaciones va separado por un guión.
    * - Si un bloque tiene más de un número, debe ser siempre el mismo.
    * - Ejemplo:
    *     Entrada: 6-666-88-777-33-3-33-888
    *     Salida: MOUREDEV
    *
    *   1 .,?!  2 ABC   3 DEF
    *   4 GHI   5 JKL   6 MNO
    *   7 PRS   8 TUV   9 WXYZ
    *
    */

    var input = "6-666-88-777-33-3-33-888"
    println( "${input} => ${t9InputToString(input)}")

    print("Introduce entrada >")
    input = readLine().toString()
    println( "${input} => ${t9InputToString(input)}")

}

fun t9InputToString(input : String):String{
    val listaPulsaciones = input.split('-')
    var resultado = "";
    listaPulsaciones.forEach {
        val letra = t9Transform(it)
        println("$it => $letra" )
        resultado +=  letra
    }

    return resultado;
}

fun t9Transform(bloque:String):Char{
    return  when (bloque) {
        "1" -> '.'
        "11" -> ','
        "111" -> '?'
        "1111" -> '!'

        "2" -> 'A'
        "22" -> 'B'
        "222" -> 'C'

        "3" -> 'D'
        "33" -> 'E'
        "333" -> 'F'

        "4" -> 'G'
        "44" -> 'H'
        "444" -> 'I'

        "5" -> 'J'
        "55" -> 'K'
        "555" -> 'L'

        "6" -> 'M'
        "66" -> 'N'
        "666" -> 'O'

        "7" -> 'P'
        "77" -> 'Q'
        "777" -> 'R'
        "7777" -> 'S'

        "8" -> 'T'
        "88" -> 'U'
        "888" -> 'V'

        "9" -> 'W'
        "99" -> 'X'
        "999" -> 'Y'
        "9999" -> 'Z'

        else -> ' '
    }

}