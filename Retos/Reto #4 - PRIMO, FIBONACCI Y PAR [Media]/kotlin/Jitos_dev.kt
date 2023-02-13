package reto4.kotin

fun main(){
    val jitosDev = jitos_dev()

    val result1: String = jitosDev.checkNumber(2)
    val result2: String = jitosDev.checkNumber(7)
    val result3: String = jitosDev.checkNumber(55)
    val result4: String = jitosDev.checkNumber(73)

    println(result1)
    println(result2)
    println(result3)
    println(result4)
}


class jitos_dev {

    fun checkNumber(number: Int): String {
        var message: String = number.toString()

        //Si es primo
        message += if(isPrimo(number)) " es primo, " else " no es primo, "

        //Si es fibonacci
        message += if(isFibonacci(number)) "fibonacci " else "no es fibonacci "

        //Si es par
        message += if(number % 2 == 0)  "y es par" else "y es impar"

        return message;
    }

    private fun isPrimo(number: Int): Boolean {
        if (number == 0 || number == 1)
            return false

        for (i in 2..number / 2) {
            if (number % i == 0)
                return false
        }

        return true;
    }

    private fun isFibonacci(number: Int): Boolean{
        //el número 0 y el número 1 son los primeros de fibonacci
        if (number == 0 || number == 1)
            return true

        var previous = 1
        var later = 1
        var fibonacci: Int

        while (true) {
            fibonacci = previous + later;

            //Si el número es mayor es que no es fibonacci por que se ha pasado
            if (fibonacci > number)
                return false

            //Si el número es igual es que si es fibonacci
            if (fibonacci == number)
                return true

            //el número anterior le damos el valor del posterior para adelantar una posición
            previous = later

            //al número posterior le damos el valor de fibonacci para actualizarlo en la siguiente vuelta
            later = fibonacci
        }

    }
}