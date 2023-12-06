package EjercicioKotlin.Mouredev

fun main() {
    reto9("centrifugado")
    reto9("acondicionar")
    reto9("Un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol")
}

private fun reto9(palabra: String) {
    if (esHeterograma(palabra))
        print("es heterograma")
    else
        print("\nes isograma")

    if (esPangrama(palabra))
        print(" es pangrama")
}

private fun esPangrama(palabra: String): Boolean {

    for (item in 'a'..'z') {
        var encotrada = false
        palabra.map {
            if (item == it)
                encotrada = true
        }

        if (!encotrada) {
            return false
        }

    }
    return true
}

private fun esHeterograma(palabra: String): Boolean {

    for (item in 0..palabra.length - 1) {
        for (itemDos in 0..palabra.length - 1) {
            if (palabra[item] == palabra[itemDos] && item != itemDos) {
                return false
            }
        }
    }

    return true
}
