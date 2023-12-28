/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

fun main() {
    print(generatePassword())
}

private fun generatePassword():String{
    
    var password = ""
    
    for(contador in 1..10){
        
        when(randNumero(1,3)){
            1->{
                password += randletraMinucula()
            }
            2->{
                password += randletraMayuscula()
            }
            3->{
                password += randNumero(1,9)
            }
        }
    }
    
    return password
}

fun randletraMinucula(): Char {
    return ('a'..'z').random()
}

fun randletraMayuscula(): Char {
    return ('A'..'Z').random()
}

fun randNumero(start: Int, end: Int): Int {
    require(start <= end) { "Illegal Argument" }
    return (start..end).random()
}
