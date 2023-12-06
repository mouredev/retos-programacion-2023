#  Crea un programa que simule el comportamiento del sombrero selccionador del
#  Universo mágico de Harry Potter.
#  - De ser posible realizará 5 preguntas(como mínimo) a través de la terminal.
#  - Cada pregunta tendrá 4 respuestas posibles(también a selecciona una a través de terminal).
#  - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#    coloque al alumno en una de las 4 casas de Hogwarts(Gryffindor, Slytherin, Hufflepuff y Ravenclaw)
#  - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#    Por ejemplo, en Slytherin se premia la ambición y la astucia.

sorting_Hat <- function(){
  
  Gryffindor = 0
  Hufflepuff = 0
  Ravenclaw = 0
  Slytherin = 0
  
  questions <- list(
    "¿Cuál de las siguientes odiarías más que la gente te llamara?" = list(
      "Cobarde" = 1,
      "Egoista" = 2,
      "Ignorante" = 3,
      "Ingenuo" = 4),
    "¿Cómo le gustaría ser conocido en la historia?" = list("El gran" = 1, "El bueno" = 2, "El sabio" = 3, "El audaz" = 4),
    "¿Qué tipo de instrumento agrada mas a tu oído?" = list("Trompeta" = 1, "Tambores" = 2, "Violin" = 3, "Piano" = 4),
    "¿Qué es lo que más anhelas aprender en Hogwarts?" = list(
      "Volar en una escoba"= 1,
      "Todo sobre criaturas mágicas, hacerse amigo y protegerlos"= 2,
      "Cada área de magia que pueda"= 3,
      "Maleficios y hechizos"= 4),
    "Tú y dos amigos deben cruzar un puente custodiado por un troll de río que insiste en\n luchar contra uno de ustedes antes de que los deje pasar a todos. Tú:" = list(
      "Te ofreces como voluntario"= 1,
      "¿Sugieres que los tres deben luchar? (sin decírselo al troll)"= 2,
      "¿Intentas confundir al troll para que te deje pasar a los tres sin luchar?"= 3,
      "¿Sugerir un sorteo para decidir quién de ustedes peleará?"= 4),
    "A altas horas de la noche, caminando solo por la calle, escuchas un grito peculiar\n que crees que tiene una fuente mágica. ¿Cuál elegirías?:" = list(
      "Tomas tu varita y tratas de descubrir la fuente del ruido!" = 1,
      "Retirarse a las sombras para esperar los acontecimientos, mientras revisas los hechizos defensivos y ofensivos más apropiados" = 2,
      "¿Proceder con precaución, manteniendo una mano en tu varita oculta y atento a cualquier perturbación?" = 3,
      "¿Tomar tu varita y mantenerte firme?" = 4)
  )
  
  
  questions_remaining <- names(questions)
  
  while(length(questions_remaining) > 0){
    cat("\014")
    random_question = sample(questions_remaining, 1)
    if (length(random_question) == 0) {
      break
    }
    question_text <- random_question[1]
    cat(question_text, "\n")
    
    list_options = questions[[question_text]]
    #print(list_options)
    for (option in names(list_options)) {
      cat(list_options[[option]],") ", option , "\n", sep = "")
    }
    ops = readline(prompt = "Ingresa una opción: ")
    #obs = c("1", "2", "3", "4")
    
    SALIR = 0
    
    while (SALIR == 0) {
      if (ops == "1" | ops == "2" | ops == "3" | ops == "4") {
        SALIR = 1
      } else {
        ops = readline(prompt = "Ingresa una opción correcta: ")
        SALIR = 0
      }
    }
    
    cat("\n")
    questions_remaining <- setdiff(questions_remaining, random_question)
  
    switch(ops,
           "1" = { Gryffindor <- Gryffindor + 1 },
           "2" = { Hufflepuff <- Hufflepuff + 1 },
           "3" = { Ravenclaw <- Ravenclaw + 1 },
           "4" = { Slytherin <- Slytherin + 1 })
  
  }
  
  maximo = c(Gryffindor, Hufflepuff, Ravenclaw, Slytherin)
  
  if (max(maximo, na.rm = TRUE) == Gryffindor) {
    casa = "Gryffindor"
  } else if (max(maximo, na.rm = TRUE) == Hufflepuff) {
    casa = "Hufflepuff"
  } else if (max(maximo, na.rm = TRUE) == Ravenclaw) {
    casa = "Ravenclaw"
  } else if (max(maximo, na.rm = TRUE) == Slytherin) {
    casa = "Slytherin"
  }
  
  cat(paste("Apartir de ahora serás de la casa ", casa, "!", sep = ""))

}



main <- function(){
  cat("\014")
  cat("\n")
  cat("EL SOMBRERO SELECCIONADOR: \n")
  cat("SE REALIZARAN 6 PREGUNTAS, DEBES ESCOGER UNA OPCIÓN (1:4): \n")
  sorting_Hat()
  cat("\n")
  cat("GRACIAS POR JUGAR!\n")
}



main()