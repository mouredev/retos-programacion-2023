"""
* Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 
"""
questions=["""
¿Cuál de estos rasgos es más importante para ti en un amigo?
a) Coraje y valentía (osadía)
b) Ambición y éxito (ambición)
c) Inteligencia y curiosidad (curiosidad)
d) Honestidad y lealtad (lealtad)""",

"""
¿Cuál de estos libros te interesaría más leer?
a) Un libro sobre deportes extremos y aventuras (osadía)
b) Un libro sobre emprendimiento y negocios (ambición)
c) Un libro sobre ciencia o tecnología (curiosidad)
d) Un libro sobre relaciones y emociones humanas (lealtad)
""",
"""
¿Cuál de estos deportes preferirías jugar?
a) Escalada en roca o paracaidismo (osadía)
b) Tenis o golf (ambición)
c) Esquí o snowboard (curiosidad)
d) Natación o ciclismo (lealtad)
""",
"""
¿Qué opinas sobre probar nuevos alimentos o platos?
a) Me encanta probar cosas nuevas y diferentes (osadía)
b) Solo pruebo cosas nuevas si tienen buena reputación (ambición)
c) Me gusta probar nuevos sabores y platos de diferentes culturas (curiosidad)
d) Me gusta comer lo que ya conozco y me gusta (lealtad)
""",

"""¿Qué opinas sobre viajar a países desconocidos?
a) Me emociona explorar nuevos lugares y culturas (osadía)
b) Solo viajaría a países seguros y con buena reputación (ambición)
c) Me encanta viajar y descubrir cosas nuevas (curiosidad)
d) Me gusta viajar a lugares conocidos o a los que he visitado antes (lealtad)
""",
"""
¿Qué te motiva a realizar una tarea o proyecto?
a) El desafío de hacer algo difícil (osadía)
b) La posibilidad de obtener una recompensa o logro (ambición)
c) El deseo de aprender algo nuevo (curiosidad)
d) La satisfacción de ayudar a alguien o ser útil (lealtad)
""",
"""¿Cuál es tu mayor miedo?
a) No ser lo suficientemente valiente en una situación difícil (osadía)
b) No tener éxito en la vida (ambición)
c) No conocer o aprender lo suficiente sobre el mundo (curiosidad)
d) Perder a alguien que amo o ser traicionado (lealtad)
"""]

osadia =0
ambición=0
curiosidad=0
lealtad=0

def puntos(ans):
    
    global osadia
    global ambición
    global curiosidad
    global lealtad
    
    if ans=="a":
        osadia=osadia+1
    if ans=="b":
        ambición+=1
    if ans=="c":
        curiosidad+=1
    if ans=="d":
        lealtad+=1
    return (osadia, ambición, curiosidad, lealtad)

def sombrero(osadia, ambición, curiosidad, lealtad):
    if osadia > ambición and osadia > curiosidad and osadia > lealtad:
        return "Tu casa será Gryffindor"
    if ambición > osadia and ambición > curiosidad and ambición > lealtad:
        return "Tu casa será Slytherin"
    if curiosidad > ambición and curiosidad > osadia and curiosidad > lealtad:
        return "Tu casa será Ravenclaw"
    if lealtad > ambición and lealtad > curiosidad and lealtad > osadia:
        return "Tu casa será Hufflepuff"

if __name__=="__main__":
    for question in questions:
        print(question)
        answer=input().lower()
        
        
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("type a valid option")
            answer=input()
        

        a,b,c,d=puntos(answer)
        #print(a,b,c,d)
    print(sombrero(a,b,c,d))

