generate_password <- function(size = 8, case = FALSE, number  = FALSE, symbol = FALSE) {

    if (size < 8 || size > 16) {
        print('La contraseña tiene que tener entre 8 y 16 caracteres')
    } else {

        if (case == TRUE) {
            chars <- c(letters, LETTERS)
        } else {
            chars <- c(letters)
        }

        if (number == TRUE) {
            numbers <- as.character(c(0:9))
        } else {
            numbers <- as.character(c())
        }

        if (symbol == TRUE) {
            special_chars <- unlist(strsplit(c("¿?¡!#$€%&@|~/()="), split=""))
        } else {
            special_chars <- c()
        }

        password <- paste0(sample(c(chars, numbers, special_chars), size), collapse = "")
        print(password)

    }

}

generate_password(size = 10, case = TRUE, number = TRUE, symbol = TRUE)
generate_password(size = 12, case = FALSE, number = FALSE, symbol = TRUE)
generate_password(size = 24)
generate_password(size = 102, case = FALSE, number = FALSE, symbol = TRUE)
generate_password(size = 12, case = TRUE, number = TRUE, symbol = FALSE)
generate_password(size = 12, case = TRUE, number = FALSE, symbol = FALSE)