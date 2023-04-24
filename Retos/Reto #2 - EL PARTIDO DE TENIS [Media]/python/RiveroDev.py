"""
Escribe un programa que muestre como transcurre un juego de tenis y quien lo ha ganado 
El programa recibira un a secuencia formada por P1 (Player 1) y P2 (Player 2), segun quien
gane cada punto del juego .


Las Puntuaciones de un juego son "Love" (Cero), 15 ,30 , 40, "Deuce" (Empate), ventaja.
Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraria lo siguiente.
15 -love
30- love
30 - 15
30 - 30
40 - 30
 Douce
P1 ventaja
P1 gana la partida
Si quieres, puede controlar errores en la entrada de datos.
Consulta las reglas del juego si tienes duda sobre el sistema de putos.
"""
secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2","P2"] #este es un ejemplo de entrada
puntos = {0: "love", 1:"15", 2:"30", 3:"40"}
p1 , p2 = 0 , 0 
for point in secuencia:
    if point == "P1":
        p1 += 1
    else: 
        p2 += 1
    
    if p1 == p2 >= 3 or p2 > 3 or p1 > 3:
        if p1 == p2 :
            print("Douce")
        elif p1 == p2 + 2:
            print("P1 gana la pártida")
            break
        elif p1 > p2 :
            print("P1 ventaja")
        elif p2 == p1 + 2:
            print("P2 gana la pártida")
            break
        elif p2 > p1 :
            print("P2 ventaja")
    else:
        print(f"{puntos[p1]} - {puntos[p2]}") 

## Notas
## Este ejercicio se puede modificar y usar el siclo while para usarlo indefinidas veces 
## O converfirlo en una funcion para solo tener que mandar un array y no necesitar del comando break
## Estar pendiente que si el array supera la logica del juego puede dar resulatdos que no son reales 
## como que , si ya se ganos la partida seguiria sumando o restando puntos al array asta que terminar el 
## ciclo 
