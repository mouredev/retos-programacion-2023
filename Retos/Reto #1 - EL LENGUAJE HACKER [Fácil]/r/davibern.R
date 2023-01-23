#
# Escribe un programa que reciba un texto y transforme lenguaje natural a 'lenguaje hacker' (conocido realmente como "leet" o "1337").
# Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
# 
# Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) con el alfabeto y los números en "leet".
# (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#

leet <- c("a" = "4", "b" = "I3", "c" = "[", "d" = ")", "e" = "3", "f" = "|=", "g" = "&", "h" = "#", "i" = "1", "j" = ",_|", "k" = ">|", "l" = "1", 
"m" = "//", "n" = "^/", "o" = "0", "p" = "|*", "q" = "(_,)", 
"r" = "I2", "s" = "5", "t" = "7", "u" = "(_)", "v" = "///", "w" = "/", 
"x" = "><", "y" = "j", "z" = "2")

transformar_texto <- function(texto) {

    texto <- tolower(texto)
    texto_encriptado = ""

    for (i in 1:nchar(texto)) {
      if (substr(texto, i, i) %in% names(leet)) {
        texto_encriptado = paste(texto_encriptado, leet[substr(texto, i, i)], sep = "")
      } else {
        texto_encriptado = paste(texto_encriptado, substr(texto, i, i), sep = "")
      }
    }
    return(texto_encriptado)
}

texto <- readline(prompt = "Escribe un texto que se va a hackear: ")
print(transformar_texto(texto))