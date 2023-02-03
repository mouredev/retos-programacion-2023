# Reto 1 - EL "LENGUAJE HACKER"

leet_letters <- list("a" = "4", "b" = "I3", "c" = "[",  "d" = ")",
                     "e" = "3", "f" = "|=", "g" = "6",  "h" = "#",
                     "i" = "1", "j" = ",_|", "k" = ">|",  "l" = "1",
                     "m" = "[V]", "n" = "^/", "o" = "0",  "p" = "|*",
                     "q" = "(_,)", "r" = "I2", "s" = "5",  "t" = "7",
                     "u" = "(_)", "v" = "|/", "w" = "(n)",  "x" = "><",
                     "y" = "j", "z" = "2")

leet_numbers <- list("1" = "L", "2" = "R", "3" = "E", "4" = "A", "5" = "S",
                     "6" = "b", "7" = "T", "8" = "B", "9" = "g", "0" = "o")

leet_alphabet <- c(leet_letters, leet_numbers)

leet_generator <- function() {
  text_input <- tolower(readline("Ingrese un texto: "))
  text_leet <- ""
  
  for (count in 1:nchar(text_input)) {
    if (substr(text_input, count, count) %in% names(leet_alphabet)) {
      text_leet = paste(text_leet, leet_alphabet[substr(text_input, count, count)])
    } else {
      text_leet = paste(text_leet, substr(text_input, count, count))
    }
  }
  print(text_leet)
}

leet_generator()