
fun main(){
    val number = 233

    printResult(number)

}

fun printResult(number: Int) {
    var text = "$number"

    text = if (isPrimo(number)) "$text es primo"
    else "$text no es primo"
    text = if (isFibonacci(number)) "$text es fibonacci"
    else "$text no es fibonacci"
    text = if (isPar(number)) "$text es par"
    else "$text es impar"

    println(text)
}


fun isPrimo(number: Int): Boolean {
    var isPrimo = true
    var counter = 2
    while (isPrimo && counter < number){
        if (number % counter == 0 ) isPrimo = false
        counter ++
    }

    return isPrimo
}


fun isFibonacci(number: Int): Boolean {
    var isFibonacci = true
    var firstNumber = 0
    var secondNumber = 1

    while (isFibonacci){
        val thirdNumber = firstNumber + secondNumber
        if (thirdNumber == number) break
        if (thirdNumber > number) isFibonacci = false

        firstNumber = secondNumber
        secondNumber = thirdNumber
    }

    return isFibonacci
}


fun isPar(number: Int): Boolean {
    return (number % 2) == 0
}
