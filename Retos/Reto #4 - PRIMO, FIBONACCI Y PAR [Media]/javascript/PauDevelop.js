//Función para saber si es primo
const isPrime = (num) => {
    for (let i = 2; i < num; i++) {
        if (num % i === 0) {
            return false
        }
    }
    return num !== 1
}

//Función para saber si es par
const isEven = (num) => (num % 2 === 0) ? true : false

//Función para saber si está incluido en la secuencia de  Fibonacci
const isFibonacci = (num) => {
    let fibonacci = [1, 1]
    for (let i = 2; i < 50000; i++) {
        fibonacci.push(fibonacci[i - 1] + fibonacci[i - 2])
    }
    return fibonacci.includes(num)
}


//FUNCIÓN FINAL QUE DEVUELVE LAS PPROPIEDADES DEL NÚMERO
const numbersProperties = (num) => {
    let properties = ''

    isPrime(num) ? properties = properties.concat(' es primo') : properties = properties.concat(' no es primo')
    isFibonacci(num) ? properties = properties.concat(', fibonacci') : properties = properties.concat(', no es fibonacci')
    isEven(num) ? properties = properties.concat(' y es par') : properties = properties.concat(' y es impar')

    return (num > 0) ? num + properties : 'Error'
}

console.log(isFibonacci(1))
console.log(numbersProperties(1))
console.log(numbersProperties(2))
console.log(numbersProperties(7))
console.log(numbersProperties(-80))
console.log(numbersProperties(13))
console.log(numbersProperties(55))
console.log(numbersProperties(364))
console.log(numbersProperties(5970))
console.log(numbersProperties(76255389263740))