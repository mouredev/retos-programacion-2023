# * LA FUNCION GENERADOR, CREA DOS EMOJIS ALEATORIAMENTE

generador <- function(){
  db <- c("\U0001F596", "\U0001f98e", "\u2702\uFE0F", "\U0001F4C4", "\U0001F5FF")
  fp <- sample(db, replace = FALSE, size = 1)
  sp <- sample(db, replace = FALSE, size = 1)
  return(c(fp, sp))
}

contadoremo <- function(n){
  contadorfp <- 0
  contadorsp <- 0
  f <- "PLAYER 1"
  s <- "PLAYER 2"
  #gene <- generador()
  for (i in 1:n){
    gene <- generador()
    a <- gene[1]
    b <- gene[2]
    cat(rep("*", 15), "\n")
    print(sprintf("%s: %s", f, a))
    print(sprintf("%s: %s", s, b))
    if (a == "\U0001F5FF" & b == "\u2702\uFE0F") {
      contadorfp <- contadorfp + 1
    }
    if (b == "\U0001F5FF" & a == "\u2702\uFE0F") {
      contadorsp <- contadorsp + 1
    }
    if (a == "\u2702\uFE0F" & b == "\U0001F4C4") {
      contadorfp <- contadorfp + 1
    }
    if (b == "\u2702\uFE0F" & a == "\U0001F4C4") {
      contadorsp <- contadorsp + 1
    }
    if (a == "\U0001F4C4" & b == "\U0001F5FF") {
      contadorfp <- contadorfp + 1
    }
    if (b == "\U0001F4C4" & a == "\U0001F5FF") {
      contadorsp <- contadorsp + 1
    }
    if (a == "\U0001F5FF" & b == "\U0001f98e") {
      contadorfp <- contadorfp + 1
    }
    if (b == "\U0001F5FF" && a == "\U0001f98e") {
      contadorsp <- contadorsp + 1
    }
    if (a == "\U0001f98e" & b == "\U0001F596") {
      contadorfp <- contadorfp + 1
    }
    if (b == "\U0001f98e" & a == "\U0001F596") {
      contadorsp <- contadorsp + 1
    }
    if (a == "\U0001F596" & b == "\u2702\uFE0F") {
      contadorfp <- contadorfp + 1
    }
    if (b == "\U0001F596" & a == "\u2702\uFE0F") {
      contadorsp <- contadorsp + 1
    }
    if (a == "\u2702\uFE0F" & b == "\U0001f98e") {
      contadorfp <- contadorfp + 1
    }
    if (b == "\u2702\uFE0F" & a == "\U0001f98e") {
      contadorsp <- contadorsp + 1
    }
    if (a == "\U0001f98e" & b == "\U0001F4C4") {
      contadorfp <- contadorfp + 1
    }
    if (b == "\U0001f98e" & a == "\U0001F4C4") {
      contadorsp <- contadorsp + 1
    }
    if (a == "\U0001F4C4" & b == "\U0001F596") {
      contadorfp <- contadorfp + 1
    }
    if (b == "\U0001F4C4" & a == "\U0001F596") {
      contadorsp <- contadorsp + 1
    }
    if (a == "\U0001F596" & b == "\U0001F5FF") {
      contadorfp <- contadorfp + 1
    }
    if (b == "\U0001F596" & a == "\U0001F5FF") {
      contadorsp <- contadorsp + 1
    }
        
  }
  return(c(contadorfp, contadorsp))
}

analiza <- function(){
  SALIR <- 0
  while (SALIR == 0) {
    conta <- contadoremo(5)
    contadorfp <- conta[1]
    contadorsp <- conta[2]
    if (contadorfp > contadorsp){
      cat(rep("*", 15), "\n")
      print("GANADOR PLAYER 1")
      break
    }
    if (contadorfp < contadorsp){
      cat(rep("*", 15), "\n")
      print("GANADOR PLAYER 2")
      break
    }
    #**
    while (contadorfp == contadorsp) {
      cat(rep("*", 15), "\n")
      print("EMPATE!!")
      conta <- contadoremo(1)
      contadorfp <- conta[1]
      contadorsp <- conta[2]
      if (contadorfp > contadorsp){
        cat(rep("*", 15), "\n")
        print("GANADOR PLAYER 1")
        break
      }
      if (contadorfp < contadorsp){
        cat(rep("*", 15), "\n")
        print("GANADOR PLAYER 2")
        break
      }
    }
    SALIR = 1
  }
}


main <- function(){
  cat("\014")
  print("JUEGO: PIEDRA, PAPEL, TIJERA, LAGARTO Y SPOCK")
  analiza()
}

main()

