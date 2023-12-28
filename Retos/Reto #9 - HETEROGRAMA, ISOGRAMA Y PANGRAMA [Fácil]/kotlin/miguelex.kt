private fun removeDiacritics(cadena: String): String {
        val diacriticos =
                        mapOf(
                                        'á' to 'a',
                                        'é' to 'e',
                                        'í' to 'i',
                                        'ó' to 'o',
                                        'ú' to 'u',
                                        'à' to 'a',
                                        'è' to 'e',
                                        'ì' to 'i',
                                        'ò' to 'o',
                                        'ù' to 'u',
                                        'ä' to 'a',
                                        'ë' to 'e',
                                        'ï' to 'i',
                                        'ö' to 'o',
                                        'ü' to 'u',
                                        'â' to 'a',
                                        'ê' to 'e',
                                        'î' to 'i',
                                        'ô' to 'o',
                                        'û' to 'u',
                                        'ã' to 'a',
                                        'ñ' to 'n',
                                        'õ' to 'o',
                                        'ç' to 'c'
                        )

        var cadenaSinDiacriticos = ""
        for (caracter in cadena) {
                if (caracter in diacriticos) {
                        cadenaSinDiacriticos += diacriticos[caracter]
                } else {
                        cadenaSinDiacriticos += caracter
                }
        }

        return cadenaSinDiacriticos
}

private fun isHeterogram(cadena: String): Boolean {
        return cadena.length == cadena.toSet().size &&
                        cadena.length == removeDiacritics(cadena).length
}

private fun isIsogram(cadena: String): Boolean {
        val letrasVistas = mutableSetOf<Char>()
        for (letra in removeDiacritics(cadena)) {
                if (letra in letrasVistas) {
                        return false
                }
                letrasVistas.add(letra)
        }
        return true
}

private fun isPangram(cadena: String): Boolean {
        val alfabeto = mutableSetOf<Char>()
        for (letra in 'a'..'z') {
                alfabeto.add(letra)
        }

        val cadenaSinDiacriticos = removeDiacritics(cadena.toLowerCase())
        for (letra in cadenaSinDiacriticos) {
                if (letra in alfabeto) {
                        alfabeto.remove(letra)
                }
                if (alfabeto.isEmpty()) {
                        return true
                }
        }
        return false
}

fun main() {
        val string1 = "murcielago"
        val string2 = "esdrújula"
        val string3 =
                        "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja"

        println(isHeterogram(string1)) // true
        println(isHeterogram(string2)) // false
        println(isIsogram(string1)) // true
        println(isIsogram(string2)) // false
        println(isPangram(string3)) // true
}
