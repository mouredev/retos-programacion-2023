package com.cursosant.android.retosprogramacion2223

import androidx.core.text.isDigitsOnly
import kotlin.system.exitProcess

fun main(){
    println("Bienvenidos al fantástico generado de contraseñas MourePass.")
    println("------------------------------------------------------------")
    println("A continuación vas poder configurar la complejidad de la contraseña respondiendo cuatro preguntas")
    println("Cuando acabes se te mostrará la contraseña generada por la consola")
    println("Para salir del programa puedes pulsar la tecla 'Q'")
    println("------------------------------------------------------------")


    var sizePassword = validateLenPassword()
    exitProgram(sizePassword)


    var upperPassword = validateUpperPassword()
    exitProgram(upperPassword)

    var numberPassword = validateNumberPassword()
    exitProgram(numberPassword)


    var symbolPassword = validateSymbolPassword()
    exitProgram(symbolPassword)

    generatePassword(sizePassword.toInt(), upperPassword, numberPassword, symbolPassword)



}
fun exitProgram(letter:String){
    if (letter == "q"){
        println("Bye bye")
        exitProcess(0)
    }

}

fun validateLenPassword ():String{
    var sizePassword = ""
    do {
        println("Indica la longitud del password (8-16):")
        sizePassword = readln().lowercase()
    }while ((!sizePassword.toString().all { it in '0'..'9' } && sizePassword != "q") || sizePassword.toInt() !in 8..16)

    return  sizePassword
}

fun validateUpperPassword():String{
    var upPassword = ""

    do {
        println("¿Contiene letras mayúsculas? ( S/N ):")
        upPassword = readln().lowercase()
    }while (upPassword != "q" && upPassword != "s" && upPassword != "n")

    return  upPassword

}

fun validateNumberPassword():String{
    var numPassword = ""

    do {
        println("¿Contiene números? ( S/N ):")
        numPassword = readln().lowercase()
    }while (numPassword != "q" && numPassword != "s" && numPassword != "n")

    return  numPassword

}

fun validateSymbolPassword():String{
    var symPassword = ""

    do {
        println("¿Contiene simbolos? ( S/N ):")
        symPassword = readln().lowercase()
    }while (symPassword != "q" && symPassword != "s" && symPassword != "n")

    return  symPassword

}

fun generatePassword(sizePassword: Int, upperPassword: Any, numberPassword: Any, symbolPassword: Any) {

    var charset = "abcdefghijklmnopqrstuvwxyz"
    if (upperPassword == "s"){
        charset += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    }
    if (numberPassword == "s"){
        charset +=  "0123456789"
    }
    if (symbolPassword == "s"){
        charset +=  "#@!?<>._*+-"
    }
    var pwd = ""
    for (n in 1..sizePassword){
        pwd += charset.random()
    }
    println(pwd)
}
