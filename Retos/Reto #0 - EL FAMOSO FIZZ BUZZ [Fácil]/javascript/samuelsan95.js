function isMultiplo (num, multiplo) {
    return (num % multiplo) === 0
}

function run () {
    for (let i = 1; i <= 100; i++) {
        let res = i

        if (isMultiplo(i, 3) && isMultiplo(i, 5)) {
            res = 'fizzbuzz'
        } else if (isMultiplo(i, 3)) {
            res = 'fizz'
        } else if (isMultiplo(i, 5)) {
            res = 'buzz'
        }

        console.log(res)
    }
}

run()