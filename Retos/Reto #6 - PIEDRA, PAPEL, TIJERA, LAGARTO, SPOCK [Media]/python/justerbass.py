"""
 Crea un programa que calcule quien gana mΓ‘s partidas al piedra,
 papel, tijera, lagarto, spock.
 El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 La funciΓ³n recibe un listado que contiene pares, representando cada jugada.
 El par puede contener combinaciones de "πΏ" (piedra), "π" (papel),
 "βοΈ" (tijera), "π¦" (lagarto) o "π" (spock).
 - Ejemplo. Entrada: [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ")]. Resultado: "Player 2".
 Debes buscar informaciΓ³n sobre cΓ³mo se juega con estas 5 posibilidades.
"""

def inicio():

    rules = "βοΈ corta a π, π cubre a πΏ, πΏ tritura a π¦, π¦ envena a π, π aplasta a βοΈ, βοΈ decapita a π¦, π¦ come a π, π desaprueba a π, π vaporiza a πΏ, πΏ tritura a βοΈ"

    input("ΒΏsaber las reglas de este juego?")
    print(f"da igual, las reglas son {rules}")

inicio()

def cachipun (p1_opcion, p2_opcion):
    opciones = ("πΏ", "π", "βοΈ", "π¦", "π")
    p1 = "player 1"
    p2 = "player 2"

    print(f"{p1} eligue {p1_opcion} y {p2} eligue {p2_opcion}")

    if not p1_opcion in opciones:  
        print("opcion no valida")
        print(f"las opciones a eleguir son {opciones}")
    if not p2_opcion in opciones:  
        print("opcion no valida")
        print(f"las opciones a eleguir son {opciones}")

    if p1_opcion == p2_opcion:
        print("Empate")

    elif p1_opcion == "πΏ":
        if p2_opcion == "βοΈ":
            print("πΏ tritura a βοΈ")
            print(f"{p1} gano")
        elif p2_opcion == "π¦":
            print("πΏ tritura a π¦")
            print(f"{p1} gano")
        elif p2_opcion == "π":
            print("π cubre a πΏ")
            print(f"{p2} gano")
        elif p2_opcion == "π":
            print("π vaporiza a πΏ")
            print(f"{p2} gano")

    elif p1_opcion == "π":
        if p2_opcion == "πΏ":
            print("π cubre a πΏ")
            print(f"{p1} gano")
        elif p2_opcion == "π":
            print("π desaprueba a π")
            print(f"{p1} gano")
        elif p2_opcion == "βοΈ":
            print("βοΈ corta a π")
            print(f"{p2} gano")
        elif p2_opcion == "π¦":
            print("π¦ come a ππΏ")
            print(f"{p2} gano")            
            
    elif p1_opcion == "βοΈ":
        if p2_opcion == "π":
            print("βοΈ corta a π")
            print(f"{p1} gano")
        elif p2_opcion == "π¦":
            print("βοΈ decapita a π¦")
            print(f"{p1} gano")
        elif p2_opcion == "π":
            print("π aplasta a βοΈ")
            print(f"{p2} gano")
        elif p2_opcion == "πΏ":
            print("πΏ tritura a βοΈ")
            print(f"{p2} gano")
            
    elif p1_opcion == "π¦":
        if p2_opcion == "π":
            print("π¦ envena a π")
            print(f"{p1} gano")
        elif p2_opcion == "π":
            print("π¦ come a π")
            print(f"{p1} gano")
        elif p2_opcion == "πΏ":
            print("πΏ tritura a π¦")
            print(f"{p2} gano")
        elif p2_opcion == "βοΈ":
            print("βοΈ decapita a π¦")
            print(f"{p2} gano")

    elif p1_opcion == "π":
        if p2_opcion == "βοΈ":
            print("π aplasta a βοΈ")
            print(f"{p1} gano")
        elif p2_opcion == "πΏ":
            print("π vaporiza a πΏ")
            print(f"{p1} gano")
        elif p2_opcion == "π¦":
            print("π¦ envena a π")
            print(f"{p2} gano")
        elif p2_opcion == "π":
            print("π desaprueba a π")
            print(f"{p2} gano")


# ("πΏ", "π", "βοΈ", "π¦", "π")

cachipun("πΏ","π¦")
cachipun("πΏ","tijera")
cachipun("π","π")
cachipun("spock","π¦")

