"""
 Crea un programa que calcule quien gana mรกs partidas al piedra, papel, tijera, lagarto, spock.
  - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
  - La funciรณn recibe un listado que contiene pares, representando cada jugada.
  - El par puede contener combinaciones de "๐ฟ" (piedra), "๐" (papel),
    "โ๏ธ" (tijera), "๐ฆ" (lagarto) o "๐" (spock).
  - Ejemplo. Entrada: [("๐ฟ","โ๏ธ"), ("โ๏ธ","๐ฟ"), ("๐","โ๏ธ")]. Resultado: "Player 2".
  - Debes buscar informaciรณn sobre cรณmo se juega con estas 5 posibilidades.
"""
#global vars
counter = 0
points_1 = 0 
points_2 = 0
lst_roles = ["PIEDRA","PAPEL","TIJERA","LAGARTO","SPOCK"]

def reset():
    return(0)

def stringValidation(inpt):
    election = inpt.upper()
    election = election.strip()
    if election in lst_roles:
        return(election)
    else:
        return(0)

def eval(p1, p2):
    if p1 > p2:
        return("Player 1 Gano la partida ๐")
    elif p1 < p2:
        return("Player 2 Gano la partida ๐")
    elif p1 == p2:
        return("Tie ๐")

def game(option_1, option_2, points_player_1, points_player_2):
    if option_1 == option_2:
        print("***TIE***๐")
        points_player_1 = 1
        points_player_2 = 1
    elif option_1 == "PIEDRA": #PIEDRA
        if option_2 == "LAGARTO":
            print("Piedra ๐ฟ aplasta a lagarto ๐ฆ / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "TIJERA":
            print("Piedra ๐ฟ aplasta a Tijera โ๏ธ / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "PAPEL":
            print("Papel ๐ envuelve a Piedra ๐ฟ / Gano jugador 2")
            points_player_2 = 1
        elif option_2 == "SPOCK":
            print("Spock ๐ vaporiza a Piedra ๐ฟ / Gano jugador 2")
            points_player_2 = 1
    elif option_1 == "PAPEL": #PAPEL
        if option_2 == "SPOCK":
            print("Papel ๐ desautoriza a Spock ๐ / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "PIEDRA":
            print("Papel ๐ envuelve a Piedra ๐ฟ / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "TIJERA":
            print("Tijera โ๏ธ corta a Papel ๐ / Gano jugador 2")
            points_player_2 = 1
        elif option_2 == "LAGARTO":
            print("Lagarto ๐ฆ devora al Papel ๐ / Gano jugador 2")
            points_player_2 = 1
    elif option_1 == "TIJERA": #TIJERA
        if option_2 == "LAGARTO":
            print("Tijera โ๏ธ decapita a Lagarto ๐ฆ / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "PAPEL":
            print("Tijera โ๏ธ corta a Papel ๐ / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "SPOCK":
            print("Spock ๐ rompe a Tijera โ๏ธ / Gano jugador 2")
            points_player_2 = 1
        elif option_2 == "PIEDRA":
            print("Piedra ๐ฟ aplasta a Tijera โ๏ธ / Gano jugador 2")
            points_player_2 = 1
    elif option_1 == "LAGARTO": #LAGARTO
        if option_2 == "SPOCK":
            print("Lagarto ๐ฆ envenena a Spock ๐/ Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "PAPEL":
            print("Lagarto ๐ฆ devora al Papel ๐ / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "TIJERA":
            print("Tijera โ๏ธ decapita a Lagarto ๐ฆ / Gano jugador 2")
            points_player_2 = 1
        elif option_2 == "PIEDRA":
            print("Piedra ๐ฟ aplasta a lagarto ๐ฆ / Gano jugador 2")
            points_player_2 = 1
    elif option_1 == "SPOCK": #SPOCK
        if option_2 == "TIJERA":
            print("Spock ๐ rompe a Tijera โ๏ธ / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "PIEDRA":
            print("Spock ๐ vaporiza a Piedra ๐ฟ / Gano jugador 1")
            points_player_1 = 1           
        elif option_2 == "PAPEL":
            print("Papel ๐ desautoriza a Spock ๐ / Gano jugador 2")
            points_player_2 = 1
        elif option_2 == "LAGARTO":
            print("Lagarto ๐ฆ envenena a Spock ๐/ Gano jugador 2")
            points_player_2 = 1

    return(points_player_1, points_player_2)


if __name__ == "__main__":
    print("-"*51)
    print("Piedra ๐ฟ, Papel ๐, Tijera โ๏ธ, Lagarto ๐ฆ, Spock ๐")
    print("-"*51)
    points_f = []
    final_r = ""
    session = "yes"
    while session == "yes":
        while counter < 2:
            counter += 1
            option_player_1 = stringValidation(input("Ingrese opciรณn jugador 1: "))
            print(f"Seleccion -> {option_player_1}")
            option_player_2 = stringValidation(input("Ingrese opciรณn jugador 2: "))
            print(f"Seleccion -> {option_player_2}")
            if option_player_1 == 0 or option_player_2 == 0:
                print("Opcion incorrecta")
                break
            else:
                points_f = game(option_player_1, option_player_2, points_1, points_2)
                points_1 += points_f[0]
                points_2 += points_f[1]

        if option_player_1 == 0 or option_player_2 == 0:
            session = input("\nLe gustaria continuar? (Escriba 'yes' o 'no') ")
            if session == "yes":
                counter = reset()
                points_1 = reset()
                points_2 = reset()
            else:
                exit()
        else:
            final_r =  eval(points_1, points_2)
            print(final_r)
            session = input("\nLe gustaria continuar? (Escriba 'yes' o 'no') ")
            if session == "yes":
                counter = reset()
                points_1 = reset()
                points_2 = reset()
            else:
                exit()

