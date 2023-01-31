/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

println("Password con todo: "+generatePassword(16,true,true,true))

println("Password sin mayusculas pero con lo demas: "+generatePassword(16,false,true,true))

println("Password sin numeros pero con lo demas: "+generatePassword(16,true,false,true))

println("Password sin simbolos pero con lo demas: "+generatePassword(16,true,true,false))

println("Password sin nada y 8 caracteres: "+generatePassword(8,false,false,false))


fun generatePassword (howLong: Int, capital: Boolean, numbers: Boolean, symbols: Boolean): String{
    if (howLong < 8 || howLong > 16){
        return "Please enter a number between 8 and 16"
    }

    var password = ""
    var charatersToUse = "abcdefghijklmnopqrstuvwxyz"

    if (capital) charatersToUse += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if (numbers) charatersToUse += "0123456789"
    if (symbols) charatersToUse += "°!\"#$%&/()=?¡¨*"

    for (i in 1..howLong){
        password += charatersToUse.random()
    }

    return password
}