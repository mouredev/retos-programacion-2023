function fizzbuzz(num) {
    while (num < 100) {
        num = num + 1
        if (num % 3 == 0 && num % 5 == 0) {
            console.log("FizzBuzz")
        } else if (num % 3 == 0) {
            console.log("Fizz")
        } else if (num % 5 == 0) {
            console.log("Buzz")
        } else {
            console.log(num)
        }
    }
}

let number = 0
fizzbuzz(number)