def transform = { number ->
    if (number % 3 == 0 && number % 5 == 0) return "fizzbuzz"
    if (number % 3 == 0) return "fizz"
    if (number % 5 == 0) return "buzz"
    number
}
(0..100).collect { transform it }.each { println it }
