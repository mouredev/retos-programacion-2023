
type TwinPrime = [number, number]


const isPrime = (num: number): boolean => {
  if (num <= 1) return false
  for (let n = 2; n <= Math.sqrt(num); n++) {
    if (num % n === 0) return false
  } 

  return true
}


const twinPrime = (lnum: number): TwinPrime[] => {
  const numbers: TwinPrime[] = []
  let prevPrime = 2
  
  for (let n = 3; n <= Math.abs(lnum); n++) {
    if (isPrime(n) && (n - prevPrime) === 2){
      numbers.push([prevPrime, n])
    }
    prevPrime = isPrime(n) ? n : prevPrime
    
  }

  return numbers
    
  }
  

const mainF = () => {
  console.log(twinPrime(14))
  
}


mainF()