function fizzbuzz(){
    for (let i = 0; i <= 100; i++) {
        console.log(
            (i % 5 === 0 && i % 3 === 0) ? 'fizzbuzz' : (i % 5 === 0) ? 'buzz' : (i % 3 === 0) ? 'fizz' : i 
        )
    }
}

fizzbuzz();