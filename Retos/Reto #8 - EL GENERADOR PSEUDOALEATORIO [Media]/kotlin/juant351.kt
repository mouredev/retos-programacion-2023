package `Reto 08`

fun main(args: Array<String>) {
    val numbers = Array(100) {it +1}
    val randomNumber = numbers.toList().shuffled().first()

    println("¡Tu numero pseuodoaleatorio es $randomNumber!")
}