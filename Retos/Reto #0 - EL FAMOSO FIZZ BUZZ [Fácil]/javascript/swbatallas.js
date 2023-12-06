function fizzbuzz(cantidad) {

    for (let i = 0; i < cantidad; i++) {
        if (i % 15 == 0) {
            console.log('fizzbuzz')
        }
        else if (i % 3 == 0) {
            console.log('fizz')
        }
        else if (i % 5 == 0) {
            console.log('buzz')
        }
        else console.log(i)
    }
}

fizzbuzz(100)