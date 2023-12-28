import random

casas = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0
}
preguntas = [
    ("¿Cómo te definirías?", [
        ("1. Valiente", "Gryffindor"),
        ("2. Leal", "Hufflepuff"),
        ("3. Sabio", "Ravenclaw"),
        ("4. Ambicioso", "Slytherin")
    ]),
    ("¿Cuál es tu clase favorita?", [
        ("1. Vuelo", "Gryffindor"),
        ("2. Pociones", "Ravenclaw"),
        ("3. Defensa contra las artes oscuras", "Slytherin"),
        ("4. Animales fantásticos", "Hufflepuff")
    ]),
    ("¿Dónde pasarías más tiempo?", [
        ("1. Invernadero", "Hufflepuff"),
        ("2. Biblioteca", "Ravenclaw"),
        ("3. En la sala común", "Slytherin"),
        ("4. Explorando", "Gryffindor")
    ]),
    ("¿Cuál es tu color favorito?", [
        ("1. Rojo", "Gryffindor"),
        ("2. Azul", "Ravenclaw"),
        ("3. Verde", "Slytherin"),
        ("4. Amarillo", "Hufflepuff")
    ]),
    ("¿Cuál es tu mascota?", [
        ("1. Sapo", "Ravenclaw"),
        ("2. Lechuza", "Gryffindor"),
        ("3. Gato", "Hufflepuff"),
        ("4. Serpiente", "Slytherin")
    ])
]

def respuesta():

    rpta = input("Responde 1, 2, 3 o 4: ")
    if rpta == "1" or rpta == "2" or rpta == "3" or rpta == "4":
        return int(rpta)

    return respuesta()

print("Hola, soy el \"Sombrero Seleccionador\"\nTendrás que responder cinco preguntas para ayudarme a descubrir tu casa de Hogwarts.\n")

for pregunta in preguntas:
    print(pregunta[0])
    for x in pregunta[1]:
        print(x[0])

    casa = pregunta[1][respuesta()-1][1]
    casas[casa] += 1

seleccionar_casa = []
max_punto = 0

for casa, puntos in casas.items():
    if puntos > max_punto:
        seleccionar_casa.clear()
        seleccionar_casa.append(casa)
        max_punto = puntos
    elif puntos == max_punto:
        seleccionar_casa.append(casa)
        max_punto = puntos

print("Tu casa es: " + random.choice(seleccionar_casa))
