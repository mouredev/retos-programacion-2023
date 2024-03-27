const number = 2

let isPrime = false
let isPair = false
let isFibo = false

for (let i = 2; i < number; i++) {
    if (number % i == 0) {
        isPrime = false
    }
}

isPair = number % 2 == 0 ? true : false

const fibo = [1,1]

for (let i = 1; i < 20; i++) {
    fibo.push(fibo[i] + fibo[i-1])
}

isFibo = fibo.includes(number) ? true : false

console.log(`${number} ${!isPrime ? "es" : "no es"} primo, ${isFibo ? "es" : "no es"} fibonacci y ${isPair ? "es" : "no es"} par`)
