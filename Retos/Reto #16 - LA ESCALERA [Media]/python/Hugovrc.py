def escalera(escalones: int):
    
    if escalones == 0:
        print("__")

    if escalones > 0:
        espacio = "  "
        escalon_arriba = escalones * espacio
        print(escalon_arriba + " _")
        espacios = escalones
        for x in range(escalones):
            espacios -= 1
            espacio_entre_escalon = espacios * espacio
            print(espacio_entre_escalon + " _|")
        
    if escalones < 0:
        escalones = escalones * -1
        espacio = "  "
        print("_")
        for i in range(escalones):
            espacio_entre_escalon = i * espacio
            print(espacio_entre_escalon + " |_")

escalera(-7)
escalera(7)
escalera(0)