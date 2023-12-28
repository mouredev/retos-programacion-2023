# Reto #4: PRIMO, FIBONACCI Y PAR

# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
#  - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

prime_number <- function(number){
  
  x = seq(1, number)
  
  vecPrime=c()
  
  for (i in seq(2, number)) {
    if (any(x == i)) {
      vecPrime = c(vecPrime, i)
      x = c(x[(x %% i) != 0], i)
    }
  }
  for (item in vecPrime) {
    if (item == number) {
      prime = "es primo,"
      break
    }else 
      prime = "no es primo,"
  }
  return(prime)
}

fibonacci <- function(number){
  n0 = 0
  n1 = 1
  
  for (i in 1:(number - 2)) {
    fib = n0 + n1
    n0 = n1
    n1 = fib
    
    if (fib == number) {
      fibo = "fibonacci"
      break
    }else
      fibo = "no es fibonacci"
  }
  return(fibo)
}

even_odd <- function(number) {
  if (number %% 2 == 0) {
    message <- "y es par"
  }else
    message <- "y es impar"
  return(message)
}

what_kind_of_number <- function(number) {
  
  print(paste(number,
              prime_number(number),
              fibonacci(number),
              even_odd(number)))

}

what_kind_of_number(2)
what_kind_of_number(7)
what_kind_of_number(8)
what_kind_of_number(13)








