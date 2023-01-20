jugador = " "
juegoJugador1 = 0
juegoJugador2 = 0
resJugador1 = 0
resJugador2 = 0
res = 0
print("H")
while res != 0:
    print("Introduzca el jugador que ha ganado")
    jugador = input()
    if jugador == "jugador1":
        if(resJugador1 == 0):
            print("Jugador 1 => 0")
            resJugador1 = resJugador1 + 1
        elif(resJugador1 == 1):
            print("Jugador 1 => 15")
            resJugador1 = resJugador1 + 1
        elif(resJugador1 == 2):
            print("Jugador 1 => 30")
            resJugador1 = resJugador1 + 1
        elif(resJugador1 == 3):
            print("Jugador 1 => 40")
            resJugador1 = resJugador1 + 1
        elif(resJugador1 == 4):
            print("Jugador 1 => Juego")
            juegoJugador1 = juegoJugador1 + 1
            resJugador1 = 0
                
            print("FIN DEL JUEGO\nJugador 1 => " + juegoJugador1 +"\nJugador 2 => " + juegoJugador2)
    elif jugador == "jugador2":
        if(resJugador2 == 0):
            print("Jugador 2 => 0")
            resJugador2 = resJugador2 + 1
        elif(resJugador2 == 1):
            print("Jugador 2 => 15")
            resJugador2 = resJugador2 + 1
        elif(resJugador2 == 2):
            print("Jugador 2 => 30")
            resJugador2 = resJugador2 + 1
        elif(resJugador2 == 3):
            print("Jugador 2 => 30")
            resJugador2 = resJugador2 + 1
        elif(resJugador2 == 4):
            print("Jugador 2 => Juego")
            juegoJugador2 = juegoJugador2 + 1
            resJugador2 = 0
            print("FIN DEL JUEGO\nJugador 1 => " + juegoJugador1 +"\nJugador 2 => " + juegoJugador2)
    print("Pulse intro para continuar en caso contrario intrduzca $")
    res = input()