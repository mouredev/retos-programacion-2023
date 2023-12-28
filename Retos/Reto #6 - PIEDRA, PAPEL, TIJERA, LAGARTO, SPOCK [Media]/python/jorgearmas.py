"""
 Crea un programa que calcule quien gana más partidas al piedra, papel, tijera, lagarto, spock.
  - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
  - La función recibe un listado que contiene pares, representando cada jugada.
  - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
    "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
  - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
  - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
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
        return("Player 1 Gano la partida 🎉")
    elif p1 < p2:
        return("Player 2 Gano la partida 🚀")
    elif p1 == p2:
        return("Tie 😅")

def game(option_1, option_2, points_player_1, points_player_2):
    if option_1 == option_2:
        print("***TIE***😆")
        points_player_1 = 1
        points_player_2 = 1
    elif option_1 == "PIEDRA": #PIEDRA
        if option_2 == "LAGARTO":
            print("Piedra 🗿 aplasta a lagarto 🦎 / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "TIJERA":
            print("Piedra 🗿 aplasta a Tijera ✂️ / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "PAPEL":
            print("Papel 📄 envuelve a Piedra 🗿 / Gano jugador 2")
            points_player_2 = 1
        elif option_2 == "SPOCK":
            print("Spock 🖖 vaporiza a Piedra 🗿 / Gano jugador 2")
            points_player_2 = 1
    elif option_1 == "PAPEL": #PAPEL
        if option_2 == "SPOCK":
            print("Papel 📄 desautoriza a Spock 🖖 / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "PIEDRA":
            print("Papel 📄 envuelve a Piedra 🗿 / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "TIJERA":
            print("Tijera ✂️ corta a Papel 📄 / Gano jugador 2")
            points_player_2 = 1
        elif option_2 == "LAGARTO":
            print("Lagarto 🦎 devora al Papel 📄 / Gano jugador 2")
            points_player_2 = 1
    elif option_1 == "TIJERA": #TIJERA
        if option_2 == "LAGARTO":
            print("Tijera ✂️ decapita a Lagarto 🦎 / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "PAPEL":
            print("Tijera ✂️ corta a Papel 📄 / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "SPOCK":
            print("Spock 🖖 rompe a Tijera ✂️ / Gano jugador 2")
            points_player_2 = 1
        elif option_2 == "PIEDRA":
            print("Piedra 🗿 aplasta a Tijera ✂️ / Gano jugador 2")
            points_player_2 = 1
    elif option_1 == "LAGARTO": #LAGARTO
        if option_2 == "SPOCK":
            print("Lagarto 🦎 envenena a Spock 🖖/ Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "PAPEL":
            print("Lagarto 🦎 devora al Papel 📄 / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "TIJERA":
            print("Tijera ✂️ decapita a Lagarto 🦎 / Gano jugador 2")
            points_player_2 = 1
        elif option_2 == "PIEDRA":
            print("Piedra 🗿 aplasta a lagarto 🦎 / Gano jugador 2")
            points_player_2 = 1
    elif option_1 == "SPOCK": #SPOCK
        if option_2 == "TIJERA":
            print("Spock 🖖 rompe a Tijera ✂️ / Gano jugador 1")
            points_player_1 = 1
        elif option_2 == "PIEDRA":
            print("Spock 🖖 vaporiza a Piedra 🗿 / Gano jugador 1")
            points_player_1 = 1           
        elif option_2 == "PAPEL":
            print("Papel 📄 desautoriza a Spock 🖖 / Gano jugador 2")
            points_player_2 = 1
        elif option_2 == "LAGARTO":
            print("Lagarto 🦎 envenena a Spock 🖖/ Gano jugador 2")
            points_player_2 = 1

    return(points_player_1, points_player_2)


if __name__ == "__main__":
    print("-"*51)
    print("Piedra 🗿, Papel 📄, Tijera ✂️, Lagarto 🦎, Spock 🖖")
    print("-"*51)
    points_f = []
    final_r = ""
    session = "yes"
    while session == "yes":
        while counter < 2:
            counter += 1
            option_player_1 = stringValidation(input("Ingrese opción jugador 1: "))
            print(f"Seleccion -> {option_player_1}")
            option_player_2 = stringValidation(input("Ingrese opción jugador 2: "))
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

