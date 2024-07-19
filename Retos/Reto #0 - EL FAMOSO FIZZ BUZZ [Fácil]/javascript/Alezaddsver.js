for (range = 1; range <= 100; range +=1) {
    if (range % 3 === 0 && range % 5 === 0) {
        console.log("fizzbuzz")
    }
    else if (range % 5 === 0 ) {
        console.log("buzz")
    }
    else if (range % 3 === 0) {
        console.log("fizz")
    }
    else {
        console.log(range)
    }
}
