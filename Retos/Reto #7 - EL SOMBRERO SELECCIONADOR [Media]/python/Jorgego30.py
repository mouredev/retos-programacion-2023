"""
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo magico de Harry Potter.
 * - De ser posible realizara 5 preguntas (como minimo) a traves de la terminal.
 * - Cada pregunta tendra 4 respuestas posibles (tambien a selecciona una a traves de terminal).
 * - En funcion de las respuestas a las 5 preguntas deberas diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambicion y la astucia.


Preguntas:
    1- ¿Cual de estos rasgos es mas importante para ti en un amigo?
    2- ¿Cual de estos libros te interesaria mas leer?
    3- ¿Cual de estos deportes preferirias jugar?
    4- ¿Que opinas sobre probar nuevos alimentos o platos?
    5- ¿Que opinas sobre viajar a paises desconocidos?
Gryffindor:
    a) Coraje y valentia
    a) Un libro sobre deportes extremos y aventuras 
    a) Escalada en roca o paracaidismo 
    a) Me encanta probar cosas nuevas y diferentes
    a) Me emociona explorar nuevos lugares y culturas
Slytherin:
    b) Ambicion y exito 
    b) Un libro sobre emprendimiento y negocios
    b) Tenis o golf
    b) Solo pruebo cosas nuevas si tienen buena reputacion 
    b) Solo viajaria a paises seguros y con buena reputacion
Ravenclaw:
    c) Inteligencia y curiosidad
    c) Un libro sobre ciencia o tecnologia
    c) Esqui o snowboard
    c) Me gusta probar nuevos sabores y platos de diferentes culturas
    c) Me encanta viajar y descubrir cosas nuevas
Huffepluf:
    d) Honestidad y lealtad
    d) Un libro sobre relaciones y emociones humanas
    d) Natacion o ciclismo
    d) Me gusta comer lo que ya conozco y me gusta 
    d) Me gusta viajar a lugares conocidos o a los que he visitado antes 
"""

print("¿Quieres comenzar el test? (y/n)") 
test=input()
if (test=="y"):
    r1=""
    r2=""
    r3=""
    r4=""
    r5=""
    print("\nPrimera pregunta")
    print("\n¿Cual de estos rasgos es mas importante para ti en un amigo?")
    print("a) Coraje y valentia")
    print("b) Ambicion y exito ")
    print("c) Inteligencia y curiosidad")
    print("d) Honestidad y lealtad")
    r1=input()

    print("\nSegunda pregunta")
    print("\n¿Cual de estos libros te interesaria mas leer?")
    print("a) Un libro sobre deportes extremos y aventuras")
    print("b) Un libro sobre emprendimiento y negocios ")
    print("c) Un libro sobre ciencia o tecnologia")
    print("d) Un libro sobre relaciones y emociones humanas")
    r2=input()

    print("\nTercera pregunta")
    print("\n¿Cual de estos deportes preferirias jugar?")
    print("a) Escalada en roca o paracaidismo ")
    print("b) Tenis o golf")
    print("c) Esqui o snowboard")
    print("d) Natacion o ciclismo")
    r3=input()

    print("\nCuarta pregunta")
    print("\n¿Que opinas sobre probar nuevos alimentos o platos?")
    print("a) Me encanta probar cosas nuevas y diferentes")
    print("b) Solo pruebo cosas nuevas si tienen buena reputacion ")
    print("c) Me gusta probar nuevos sabores y platos de diferentes culturas")
    print("d) Me gusta comer lo que ya conozco y me gusta")
    r4=input()

    print("\nQuinta pregunta")
    print("\n¿Que opinas sobre viajar a paises desconocidos?")
    print("a) Me emociona explorar nuevos lugares y culturas")
    print("b) Solo viajaria a paises seguros y con buena reputacion")
    print("c) Me encanta viajar y descubrir cosas nuevas")
    print("d) Me gusta viajar a lugares conocidos o a los que he visitado antes")
    r5=input()

    gry=0
    sly=0
    rav=0
    huff=0

    if(r1=="a"):
        gry+1
    elif(r1=="b"):
        sly+1
    elif(r1=="c"):
        rav+1
    elif(r1=="d"):
        huff+1
    elif(r2=="a"):
        gry+1
    elif(r2=="b"):
        sly+1
    elif(r2=="c"):
        rav+1
    elif(r2=="d"):
        huff+1
    elif(r3=="a"):
        gry+1
    elif(r3=="b"):
        sly+1
    elif(r3=="c"):
        rav+1
    elif(r3=="d"):
        huff+1
    elif(r4=="a"):
        gry+1
    elif(r4=="b"):
        sly+1
    elif(r4=="c"):
        rav+1
    elif(r4=="d"):
        huff+1
    elif(r5=="a"):
        gry+1
    elif(r5=="b"):
        sly+1
    elif(r5=="c"):
        rav+1
    elif(r5=="d"):
        huff+1
        

    if(gry>sly and gry>rav and gry>huff):
        print( "\nPerteneces a Gryffindor, felicidades")
    elif(sly>gry and sly>rav and sly>huff):
        print("\nPerteneces a Slytherin, felicidades")
    elif(rav>gry and rav>sly and rav>huff):
        print("\nPerteneces a Ravenclaw, felicidades")
    elif(huff>gry and huff>sly and huff>rav):
        print("\nPerteneces a Hufflepuff, felicidades")
        

else :
    print("Muggle...")
    
