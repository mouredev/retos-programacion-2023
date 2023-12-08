# Reto #2: EL PARTIDO DE TENIS
#### Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23

## Enunciado

"""
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
"""
import sys

def ask_list ():
    return input("List Points: ").lower()

def convert_str_list(string):
    return string.split(",")
    
def check_errors_lista(lista):
    for point in lista:
        match point:
            case "p1":
                continue
            case "p2":
                continue
            case _:
                return False
    return True

def print_points(lista):
    points_p1 = 0
    points_p2 = 0
    stringp1 = ""
    stringp2 = ""
    Deuce = False
    Ventaja = False
    v1 = False
    v2 = False
    for point in lista:
        match point:
            case "p1":
                points_p1 += 1
            case "p2":
                points_p2 += 1
        match points_p1:
            case 0:
                stringp1= "Love"
            case 1:
                stringp1= "15"
            case 2:
                stringp1= "30"
            case 3:
                stringp1= "40"
            case 4:
                stringp1= "game"
        match points_p2:
            case 0:
                stringp2= "Love"
            case 1:
                stringp2= "15"
            case 2:
                stringp2= "30"
            case 3:
                stringp2= "40"
            case 4:
                stringp2= "game"
        
        if stringp2 == "40" and stringp1 == "40":
            Deuce = True
            print("Deuce")
        elif Deuce == True and Ventaja != True:
            
            if point == "p1":
                v1 = True
                print("Ventaja P1")
            elif point == "p2":
                v2 = True
                print("Ventaja P2")
            Ventaja = True
            Deuce = False
        elif Ventaja == True:
            if point =="p1" and v1 == True:
                print("Ha Ganado el Player 1")
            elif point =="p1" and v2 == True:
                print("Deuce")
                v2 = False
                Deuce = True
                Ventaja = False
            elif point == "p2" and v2 == True:
                print("Ha ganado el Player 2")
            elif point == "p2" and v2 == False:
                print("Deuce")
                v1 = False
                Deuce = True
                Ventaja = False
        else:
            if stringp1 == "game":
                print("Ha ganado el Player 1")
                break
            elif stringp2 == "game":
                print("Ha ganado el Player 2")
                break
            else:
                print(f"{stringp1} - {stringp2}")
    
    
def main():
    string_lista = ask_list()
    lista = convert_str_list(string_lista)
    if check_errors_lista(lista):
        print_points(lista)
    else: 
        print("Has introducido los datos incorrectamente: Ex. p1,p2,p2,p1")
        
if __name__=="__main__":
    main()