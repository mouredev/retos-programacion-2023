function fb(x) {
    for (i = 1; i <= x; i++){
        if (i % 3 === 0 && i % 5 === 0) {
            console.log("FizzBuzz")
        } else if (i % 3 === 0) {
            console.log("Fizz")
        } else if (i % 5 === 0) {
            console.log("Buzz")
        }
    }
}

let control = 100

fb(control)