# # Reto #7: El sombrero seleccionador
# #### Dificultad: Media | Publicación: 13/02/23 | Corrección: 20/02/23

# ## Enunciado

# ```
# /*
#  * Crea un programa que simule el comportamiento del sombrero seleccionador del
#  * universo mágico de Harry Potter.
#  * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
#  * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
#  * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#  *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
#  * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#  *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
#  */
# ```
# #### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

# Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

# > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.


# # Reto #7: El sombrero seleccionador
# #### Dificultad: Media | Publicación: 13/02/23 | Corrección: 20/02/23

# ## Enunciado

# ```
# /*
#  * Crea un programa que simule el comportamiento del sombrero seleccionador del
#  * universo mágico de Harry Potter.
#  * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
#  * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
#  * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#  *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
#  * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#  *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
#  */
# ```
# #### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

# Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

# > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.


import random

def main():
    print("Reto 7")
    print("Responde a las siguientes preguntas para determinar a qué casa perteneces:")

    preguntas = [
        ("¿Qué cualidad valoras más en un amigo?", ["a) Valentía", "b) Astucia", "c) Lealtad", "d) Inteligencia"]),
        ("¿Qué animal te representa mejor?", ["a) León", "b) Serpiente", "c) Tejón", "d) Águila"]),
        ("¿Qué tipo de magia prefieres?", ["a) Ofensiva", "b) Sigilosa", "c) Curativa", "d) Analítica"]),
        ("¿Qué harías si encontraras una cartera perdida?", ["a) La devolvería sin dudarlo", "b) La devolvería si me beneficia", "c) La devolvería después de asegurarme de que está vacía", "d) La tomaría como propia"]),
        ("¿Qué lugar te atrae más?", ["a) Bosque oscuro", "b) Mazmorras", "c) Campo abierto", "d) Biblioteca"]),
    ]

    respuestas = []

    for pregunta, opciones in preguntas:
        print("\n" + pregunta)
        for opcion in opciones:
            print(opcion)
        respuesta = input("Elige una opción (a-d): ").lower()
        while respuesta not in ['a', 'b', 'c', 'd']:
            print("Por favor, elige una opción válida (a-d).")
            respuesta = input("Elige una opción: ").lower()
        respuestas.append(ord(respuesta) - ord('a'))

    casa = seleccionar_casa(respuestas)
    print("\nTu perteneces a la casa: " + casa)

def seleccionar_casa(respuestas):
    puntajes = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    for i, respuesta in enumerate(respuestas):
        if i == 0:  # Primera pregunta
            if respuesta == 0:  # Gryffindor
                puntajes["Gryffindor"] += 1
            elif respuesta == 1:  # Slytherin
                puntajes["Slytherin"] += 1
            elif respuesta == 2:  # Hufflepuff
                puntajes["Hufflepuff"] += 1
            elif respuesta == 3:  # Ravenclaw
                puntajes["Ravenclaw"] += 1
        elif i == 1:  # Segunda pregunta
            if respuesta == 0:  # Gryffindor
                puntajes["Gryffindor"] += 1
            elif respuesta == 1:  # Slytherin
                puntajes["Slytherin"] += 1
            elif respuesta == 2:  # Hufflepuff
                puntajes["Hufflepuff"] += 1
            elif respuesta == 3:  # Ravenclaw
                puntajes["Ravenclaw"] += 1
        elif i == 2:  # Tercera pregunta
            if respuesta == 0:  # Gryffindor
                puntajes["Gryffindor"] += 1
            elif respuesta == 1:  # Slytherin
                puntajes["Slytherin"] += 1
            elif respuesta == 2:  # Hufflepuff
                puntajes["Hufflepuff"] += 1
            elif respuesta == 3:  # Ravenclaw
                puntajes["Ravenclaw"] += 1
        elif i == 3:  # Cuarta pregunta
            if respuesta == 0:  # Gryffindor
                puntajes["Gryffindor"] += 1
            elif respuesta == 1:  # Slytherin
                puntajes["Slytherin"] += 1
            elif respuesta == 2:  # Hufflepuff
                puntajes["Hufflepuff"] += 1
            elif respuesta == 3:  # Ravenclaw
                puntajes["Ravenclaw"] += 1
        elif i == 4:  # Quinta pregunta
            if respuesta == 0:  # Gryffindor
                puntajes["Gryffindor"] += 1
            elif respuesta == 1:  # Slytherin
                puntajes["Slytherin"] += 1
            elif respuesta == 2:  # Hufflepuff
                puntajes["Hufflepuff"] += 1
            elif respuesta == 3:  # Ravenclaw
                puntajes["Ravenclaw"] += 1


    casa = max(puntajes, key=puntajes.get)
    return casa

if __name__ == "__main__":
    main()
