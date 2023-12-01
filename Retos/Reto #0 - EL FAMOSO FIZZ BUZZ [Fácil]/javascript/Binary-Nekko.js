const fizzbuzz = (start = 1, end = 100) => {
    for (let i = start; i <= end; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log('fizzbuzz')
        }
        else if (i % 3 === 0) {
            console.log('fizz')
        }
        else if (i % 5 === 0) {
            console.log('buzz')
        }
        else {
            console.log(i)
        }
    }
}

fizzbuzz()