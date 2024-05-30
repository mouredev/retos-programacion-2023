"""
Crea un programa que simule el comportamiento del sombrero
seleccionador del universo magico de Harry Potter.
- De ser posible realizara 5 preguntas (como minimo) a traves
de la terminal.
- Cada pregutna tendra 4 respuestas posibles (tambien a
selecciona una a traves de terminal).
- En guncion de las respuestas a las 5 preguntas deberas 
disenar un algoritmo que 
coloque al alumno en una de las 4 casas de Hogwarts
(Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
- Ten en cuenta los rasgos de cada casa para hacer las 
preguntas y crear el algoritmo seleccionador.
Por ejemplo, en Slytherin se premia la ambicion y la astucia.
"""

def preguntar(pregunta, opciones):
    print(pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion['respuesta']}")
    while True:
        try:
            respuesta = int(input("Selecciona una opción (1-4): "))
            if 1 <= respuesta <= 4:
                return opciones[respuesta - 1]['casa']
            else:
                print("Por favor, selecciona un número entre 1 y 4.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

def sombrero_seleccionador():
    preguntas = [
        {
            "pregunta": "¿Qué calidad valoras más en ti mismo?",
            "opciones": [
                {"respuesta": "Valentía", "casa": "Gryffindor"},
                {"respuesta": "Inteligencia", "casa": "Ravenclaw"},
                {"respuesta": "Lealtad", "casa": "Hufflepuff"},
                {"respuesta": "Astucia", "casa": "Slytherin"}
            ]
        },
        {
            "pregunta": "¿Cuál de estas materias prefieres?",
            "opciones": [
                {"respuesta": "Defensa Contra las Artes Oscuras", "casa": "Gryffindor"},
                {"respuesta": "Aritmancia", "casa": "Ravenclaw"},
                {"respuesta": "Herbología", "casa": "Hufflepuff"},
                {"respuesta": "Pociones", "casa": "Slytherin"}
            ]
        },
        {
            "pregunta": "¿Qué harías en una situación peligrosa?",
            "opciones": [
                {"respuesta": "Enfrentar el peligro de frente", "casa": "Gryffindor"},
                {"respuesta": "Buscar una solución lógica", "casa": "Ravenclaw"},
                {"respuesta": "Proteger a los demás", "casa": "Hufflepuff"},
                {"respuesta": "Buscar una ventaja estratégica", "casa": "Slytherin"}
            ]
        },
        {
            "pregunta": "¿Qué animal prefieres como mascota?",
            "opciones": [
                {"respuesta": "León", "casa": "Gryffindor"},
                {"respuesta": "Águila", "casa": "Ravenclaw"},
                {"respuesta": "Tejón", "casa": "Hufflepuff"},
                {"respuesta": "Serpiente", "casa": "Slytherin"}
            ]
        },
        {
            "pregunta": "¿Cuál de estos colores prefieres?",
            "opciones": [
                {"respuesta": "Rojo", "casa": "Gryffindor"},
                {"respuesta": "Azul", "casa": "Ravenclaw"},
                {"respuesta": "Amarillo", "casa": "Hufflepuff"},
                {"respuesta": "Verde", "casa": "Slytherin"}
            ]
        }
    ]

    puntos = {"Gryffindor": 0, "Ravenclaw": 0, "Hufflepuff": 0, "Slytherin": 0}

    for pregunta in preguntas:
        casa = preguntar(pregunta["pregunta"], pregunta["opciones"])
        puntos[casa] += 1

    casa_ganadora = max(puntos, key=puntos.get)
    print(f"\n¡Felicidades! Has sido seleccionado para la casa {casa_ganadora}!")

if __name__ == "__main__":
    sombrero_seleccionador()