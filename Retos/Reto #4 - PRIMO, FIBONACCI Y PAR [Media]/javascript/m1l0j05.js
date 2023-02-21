/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function checkInput(expresionInput) {
    let numberCheck
    while (true) {
      numberCheck = prompt(expresionInput)
      if (numberCheck === null) {
        return null
      }
  
      if (parseInt(numberCheck)) {
        numberCheck = parseInt(numberCheck)
        console.log(`>>> Your number is: ${numberCheck}`)
        return numberCheck
      } else {
        console.log('>>> ERROR! Only accept numbers')
        alert('>>> ERROR! Only accept numbers')
      }
    }
  }
  
  function checkPrime(number) {
    if (number < 0) {
      return false
    }
    if (number > 0) {
      const myRange = Array.from({ length: number - 2 }, (a, b) => b + 2)
      for (let i = 0; i < myRange.length; i++) {
        if (number % myRange[i] == 0) {
          return false
        }
      }
    }
    return true
  }
  
  function checkFibonacci(number) {
    let n1 = 0
    let n2 = 1
  
    if (number > 0) {
      while (number >= n1) {
        numFibo = n1 + n2
        if (number == n1) {
          return true
        } else {
          n1 = n2
          n2 = numFibo
        }
      }
    }
    return false
  }
  
  function checkNumber() {
    console.log('>>> Start !!')
  
    let numberCheck = checkInput(
      '>>> Input your number:\n>>> To exit press CANCEL\n'
    )
  
    if (numberCheck === null) {
      console.log('>>> Canceled by user!\n')
      return
    } else {
  
      /*
      let isEven = numberCheck % 2 == 0 ? true : false
      */
     let isEven = (number) => {
       return number % 2 == 0 
      }
      console.log(`>>> Is the number even?: ${isEven(numberCheck)}`)
  
      let isPrime = checkPrime(numberCheck)
      console.log(`>>> Is the number prime?: ${isPrime}`)
  
      let isFibonacci = checkFibonacci(numberCheck)
      console.log(`>>> Is the number Fibonacci?: ${isFibonacci}`)
  
    }
  }
  
  checkNumber()
  