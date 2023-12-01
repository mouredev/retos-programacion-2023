const fizzbuzz = numVal => {
    if (typeof numVal !== 'number') {
      throw new Error(`"${numVal}" is not a number`)
    }

    if (numVal === 0) {
      return numVal 
    }

    if (numVal % 3 === 0 && numVal % 5 === 0) {
      return 'fizzbuzz'
    }

    if (numVal % 3 === 0) {
      return 'fizz'
    }

    if (numVal % 5 === 0) {
      return 'buzz'
    }
    
    return numVal
  }
  
const printFizzbuzz = number => {
    for (let i = 1; i <= number; i++) {
        console.log(`${fizzbuzz(i)}`)
    }
  }
  
printFizzbuzz(100)