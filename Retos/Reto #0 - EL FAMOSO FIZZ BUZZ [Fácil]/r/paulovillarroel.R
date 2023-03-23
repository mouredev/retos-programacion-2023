## FIZZ BUZZ

fbnums <- 1:100
output <- vector()

for (i in fbnums) {
  if (i %% 3 == 0 && i %% 5 == 0) {
    output[i] <- "FizzBuzz"
  } else if (i %% 3 == 0) {
    output[i] <- "Fizz"
  } else if (i %% 5 == 0) {
    output[i] <- "Buzz"
  } else {
    output[i] <- i
  }
}

writeLines(output)
