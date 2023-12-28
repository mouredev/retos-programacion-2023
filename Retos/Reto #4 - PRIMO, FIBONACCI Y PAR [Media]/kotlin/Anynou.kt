fun main() {

    var number: Int
    var isPar: Boolean
    var isFibonacci: Boolean
    var isPrimo: Boolean
    var strPar: String
    var strFibo: String
    var strPrimo: String

    print("Introduce un número: ")
    number = readLine()!!.toInt()

    isPrimo = isPrimo(number)
    if (isPrimo){
        strPrimo = " es primo"
    } else {
        strPrimo = " no es primo"
    }

    isFibonacci = isFibonacci(number)
    if (isFibonacci){
        strFibo = ", fibonacci"
    } else {
        strFibo = ", no es fibonacci"
    }

    isPar = isPar(number)
    if (isPar){
        strPar = " y es par"
    } else {
        strPar = " y es impar"
    }

    var result = number.toString() + strPrimo + strFibo + strPar
    
    println(result)

}

fun isPar(number: Int): Boolean {
    var isPar: Boolean
    if (number%2 == 0){
        isPar = true
        return isPar
    } else {
        isPar = false
        return isPar
    }
}

fun isFibonacci(number: Int): Boolean {
    var isFibonacci: Boolean = false
    var fiboSig1: Int = 1
    var fiboSig2: Int = 1
    var fiboNumber: Int = 0

    while (fiboNumber < number) {
        fiboNumber = fiboSig1 + fiboSig2
        fiboSig1 = fiboSig2
        fiboSig2 = fiboNumber

        if (fiboNumber == number){
            isFibonacci = true
        } else {
            isFibonacci = false
        }
    }

    return isFibonacci
}

fun isPrimo(number: Int): Boolean {
    var isPrimo: Boolean = false
    var primos = listOf(2, 3, 5, 7, 11, 13, 17, 23)
    
    for (n in primos) {

        if (number % n != 0){
            isPrimo = true
        } else if (number == n ) {
            isPrimo = true
        } else {
            isPrimo = false
            break          
        }

    }

    return isPrimo
}

