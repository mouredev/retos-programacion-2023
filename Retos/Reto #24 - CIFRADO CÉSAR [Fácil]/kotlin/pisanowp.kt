fun main() {

    /*
    *
    * Reto #25 12/06/2023 CIFRADO CÉSAR
    *
    * Crea un programa que realize el cifrado César de un texto y lo imprima.
    * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
    *
    * Te recomiendo que busques información para conocer en profundidad cómo
    * realizar el cifrado. Esto también forma parte del reto.
    *
    */

    //val frase = "Te recomiendo que busques información para conocer en profundidad cómo realizar el cifrado."

    // Pido opción a realizar (C)ifrar o (D)escifrar
    val opcion = pideOpcion().uppercase()

    // Pido la frase a tratar
    if (opcion == "C") print("Introduce frase a cifrar >")
    else print("Introduce frase a descifrar >")
    val frase = readLine()

    if (frase != null){
        // Creo mi "máquina" de cifrado, por defecto desplazamiento de 3
        var enigma = CifradoCesar()
        var resultado = ""

        if (opcion == "C") resultado = enigma.cifra(frase)
        else resultado = enigma.descifra(frase)

        println(resultado)

    }

}



class  CifradoCesar(var desplazamiento: Int = 3){

    fun cifra(frase:String): String {
        var dummy = ""
        frase.forEach {
            dummy  += cifraLetra(it.toChar())
        }
        return dummy
    }

    fun descifra(frase:String): String{
        var dummy = ""
        frase.forEach {
            dummy  += desCifraLetra(it.toChar())
        }
        return dummy

    }



    private fun cifraLetra(letra:Char):Char {
        val code = letra.code
        var newcode = code

        newcode += desplazamiento
        if ((letra.code in 97..122)
            && (newcode > 122)
        ) {
            newcode = (newcode % 122) + 97

        } else if ((letra.code in 65..90)
            && (newcode > 90)
        ) {
            newcode = (newcode % 90) + 65
        }

        return newcode.toChar()

    }

    private fun desCifraLetra(letra:Char):Char {
        val code = letra.code
        var newcode = code

        newcode -= desplazamiento
        if ((letra.code in 97..122)
            && (newcode < 97)
        ) {
            newcode = (122 - (97-newcode) )

        } else if ((letra.code in 65..90)
            && (newcode < 65)
        ) {
            newcode = (90 - (newcode-65))
        }

        return newcode.toChar()

    }

}



fun pideOpcion(): String {
    var input: String? = null
    var valido = false
    while (!valido) {
        print("¿Qué operación quieres hacer (C)ifrar o (D)escifrar? >")
        input = readLine()
        if (input in listOf("c", "C", "d", "D")){
            valido = true
        } else {
            println("Opción inválida.")
        }
    }

    return input!!
}