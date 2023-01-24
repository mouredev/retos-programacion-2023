/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */


fun main(args: Array<String>) {
    println(RandomPassword().create())
    println(RandomPassword(lenght = 10).create())
}

data class RandomPassword(
    var lenght: Int = 8,
    val hasUpper: Boolean = true,
    val hasNumbers: Boolean = true,
    val hasSimbols: Boolean = true
){
    private val lowers = (97..122)
    private val uppers = (65..90)
    private val numbers = (48..57)
    private val simbols: List<Int> = (33..47) + (58..64) + (91..95)
    private val collection: MutableList<Int> = mutableListOf()


    init{
            if (lenght<8) lenght = 8 else if (lenght > 16) lenght = 16
            collection.addAll(lowers)
            if (hasUpper) collection.addAll(uppers)
            if (hasNumbers) collection.addAll(numbers)
            if (hasSimbols) collection.addAll(simbols)
    }

    fun create(): String = collection
        .shuffled()
        .take(lenght)
        .map { it.toChar() }
        .joinToString ("")

}

