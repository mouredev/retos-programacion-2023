def calcular_puntuacion(juego):
    puntuaciones = {
        0: "Love",
        15: "15",
        30: "30",
        40: "40"
    }
    
    p1_puntos = 0
    p2_puntos = 0
    p1_ventaja = False
    p2_ventaja = False
    
    for punto in juego:
        if punto == "P1":
            if p1_puntos == 40 and not p1_ventaja:
                if p2_ventaja:
                    p2_ventaja = False
                else:
                    p1_ventaja = True
            elif p1_puntos == 40 and p1_ventaja:
                return "Ha ganado el P1"
            else:
                p1_puntos += 15
        elif punto == "P2":
            if p2_puntos == 40 and not p2_ventaja:
                if p1_ventaja:
                    p1_ventaja = False
                else:
                    p2_ventaja = True
            elif p2_puntos == 40 and p2_ventaja:
                return "Ha ganado el P2"
            else:
                p2_puntos += 15
                
        if p1_puntos == 40 and p2_puntos == 40:
            p1_puntos = "Deuce"
            p2_puntos = "Deuce"
        
        p1_puntos_str = puntuaciones.get(p1_puntos, "Love")
        p2_puntos_str = puntuaciones.get(p2_puntos, "Love")
        
        print(f"{p1_puntos_str} - {p2_puntos_str}")
    
    return "El juego ha finalizado"


secuencia = ["P1", "P1", "P1", "P1", "P1", "P2", "P2", "P2"]
resultado = calcular_puntuacion(secuencia)
print(resultado)
