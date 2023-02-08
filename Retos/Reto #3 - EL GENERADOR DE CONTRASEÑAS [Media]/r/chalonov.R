# RETO 3 - PASSWORD GENERATOR

# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)

password_generator <- function(size, case_letters, number, symbol) {
  if (size >= 8 & size <=16) {
    
    if (case_letters == "lower") {
      alphabet <- c(letters)
    }else if (case_letters == "upper") {
      alphabet <- c(LETTERS)
    }else if (case_letters == "any") {
      alphabet <- c(LETTERS, letters)
    }
    
    if (number == 0) {
      numbers <- as.character(c())
    }else if (number == 1) {
      numbers <- as.character(c(0:9))
    }
    
    if (isTRUE(symbol)) {
      symbols <- unlist(strsplit(c("!#$%&/()=?¡"), split=""))
    }else if (isFALSE(symbol)) {
      symbols <- c()
    }
    
    password <- paste0(sample(c(numbers, alphabet, symbols), size), collapse = "")
    
    print(paste("Password: ", password))
    
  }else
    print("ERROR: Ingrese un tamaño de contraseña entre 8-16 caracteres")
}

password_generator(16, "lower", 1, TRUE)  # "Password:  9p)mns1/ghz4l&kx"
password_generator(8, "upper", 0, FALSE)  # "Password:  UKGEHBIS"
password_generator(12, "lower", 0, TRUE)  # "Password:  ex)zo%#k?(ip"
password_generator(14, "upper", 1, FALSE) # "Password:  378KLY0EWB9ZP5"
password_generator(9, "any", 1, FALSE)    # "Password:  sJmNQF4Rv"
password_generator(17, "upper", 1, FALSE) # "ERROR: Ingrese un tamaño de contraseña entre 8-16 caracteres"



