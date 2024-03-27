import scala.math.sqrt
import scala.math.floor

@main def main(args: String*) =
    val number = args(0).toInt
    val prime = if isPrime(number) then "es primo" else "no es primo"
    val fibonacci = if isFibonacci(number) then "es fibonacci" else "no es fibonacci"
    val even = if isEven(number) then "es par" else "es impar"
    println(s"$number $prime, $fibonacci, $even")


def isEven(num: Int): Boolean = num % 2 == 0

def isPrime(num: Int): Boolean = 
    if num < 0 then false
    else if num < 4 then true
    else if isEven(num) then false
    else
        val upperLimit = floor(sqrt(num)).toInt
        val factors = (2 to upperLimit).toList
        val res = factors.map(f => num % f == 0)
        !res.contains(true)

// A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square
// Source: http://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers

def isFibonacci(num: Int): Boolean = 
    isPerfectSquare(5*num*num+4) || isPerfectSquare(5*num*num-4)

def isPerfectSquare(num: Int): Boolean =
    val s = sqrt(num).toInt
    s * s == num