fun main() {
    print("Ingresa el texto que deseas transformar al lenguaje leet: ")
    val texto = readLine()
    println("texto ingresado: $texto")
    val lenguajeLeet = lenguajeHacker(texto)
    println("texto transformado al lenguaje leet: $lenguajeLeet")
}

private fun lenguajeHacker(text: String): String {
    return text.map {
        when (it) {
            'a', 'A' -> "4"
            'b', 'B' -> "I3"
            'c', 'C' -> "["
            'd', 'D' -> ")"
            'e', 'E' -> "3"
            'f', 'F' -> "|="
            'g', 'G' -> "&"
            'h', 'H' -> "#"
            'i', 'I' -> "1"
            'j', 'J' -> ",_|"
            'k', 'K' -> ">|"
            'l', 'L' -> "1"
            'm', 'M' -> "/\\/\\"
            'n', 'N' -> "^/"
            'o', 'O' -> "0"
            'p', 'P' -> "|*"
            'q', 'Q' -> "(_,)"
            'r', 'R' -> "I2"
            's', 'S' -> "5"
            't', 'T' -> "7"
            'u', 'U' -> "(_)"
            'v', 'V' -> "\\/"
            'w', 'W' -> "\\/\\/"
            'x', 'X' -> "><"
            'y', 'Y' -> "j"
            'z', 'Z' -> "2"
            '0' -> "o"
            '1' -> "L"
            '2' -> "R"
            '3' -> "E"
            '4' -> "A"
            '5' -> "S"
            '6' -> "b"
            '7' -> "T"
            '8' -> "B"
            '9' -> "g"
            else -> it
        }
    }.joinToString("")
}
