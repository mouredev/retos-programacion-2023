puntuacionT = 0

def puntos(respuesta):
    if respuesta == "a":
        puntuacion = 1
    elif respuesta == "b":
        puntuacion = 2
    elif respuesta == "c":
        puntuacion = 3
    elif respuesta == "d":
        puntuacion = 4
    
    return puntuacion

def casa(puntuacionT):
    if puntuacionT < 5:
        return "Tu casa será Hufflepuff."
    elif puntuacionT < 10:
        return "Tu casa será Ravenclaw."
    elif puntuacionT < 15:
        return "Tu casa será Gryffindor."
    elif puntuacionT < 20:
        return "Tu casa será Slytherin."


print("-------- Pregunta 1 --------")
print("¿Qué valoras más en la vida? \n a) La amistad y la lealtad \n b) El conocimiento y la sabiduría \n c) La valentía y el coraje \n d) La ambición y el ingenio")
respuesta = input(print("Elije tu respuesta: "))
puntuacionT += puntos(respuesta)

print("-------- Pregunta 2 --------")
print("¿Qué habilidad mágica te gustaría dominar? \n a) La transformación de objetos y animales \n b) La adivinación y la lectura de la mente \n c) El conjuro de hechizos poderosos \n d) La habilidad de volar y la magia del movimiento")
respuesta = input(print("Elije tu respuesta: "))
puntuacionT += puntos(respuesta)

print("-------- Pregunta 3 --------")
print("¿Cuál es tu mayor miedo? \n a) La soledad y el aislamiento \n b) El fracaso y la decepción \n c) La injusticia y la opresión \n d) La falta de control y el caos")
respuesta = input(print("Elije tu respuesta: "))
puntuacionT += puntos(respuesta)

print("-------- Pregunta 4 --------")
print("¿Qué tipo de entorno te hace sentir más cómodo? \n a) Un lugar tranquilo y pacífico \n b) Un lugar lleno de libros y conocimiento \n c) Un lugar lleno de acción y aventura \n d) Un lugar lleno de desafíos y oportunidades")
respuesta = input(print("Elije tu respuesta: "))
puntuacionT += puntos(respuesta)

print("-------- Pregunta 5 --------")
print("¿Cuál de estas cualidades crees que te describe mejor? \n a) Amable y generoso \n b) Inteligente y curioso \n c) Valiente y decidido \n d) Astuto y ambicioso")
respuesta = input(print("Elije tu respuesta: "))
puntuacionT += puntos(respuesta)

print(puntuacionT)
print(casa(puntuacionT))