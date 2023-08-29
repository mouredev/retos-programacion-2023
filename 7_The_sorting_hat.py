def main():
  print()
  print("¡Bienvenido al Sombrero Seleccionador de Hogwarts! 🧙‍♂️🎩")
  print("Responde las siguientes preguntas para determinar tu casa. 🏠")

  preguntas = [
    "¿Qué cualidad valoras más?", "¿Qué tipo de desafíos te emocionan?",
    "¿Cuál es tu enfoque ante decisiones difíciles?",
    "¿Qué tipo de amigos te gustaría tener?",
    "¿En qué tipo de ambiente te sientes más cómodo?"
  ]

  respuestas = [["Valentía", "Astucia", "Lealtad", "Intelecto"],
                [
                  "Aventuras peligrosas", "Lograr tus objetivos",
                  "Ayudar a otros", "Aprender cosas nuevas"
                ],
                [
                  "Sigo mi instinto", "Elaboro un plan cuidadoso",
                  "Consulto a otros", "Analizo todas las opciones"
                ],
                [
                  "Valientes y decididos", "Ambiciosos y astutos",
                  "Leales y amigables", "Inteligentes y curiosos"
                ],
                [
                  "Lugares audaces y emocionantes",
                  "Lugares estratégicos y poderosos",
                  "Lugares acogedores y amigables",
                  "Lugares llenos de conocimiento"
                ]]

  casas = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
  puntuaciones = [0, 0, 0, 0]

  for i in range(len(preguntas)):
    print("\n" + preguntas[i])
    for j in range(4):
      print(f"{j + 1}. {respuestas[i][j]}")
    respuesta = int(input("Selecciona tu respuesta (1/2/3/4): "))
    puntuaciones[respuesta - 1] += 1

  casa_seleccionada = casas[puntuaciones.index(max(puntuaciones))]
  print("\n¡El Sombrero ha decidido! 🎉🔮")
  print(f"¡Felicidades! Te unes a la casa de {casa_seleccionada}. 🏆🏰")


if __name__ == "__main__":
  main()
