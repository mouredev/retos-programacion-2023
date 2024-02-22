# 
# Crea un programa que simule el comportamiento del sombrero seleccionador del # universo mágico de Harry Potter.
# - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
# - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
# - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
# - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#   Por ejemplo, en Slytherin se premia la ambición y la astucia.
# 

CASAS = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

PREGUNTAS = [
    ("¿Cómo prefieres pasar tu tiempo libre?",
     {"Participando en actividades emocionantes y arriesgadas.": CASAS[0],
      "Disfrutando del tiempo con amigos y seres queridos.": CASAS[2],
      "Planificando y organizando tus proyectos personales.": CASAS[1],
      "Explorando nuevos temas y aprendiendo constantemente.": CASAS[3]}),

    ("¿Qué tipo de logro te hace sentir más satisfecho?",
     {"Superar obstáculos personales.": CASAS[0],
      "Ser reconocido por tu dedicación y lealtad.": CASAS[2],
      "Alcanzar el éxito mediante la astucia y la planificación.": CASAS[1],
      "Adquirir nuevos conocimientos y habilidades.": CASAS[3]}),

    ("Ante una injusticia, ¿cuál sería tu reacción?",
     {"Apoyar y consolar a quienes están afectados.": CASAS[2],
     "Actuar de inmediato para corregir la situación.": CASAS[0],
      "Encontrar la manera más estratégica de abordar el problema.": CASAS[1],
      "Investigar y comprender las causas subyacentes.": CASAS[3]}),

    ("¿Cuál es tu enfoque preferido al enfrentar un desafío?",
     {"Actuar rápidamente sin pensarlo demasiado.": CASAS[0],
      "Planificar cuidadosamente cada paso.": CASAS[1],
      "Buscar la colaboración y el apoyo de otros.": CASAS[2],
      "Analizar la situación antes de tomar una decisión.": CASAS[3]      }),

    ("¿Qué cualidad valoras más en un compañero de equipo?",
     {"Coraje y valentía.": CASAS[0],
      "Lealtad y amabilidad.": CASAS[2],
      "Astucia e inteligencia.": CASAS[1],
      "Sabiduría y curiosidad.": CASAS[3]}),
]


def preguntar_numero():
    print("Seleccione un número del 1 al 4")
    while True:
        try:
            respuesta = int(input(""))
            if respuesta in range (1, 5):
                break
            else:
                print("Seleccione un numero correcto")
        except ValueError:
            print("Introduzca un carácter numérico")
    return respuesta

def main():
    while True:
        print("Bienvenido al Test de Harry Potter para encontrar tu casa de Hogwards")
        puntuaciones_casas = {casa: 0 for casa in CASAS}

        for pregunta, respuestas in PREGUNTAS:
            print(f"\n {pregunta}")
            for numero, (respuesta, casa) in enumerate(respuestas.items()):
                print(f"{numero + 1} - {respuesta}")
            respuesta = preguntar_numero()
            puntuaciones_casas[list(respuestas.values())[respuesta - 1]] +=1

        casa_seleccionada = max(puntuaciones_casas, key=puntuaciones_casas.get)
        print("*"*48)
        print(f"¡La casa que más te representa es {casa_seleccionada}!")
        print("*"*48)
        break

if __name__ == "__main__":
    main()


