/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

/**
 * Funcion Principal
 */
fun main(){

    println(generatePassword(12, upperCase = true, numbers = true, symbols = true))
    println(generatePassword(10, upperCase = true, numbers = false, symbols = true))
    println(generatePassword(8, upperCase = false, numbers = true, symbols = false))
    println(generatePassword(20, upperCase = false, numbers = false, symbols = true))
    println(generatePassword(9, upperCase = false, numbers = false, symbols = true))

}

/**
 * Genera una contraseña aleatoria con los parámetros indicados.
 * @param length Longitud de la contraseña. Por defecto 12.
 * @param upperCase Indica si la contraseña debe contener letras mayúsculas. Por defecto true.
 * @param numbers Indica si la contraseña debe contener números. Por defecto true.
 * @param symbols Indica si la contraseña debe contener símbolos. Por defecto true.
 */

fun generatePassword(length: Int, upperCase: Boolean= true , numbers: Boolean = true , symbols: Boolean = true): String {

    if(length < 8 || length > 16){
        return "La longitud de la contraseña debe estar entre 8 y 16 caracteres"
    }

    val password = StringBuilder()


    var charPool:List<Char> = ('a'..'z').toList()


    if(upperCase){
        charPool = charPool.plus(('A'..'Z'))
    }

    if(numbers){
        charPool=charPool.plus('0'..'9')
    }

    if(symbols){
       charPool=charPool.plus('!'..'@')
    }


    for (i in 1..length) {
        val randomNum = (Math.random() * charPool.size).toInt()
        password.append(charPool[randomNum])
    }


    return password.toString()


}


main()