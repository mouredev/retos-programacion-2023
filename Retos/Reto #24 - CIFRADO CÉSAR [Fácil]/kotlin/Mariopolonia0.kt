package EjercicioKotlin.Mouredev

/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 *
 * use el ROT13 para la codificacion
 */
// 

fun main() {
    //¿Cómo se puede distinguir a un extrovertido de un introvertido en la NSA? Ra ybf nfprafberf, ry rkgebiregvqb zven ybf mncngbf qr ybf BGEBF gvcbf.
    Cifrar().code("Cómo se puede distinguir a un extrovertido de un introvertido en la NSA?")
    Cifrar().decipher("Ra ybf nfprafberf, ry rkgebiregvqb zven ybf mncngbf qr ybf BGEBF gvcbf")
}

class Cifrar() {

    fun decipher(texto: String) {
        var cifrado = ""
        texto.map {
            var codigo = it.code

            if (codigo >= 65 && codigo <= 90) {
                for (it in 1..13) {
                    codigo--

                    if (codigo < 65) {
                        codigo = 90
                    }
                }
            } else if (codigo >= 97 && codigo <= 122) {
                for (it in 1..13) {
                    codigo--

                    if (codigo < 97) {
                        codigo = 122
                    }
                }
            }

            cifrado += Char(codigo)
        }
        println(cifrado)
    }

    fun code(texto: String) {

        var cifrado = ""
        texto.map {
            var codigo = it.code

            if (codigo >= 65 && codigo <= 90) {
                for (it in 1..13) {
                    codigo++

                    if (codigo > 90) {
                        codigo = 65
                    }
                }
            } else if (codigo >= 97 && codigo <= 122) {
                for (it in 1..13) {
                    codigo++

                    if (codigo > 122) {
                        codigo = 97
                    }
                }
            }

            cifrado += Char(codigo)
        }
        println(cifrado)
    }
}
