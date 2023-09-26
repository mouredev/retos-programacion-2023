# RETO 7 de "MoureDev" 2023.

"""
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo 
 *  que coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
"""
# Introducción.
puntuacion = 0
print('\nSe te van a hacer una serie de preguntas para saber a que casa de Hogwarts perteneces. Tendrás que responder con "A, B, C o D"\n\n')

# Preguntas.
Pregunta1 = input("¿Cuál de estas características crees que te define mejor?\nA) Lealtad\nB) Inteligencia\nC) Ambición\nD) Valentía\n\n")
print(" ")
if Pregunta1.lower() == "a":
    puntuacion += 30
elif Pregunta1.lower() == "b":
    puntuacion += 20
elif Pregunta1.lower() == "c":
    puntuacion += 10
elif Pregunta1.lower() == "d":
    puntuacion += 40
else:
    print("Elige una opción adecuada")
    exit()
        
Pregunta2 = input("¿Si tuvieras que elegir una mascota, cuál sería?\nA) Una rata\nB) Una lechuza\nC) Un gato\nD) Un sapo\n\n")
print(" ")
if Pregunta2.lower() == "a":
    puntuacion += 10
elif Pregunta2.lower() == "b":
    puntuacion += 40
elif Pregunta2.lower() == "c":
    puntuacion += 20
elif Pregunta2.lower() == "d":
    puntuacion += 30
else:
    print("Elige una opción adecuada")
    exit()
    
Pregunta3 = input("¿Has copiado o has hecho trampas alguna vez en un examen\nA) Si!\nB) No!\n\n")
print(" ")
if Pregunta3.lower() == "a":
    puntuacion += 10
elif Pregunta3.lower() == "b":
    puntuacion += 40
else:
    print("Elige una opción adecuada")
    exit()
    
Pregunta4 = input("Si jugases al famoso juego de Harry Potter llamado 'Quidditch',¿Cuál crees que serías tú en el equipo?\nA) Sería un cazador/a\nB) Sería un golpeador/a\nC) Sería un guardian/a\nD) Sería un buscador/a\n\n")
print(" ")
if Pregunta4.lower() == "a":
    puntuacion += 30
elif Pregunta4.lower() == "b":
    puntuacion += 10
elif Pregunta4.lower() == "c":
    puntuacion += 40
elif Pregunta4.lower() == "d":
    puntuacion += 20
else:
    print("Elige una opción adecuada")
    exit() 
       
Pregunta5 = input("Escoge un animal:\nA) Un león\nB) Un tejón\nC) Un águila\nD) Una serpiente\n\n")
print(" ")
if Pregunta5.lower() == "a":
    puntuacion += 40
elif Pregunta5.lower() == "b":
    puntuacion += 30
elif Pregunta5.lower() == "c":
    puntuacion += 20
elif Pregunta5.lower() == "d":
    puntuacion += 10
else:
    print("Elige una opción adecuada")
    exit()
    
Pregunta6 = input("Si estudiases en Hogwarts, ¿Dónde preferirías que estuviese tu dormitorio?\nA) En las mazmorras\nB) En una torre del castillo\nC) Cerca de la cocina\nD) En el centro del castillo\n\n")
print(" ")
if Pregunta6.lower() == "a":
    puntuacion += 10
elif Pregunta6.lower() == "b":
    puntuacion += 20
elif Pregunta6.lower() == "c":
    puntuacion += 30
elif Pregunta6.lower() == "d":
    puntuacion += 40
else:
    print("Elige una opción adecuada")    
    exit()
    
Pregunta7 = input("¿Cuál de estas asignaturas escogerías si estudiaras en Hogwarts?\nA) El estudio de las pociones\nB) Las transformaciones\nC) La historia de la magia\nD) La astronomía\n\n")
print(" ")
if Pregunta7.lower() == "a":
    puntuacion += 30
elif Pregunta7.lower() == "b":
    puntuacion += 10
elif Pregunta7.lower() == "c":
    puntuacion += 40
elif Pregunta7.lower() == "d":
    puntuacion += 20
else:
    print("Elige una opción adecuada")
    exit()
    
Pregunta8 = input("Elige un color:\nA) Rojo\nB) Amarillo\nC) Azul\nD) Verde\n\n")
print(" ")
if Pregunta8.lower() == "a":
    puntuacion += 40
elif Pregunta8.lower() == "b":
    puntuacion += 30
elif Pregunta8.lower() == "c":
    puntuacion += 20
elif Pregunta8.lower() == "d":
    puntuacion += 10
else:
    print("Elige una opción adecuada")
    exit()
    
Pregunta9 = input("Te miras en el espejo de 'Oesed' y ves tu futuro, ¿Cómo te ves?\nA) Con mucho dinero\nB) Rodeado de mis seres queridos\nC) Siendo un mago importante\nD) Viviendo una increíble aventura\n\n")
print(" ")
if Pregunta9.lower() == "a":
    puntuacion += 10
elif Pregunta9.lower() == "b":
    puntuacion += 30
elif Pregunta9.lower() == "c":
    puntuacion += 20
elif Pregunta9.lower() == "d":
    puntuacion += 40
else:
    print("Elige una opción adecuada")
    exit()  
      
Pregunta10 = input("¿Que harías cuando terminases tus estudios en Hogwarts?\nA) Tendría una familia\nB) Me uniría al ministerio de magia\nC) Seguiría estudiando de otra forma\nD) Me iría de viaje a recorrer el mundo\n\n")
print(" ")
if Pregunta10.lower() == "a":
    puntuacion += 10
elif Pregunta10.lower() == "b":
    puntuacion += 30
elif Pregunta10.lower() == "c":
    puntuacion += 20
elif Pregunta10.lower() == "d":
    puntuacion += 40   
else:
    print("Elige una opción adecuada")
    exit()
     
# Relleno.
print("Redoble de tambores...\n\n")

# Averiguar la casa en función de los puntos obtenidos anteriormente
if puntuacion >= 330:
        print("Eres de Gryffindor.\nEres conocido por tu valentía, coraje, determinación y espíritu de aventura. Los Gryffindor son audaces y arriesgados, y no temen enfrentarse a los peligros para proteger a los demás.\n")
elif puntuacion >= 260:
        print("Eres de Hufflepuff.\nEres valorado por tu lealtad, paciencia, trabajo duro y amistad. Los Hufflepuff son considerados cálidos, amables y generosos, y aprecian la honestidad y la justicia.\n")   
elif puntuacion >= 180:
        print("Eres de Ravenclaw.\nEres conocido por tu inteligencia, creatividad, sabiduría y amor por el aprendizaje. Los Ravenclaw son curiosos, lógicos y disfrutan de los desafíos mentales.\n")
else:
        print("Eres de Slytherin.\nEres valorado por tu astucia, determinación, ambición y liderazgo. Los Slytherin son considerados astutos y ambiciosos, y aprecian la grandeza y el poder.\n")
# Final.
print("Tu puntuación final ha sido de: " + str(puntuacion))
print(" ")

# Para un archivo .exe (Qué no se salga automaticamente sin dar el resultado)
print(input("Test terminado, introduzca cualquier tecla para terminar: "))