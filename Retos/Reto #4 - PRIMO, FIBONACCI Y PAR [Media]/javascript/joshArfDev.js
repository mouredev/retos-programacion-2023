const prime = ( number ) => {

    let initialNumber = 2

    while( initialNumber <= Math.sqrt( number ) ) {
        
        if( number % initialNumber === 0 ) {
            return false
        }
        
        initialNumber ++
    }

    return true
}


const fibbo = ( number ) => {

    return (Math.sqrt( 5 * (number * number) + 4 ) % 1 === 0 ||  Math.sqrt( 5 * (number * number) - 4 ) % 1 === 0)
}


const even = ( number ) => {
    
    return number % 2 === 0
}


const primoFibonacciPar = ( number ) => {
    
    const isPrime = { true: 'es primo', false: 'no es primo' }
    const isFibbo = { true: 'es fibbonacci', false: 'no es fibbonaci' }
    const isEven = { true: 'es par', false: 'es impar' }

    return `${ number } ${ isPrime[prime(number)] }, ${ isFibbo[fibbo(number)] } y ${ isEven[even(number)] }`
}

console.log( primoFibonacciPar( 7 ) )

