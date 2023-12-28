fun main() {
    println("[+] Generador de contraseñas")

    var respCorrect: Boolean
    var numChar: Int = 0
    var mayus: String = "n"
    var nums: String = "n"
    var simb: String = "n"


    respCorrect = false

    while (respCorrect == false){
        print("Introduce el numero de caracters (8-16): ")
        numChar = readLine()!!.toInt()
        respCorrect = checkChars(numChar)

    }


    respCorrect = false

    while (respCorrect == false){
        print("¿Deseas incluir mayúsculas? (s/n): ")
        mayus = readLine()!!
        respCorrect = checkResp(mayus)

    }

    respCorrect = false
    
    while (respCorrect == false){
        print("¿Deseas incluir números? (s/n): ")
        nums = readLine()!!
        respCorrect = checkResp(nums)

    }

    respCorrect = false
    
    while (respCorrect == false){
        print("¿Deseas incluir símbolos (s/n): ")
        simb = readLine()!!
        respCorrect = checkResp(simb)

    }

    var password = createPassword(numChar, mayus, nums, simb)
    println(password)

    
}

fun checkChars(number: Int): Boolean {

    var correct: Boolean

    if (number < 8 || number > 16) {
        correct = false
        return correct
    } else {
        correct = true
        return correct
    }
}

fun checkResp(resp: String): Boolean {

    var correct: Boolean

    if (resp == "s" || resp == "n") {
        correct = true
        return correct
    } else {
        correct = false
        return correct
    }
}

fun createPassword(numChar: Int, mayus: String, nums: String, simb: String): String {

    val allowedChars = mutableListOf<Char>()
    val minusChars = 'a'..'z'
    val mayusChars = 'A'..'Z'
    val numChars = '0'..'9'
    val simbChars = listOf('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}','?')

    allowedChars.addAll(minusChars)

    if (mayus == "s") {
        allowedChars.addAll(mayusChars)      
    }

    if (nums == "s") {
        allowedChars.addAll(numChars)      
    }

    if (mayus == "s") {
        allowedChars.addAll(mayusChars)      
    }

    if (simb == "s") {
        allowedChars.addAll(simbChars)      
    }

    return (1..numChar)
        .map { allowedChars.random() }
        .joinToString("")
}
