#https://www.gotoquiz.com/prueba_del_sombrero_seleccionador
def sombrero_seleccionador():
    respuesta = []
    valor_respuestas = {"A":10, "B":8, "C":6, "D":4}

    print("\nHola soy el Sombrero Seleccionador Por Favor selecciona tu respuesta a cada pregunta")
    print("Escribe A, B, C, o D segun sea tu respuesta\n")
    
    print("1.- Dada la opción, preferirías inventar una poción que garantizara?:")
    respuesta += input("A: Gloria" "\nB: Sabiduria" "\nC: Amor" "\nD: Poder" "\nDigita tu Respuesta: ")

    print("\n2.- Si pudieras tener algún poder, ¿cuál elegirías?")
    respuesta += input("A: El poder de leer la mente" "\nB: El poder de la invisibilidad" "\nC: El poder de la fuerza sobrehumana" "\nD: El poder de cambiar tu apariencia a voluntad" "\nDigita tu Respuesta: ")

    print("\n3.- ¿Cuál de los siguientes te gustaría estudiar más?")
    respuesta += input("A: Centauros" "\nB: Duendes" "\nC: Fantasmas" "\nD: Trolls" "\nDigita tu Respuesta: ")

    print("\n4.- Una vez cada siglo, el arbusto Flutterby produce flores que adaptan su aroma para atraer a los desprevenidos. Si te atrajera, olería a:")
    respuesta += input("A: Una chimenea crepitante" "\nB: Pergamino fresco" "\nC: Tu hogar" "\nD: El mar" "\nDigita tu Respuesta: ")

    print("\n5.- Si pudieras tener algún poder, ¿cuál elegirías?")
    respuesta += input("A: El poder de leer la mente" "\nB: El poder de la invisibilidad" "\nC: El poder de la fuerza sobrehumana" "\nD: El poder de cambiar tu apariencia a voluntad" "\nDigita tu Respuesta: ")

    
    resultado = 0
    for i in respuesta:
        
        if i.upper() in valor_respuestas.keys():    
            resultado += valor_respuestas[i.upper()]
        print(resultado)

    if resultado <= 50  and resultado > 45 :
        print("Perteneces a la casa de Hufflepuff")   
    elif resultado <= 45 and resultado > 38:
        print("Perteneces a la casa de Ravenclaw") 
    elif resultado <= 38 and resultado > 31:
        print("Perteneces a la casa de Slytherin")
    else:
        print("Perteneces a la casa de Gryffindor")
sombrero_seleccionador()

