for (i = 0; i <= 100; i++){
    if (i % 3 === 0 && i % 5 === 0){
        console.log("Fizzbuzz")
    } else if (i % 5 === 0){
        console.log("Buzz")
    } else if (i % 3 === 0){
        console.log("Fizz")
    } else {
        console.log(i)
    }
}