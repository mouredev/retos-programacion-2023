const FizzBuzz = (): void => {
    let i: number;
    for (i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) console.log(`${i} fizzBuzz`)
        if (i % 3 === 0) console.log('fizz')
        if (i % 5 === 0) console.log('fizz')
        if (i % 3 !== 0 && i % 5 !== 0) console.log(i)
    }
}

FizzBuzz()
