fun main() {
    val number = 15
    decimalToOctal(number)
    decimalToHexadecimal(number)
}

fun decimalToOctal(num:Int){
    var numero: Int = num
    var octal = ""
    var resto = 0
    while (numero > 0){
        resto = numero%8
        octal = "$resto$octal"
    	numero -= resto
        numero /= 8
    }
    println("El número en decimal $num es $octal en octal.")
}

fun decimalToHexadecimal(num:Int){
    var numero: Int = num
    var hexadecimal = ""
    var resto = 0
    val valoresEnHexadecimal: List<String> = listOf("A","B","C","D","E","F")
    while (numero > 0){
        resto = numero%16
        if (resto > 9){
            resto -= 10
            val caracterHexadecimal: String = valoresEnHexadecimal.get(resto)
            hexadecimal = "$caracterHexadecimal$hexadecimal"
            resto += 10
        }	else{
            hexadecimal = "$resto$hexadecimal"
        }
    	numero -= resto
        numero /= 16
    }
    println("El número en decimal $num es $hexadecimal en hexadecimal.")
}