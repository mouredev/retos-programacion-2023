# Crea un programa que simule el comportamiento del sombrero selccionador del
# universo mágico de Harry Potter.
# - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
# - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
# - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#   coloque al alumno en una de las 4 casas de Hogwarts:
#   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
# - Ten en cuenta los rasgos de cada casa para hacer las preguntas
#   y crear el algoritmo seleccionador:
#   Por ejemplo, en Slytherin se premia la ambición y la astucia.

# Welcome message
print("Bienvenido al sombrero seleccionador de Hogwarts!")

# Questions and answers
questions = [
    {
        "question": "¿Que rasgo te diferencia más?",
        "answers": {'a': 'Valor', 'b': 'Creatividad', 'c': 'Justicia', 'd': 'Ambicion'}
    },
    {
        "question": "¿Con que elemento sientes mas simbiosis?",
        "answers": {'a': 'Fuego', 'b': 'Aire', 'c': 'Tierra', 'd': 'Agua'}
    },
    {
        "question": "¿Qué cualidad valoras más?",
        "answers": {'a': 'Fuerza', 'b': 'Erudición', 'c': 'Lealtad', 'd': 'Determinación'}
    },
    {
        "question": "¿Qué cualidad de define mejor?",
        "answers": {'a': 'Audacia', 'b': 'Inteligencia', 'c': 'Paciencia', 'd': 'Astucia'}
    },
    {
        "question": "¿Que metal te gusta mas?",
        "answers": {'a': 'Oro', 'b': 'Bronce', 'c': 'Tungsteno', 'd': 'Plata'}
    }
]

# Ask questions
answers = []
for question in questions:
    print(question["question"])
    for key, value in question["answers"].items():
        print(f"{key}.- {value}")
    answer = input("Seleccione una opción (a, b, c o d): ").lower()
    while answer not in question["answers"]:
        print("Respuesta inválida. Por favor seleccione una de las opciones (a, b, c o d)")
        answer = input("Seleccione una opción (a, b, c o d): ").lower()
    answers.append(answer)

# Calculate score
score = {
    "gryffindor": 0,
    "slytherin": 0,
    "hufflepuff": 0,
    "ravenclaw": 0
}

for answer in answers:
    if answer == "a":
        score["gryffindor"] += 1
        score["slytherin"] += 1
    elif answer == "b":
        score["hufflepuff"] += 1
        score["ravenclaw"] += 1
    elif answer == "c":
        score["gryffindor"] += 1
        score["hufflepuff"] += 1
    elif answer == "d":
        score["slytherin"] += 1
        score["ravenclaw"] += 1

# Get house
house = max(score, key=score.get)

# Print house
print(f"¡Felicidades! Tu casa es {house.title()}")
