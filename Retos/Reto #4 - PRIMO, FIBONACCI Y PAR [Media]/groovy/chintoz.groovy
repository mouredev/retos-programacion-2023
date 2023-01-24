import groovy.transform.TailRecursive

@TailRecursive
def isPrimeNumber(def number, def divisor = 2) {
    if (number / 2 < divisor) return true
    if (number % divisor == 0) return false
    isPrimeNumber(number, divisor + 1)
}

static def isFibonacci(int number) {
    if (number == 0 || number == 1 || number == 2) {
        return true
    }

    def fibNumber = new Tuple<Integer>(1, 1, 2)
    while (fibNumber.get(2) < number) {
        fibNumber = new Tuple<Integer>(fibNumber.get(1), fibNumber.get(2), fibNumber.get(1) + fibNumber.get(2))
        if (fibNumber.get(2) == number) return true
    }
    false
}

static def isEven(def number) {
    number % 2 == 0
}

print("Introduce el número a comprobar: ")
def input = Math.abs(System.in.newReader().readLine() as Integer)

println("$input ${isPrimeNumber(input) ? "es primo" : "no es primo"}, " +
        "${isFibonacci(input) ? "es fibonacci" : "no es fibonacci"}, " +
        "${isEven(input) ? "es par" : "es impar"}")