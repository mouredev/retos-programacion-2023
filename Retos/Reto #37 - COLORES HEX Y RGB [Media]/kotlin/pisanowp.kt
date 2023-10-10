fun main() {

    /*
    * Reto #37 18/09/2023  COLORES HEX Y RGB
    *
    * Crea las funciones capaces de transformar colores HEX
    * a RGB y viceversa.
    * Ejemplos:
    * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
    * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
    *
    * NOTAS: Se usa la función de extension creada en el reto 14 para convertir a hexadecimal
    * pero la pongo aquí de nuevo  para que este a la vista
    * Para convertir de hexadecimal a decimal se usa .toInt poniendo entre parentesis la base en la
    * que esta lo que quiero convetir, en este caso, 16.
    */

    val rgb = "(255,215,0)"
    println("$rgb => ${rgbToHex(rgb)}");

    val hex = "#FF00A3"
    println("$hex => ${hexToRgb(hex)}");

}

fun hexToRgb(hex: String): String {
    var hexDummy = hex
    var rgb = ""

    // Validmos que el color viene en formato Hexademcimal
    val regex = Regex("^#[0-9a-fA-F]{6}$")

    if (regex.matches(hexDummy)) {
        val red = hexDummy.trim('#').substring(0, 2)
        val green = hexDummy.trim('#').substring(2, 4)
        val blue = hexDummy.trim('#').substring(4, 6)

        rgb = "(" + red.toInt(16).toString() + "," + green.toInt(16).toString() + "," + blue.toInt(16).toString() + ")"

    } else {
        println("ERROR $hexDummy NO ES UN COLOR HEXADICMAL VÁLIDO PARA CONVERTIR A RGB")

    }

    return rgb
}

fun rgbToHex(rgb: String): String {
    var rgbDummy = rgb
    var hex = "#"

    // Validamos que el color viene en formato RGB
    val regex = Regex("\\(\\d+,\\d+,\\d+\\)")

    if (regex.matches(rgbDummy)) {
        var rgb = rgb
        rgb = rgb.replace('(', ' ').trim()
        rgb = rgb.replace(')', ' ').trim()

        var rgbArray = rgb.split(',')

        // Usamos la función de extension toHexadecimal creada en el reto 14
        rgbArray.forEach { hex += it.toInt().toHexadecimal().padStart(2, '0') }

    } else {
        println("ERROR $rgbDummy NO ES UN COLOR RGB VÁLIDO PARA CONVERTIR A HEXADECIMAL")

    }

    return hex

}


fun Int.toHexadecimal(): String {
    val letras = listOf('A', 'B', 'C', 'D', 'E', 'F')
    var digitoChar : String
    var hexadecimal = ""
    var numero = this
    var resto: Int

    if (this == 0)
        hexadecimal = "0"

    while (numero > 0) {
        resto = numero % 16
        if (resto < 10) {
            digitoChar = resto.toString()
        }
        else {
            digitoChar = letras[resto-10].toString()
        }

        hexadecimal = digitoChar + hexadecimal
        numero /= 16

    }
    return hexadecimal

}
