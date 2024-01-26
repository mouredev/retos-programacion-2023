const twinsPrimes = (range) => {    
    let res = []
    let k
    
    for(let i = 3; i < range - 1; i = k) {
        for(let j = i+1; ;j++) {
            let isPrime = isPrimeNum(j)
            if(isPrime) {
                k = j
                break
            } else {
                continue
            }
        }
        
        if(k - i === 2) {
            res.push([i, k])        
        }
    }
    return res
}

const isPrimeNum = (n) => {
    if(n <= 1) return false
    for(let i = 2; i<= Math.sqrt(n); i++) {
        if(n % i === 0) return false
    }
    return true
}

console.log(twinsPrimes(14))
console.log(twinsPrimes(124))
console.log(twinsPrimes(60))
console.log(twinsPrimes(32))