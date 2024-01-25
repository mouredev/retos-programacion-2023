for (let i = 1; i <= 100; i++) {
    if (Number.isInteger(i/3)) {
        console.log("fizz")
    } else if(Number.isInteger(i/5)) {
        console.log("buzz")
    } else if (Number.isInteger(i/3) && Number.isInteger(i/5)) {
        console.log("fizzbuzz")
    } else {
        console.log(i)
    }
}
