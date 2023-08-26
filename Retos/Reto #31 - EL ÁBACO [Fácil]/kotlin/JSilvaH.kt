fun main() {
    print("Ingresa un numero: ")
    val number = readln()
    if (number.toInt() <= 9999999) {
        val ar = arrayListOf<String>()
        var result = number.toInt()
        while (result > 0) {
            val mod = result.mod(10)
            result = result.div(10)
            ar.add(returnValue(mod))
        }
        val rest = 7 - ar.size
        repeat(rest) {
            ar.add("---000000000")
        }
        ar.reverse()
        println(ar)
    } else {
        println("No se puede trabajar con mas digitos")
    }
}

fun returnValue(number: Int): String {

    var value = ""
    if (number != 0) {
        value = "0"
        repeat(number) {
            value += if (it == number - 1) {
                "---"
            } else {
                "0"
            }
        }

    } else {
        value += "---"
    }

    repeat((9 - number)) {
        value += "0"
    }




    return value
}