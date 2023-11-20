function isPrime(num) {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
        if(num % i === 0) return false; 
    return num > 1;
}

function findTwinPrimes(n) {
    let twinPrimes = [];
    for(let i = 2; i <= n - 2; i++) {
        if(isPrime(i) && isPrime(i + 2)) {
            twinPrimes.push([i, i + 2]);
        }
    }
    return twinPrimes;
}

console.log(findTwinPrimes(14));