def mostrar_paratido(puntuaciones):
    jugadores = [P1, P2]

    for jugador in puntuaciones:
        jugador["anotacion"] += 1
        tabla = "{} - {}"

        for jugador in jugadores:
            match jugador["anotacion"]:
                case 1:
                    jugador["puntos"] = 15
                case 2:
                    jugador["puntos"] = 30
                case 3:
                    jugador["puntos"] = 40
                case 4:
                    jugador["puntos"] = 50
                case 5:
                    jugador["puntos"] = 60
        
        if jugadores[0]["puntos"] >= 40 and jugadores[1]["puntos"] >= 40:
            if jugadores[0]["puntos"] == 50:
                tabla = "Ventaja P1"
            elif jugadores[1]["puntos"] == 50:
                tabla = "Ventaja P2"
            
            if jugadores[0]["puntos"] == 60:
                tabla = "Ha ganado el P1"
            elif jugadores[1]["puntos"] == 60:
                tabla = "Ha ganado el P2"

            if jugadores[0]["puntos"] == jugadores[1]["puntos"]:
                tabla = "Deuce"

        print(tabla.format(P1['puntos'], P2['puntos']))

        if tabla.startswith("Ha ganado el "):
            break

P1 = {"anotacion": 0, "puntos": "Love"}
P2 = {"anotacion": 0, "puntos": "Love"}

mostrar_paratido([P1, P1, P2, P2, P1, P2, P1, P1])
