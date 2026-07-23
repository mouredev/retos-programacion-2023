for (let i = 1; i <= 100; i++) {
    const resultado = fizzBuzz(i)
    console.log(resultado)
}
    
function fizzBuzz(n) {
    if (n % 3 === 0 && n % 5 === 0) {
        return 'fizzbuzz'
    } 

    if (n % 3 === 0) {
        return 'fizz'
    }

    if (n % 5 === 0) {
        return 'buzz'
    }

    return n
}