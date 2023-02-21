# Crea un programa que simule el comportamiento del sombrero selccionador del
# universo mágico de Harry Potter.
# - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
# - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
# - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
# - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#   Por ejemplo, en Slytherin se premia la ambición y la astucia.

# Gryffindor: Valentía, coraje y determinación. Temerarios y arriesgados, con espíritu aventurero y capacidad para enfrentar el peligro.
# Hufflepuff: Lealtad, honestidad y trabajo duro. Amables y pacientes, con ética y capacidad para trabajar en equipo.
# Ravenclaw: Inteligencia, sabiduría y creatividad. Curiosos y perspicaces, con capacidad para resolver problemas y pensar de manera innovadora.
# Slytherin: Astucia, ambición y determinación. Astutos y persuasivos, con capacidad para lograr sus objetivos y gran ingenio.

# He decidido la puntuación como una suma del numero de la respuesta. El 1 corresponde a un supuesto Gryffindor, el 2 a Hufflepuff, 3 a Ravenclaw, y 4 a Slytherin
# Al final se hace una suma y depende de la puntuación será una casa o otra
# Hay texto entre medias para meterle mas lore a la elección, espero os guste B-)

def func_sombrero_seleccionador():
    respuestas = ["1", "2", "3", "4"]
    print("|Cuando vayas a contestar una pregunta, responde '1', '2', '3' o '4'|")
    
    nombre = input("¿Cual es tu nombre?\n")
    print(f"Asi que eres {nombre}, encantado, soy el sombrero seleccionador, bienvenidx a HOGWARTS")
    print("-----------------------------")
    print("Primera pregunta que te propongo: Si te viene un troll gigante, cual de estas 4 situaciones crees que harias")
    p1 = input("1- Atacar con tus hechizos\n2- Tratar de unir fuerzas con tus compañeros y atacar juntos\n3- Pensar una forma rapida y viable de acabar con el troll\n4- Huir antes de que murais todos\n-> ")
    if p1 not in respuestas:
        print("Error, respuesta mal marcada")
        return
    print("¿Seguro? No te noto muy convencido...")
    print("-----------------------------")
    p2 = input("¿Qué valores son más importantes para ti?\n1- La valentía\n2- El trabajo duro\n3- La creatividad\n4- La ambición\n-> ")
    if p2 not in respuestas:
        print("Error, respuesta mal marcada")
        return
    print("Aja... Ya veo")
    print("-----------------------------")
    p3 = input("Si te dieran a elegir entre estas 4 pociones cual elegirías\n1- Poción del amor\n2- Poción para volar\n3- Poción de invisibilidad\n4- Poción de velocidad\n-> ")
    if p3 not in respuestas:
        print("Error, respuesta mal marcada")
        return
    print("Mmm... curiosete")
    print("-----------------------------")
    p4 = input("¿Cual crees que es la cualidad de los tuyos(tus compañeros)?\n1- Ayudarte en la peor situación\n2- Apoyarte y guiarte para ser mejor\n3- Que este siempre para ti\n4- Compartir los mismos objetivos\n-> ")
    if p4 not in respuestas:
        print("Error, respuesta mal marcada")
        return
    print("Muy bonito, claro que si")
    print("-----------------------------")
    print("Aja, ya es tu ultima pregunta, ahi va. ¿Estas preparado? Porque aqui viene:")
    p5 = input("¿Con que conocimientos quieres acabar una vez finalizado el curso?\n1- Dominar la transformación en cualquier animal\n2- La maestria de las pociones como ningun otro mago\n3- Conocimiento de todo tipo de hechizos y magia antigua y moderna\n4- Maestria en defensa de las artes oscuras\n-> ")
    if p5 not in respuestas:
        print("Error, respuesta mal marcada")
        return
    print("Mm... Difícil... Te noto buenas cualidades")
    print("-----------------------------")
    p1 = int(p1)
    p2 = int(p2)
    p3 = int(p3)
    p4 = int(p4)
    p5 = int(p5)
    pfinal = p1 + p2 + p3 + p4 + p5
    # Puntuación minima = 5, puntuación maxima = 20
    # 5-8 Gryffindor, 9-12 Hufflepuff, 13-16 Ravenclaw, 17-20 Slytherin
    if pfinal >= 5 and pfinal <= 8:
            casa = "¡GRYFFINDOR!"
    if pfinal >= 9 and pfinal <= 12:
            casa = "¡HUFFLEPUFF!"
    if pfinal >= 13 and pfinal <= 16:
            casa = "¡RAVENCLAW!"
    if pfinal >= 17 and pfinal <= 20:
            casa = "¡SLYTHERIN!"

    input("¿Ultimo mensaje antes de que seleccione tu casa de aqui hasta el final del curso en Hogwarts?\n-> ")
    print("Bueno, eso ha estado bastante bien")
    print("Tu casa será...")
    print(casa)
    return

func_sombrero_seleccionador()