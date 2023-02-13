"""
 Crea un programa que calcule quien gana más partidas al piedra,
 papel, tijera, lagarto, spock.
 El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 La función recibe un listado que contiene pares, representando cada jugada.
 El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 Debes buscar información sobre cómo se juega con estas 5 posibilidades.
"""

def inicio():

    rules = "✂️ corta a 📄, 📄 cubre a 🗿, 🗿 tritura a 🦎, 🦎 envena a 🖖, 🖖 aplasta a ✂️, ✂️ decapita a 🦎, 🦎 come a 📄, 📄 desaprueba a 🖖, 🖖 vaporiza a 🗿, 🗿 tritura a ✂️"

    input("¿saber las reglas de este juego?")
    print(f"da igual, las reglas son {rules}")

inicio()

def cachipun (p1_opcion, p2_opcion):
    opciones = ("🗿", "📄", "✂️", "🦎", "🖖")
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

    elif p1_opcion == "🗿":
        if p2_opcion == "✂️":
            print("🗿 tritura a ✂️")
            print(f"{p1} gano")
        elif p2_opcion == "🦎":
            print("🗿 tritura a 🦎")
            print(f"{p1} gano")
        elif p2_opcion == "📄":
            print("📄 cubre a 🗿")
            print(f"{p2} gano")
        elif p2_opcion == "🖖":
            print("🖖 vaporiza a 🗿")
            print(f"{p2} gano")

    elif p1_opcion == "📄":
        if p2_opcion == "🗿":
            print("📄 cubre a 🗿")
            print(f"{p1} gano")
        elif p2_opcion == "🖖":
            print("📄 desaprueba a 🖖")
            print(f"{p1} gano")
        elif p2_opcion == "✂️":
            print("✂️ corta a 📄")
            print(f"{p2} gano")
        elif p2_opcion == "🦎":
            print("🦎 come a 📄🗿")
            print(f"{p2} gano")            
            
    elif p1_opcion == "✂️":
        if p2_opcion == "📄":
            print("✂️ corta a 📄")
            print(f"{p1} gano")
        elif p2_opcion == "🦎":
            print("✂️ decapita a 🦎")
            print(f"{p1} gano")
        elif p2_opcion == "🖖":
            print("🖖 aplasta a ✂️")
            print(f"{p2} gano")
        elif p2_opcion == "🗿":
            print("🗿 tritura a ✂️")
            print(f"{p2} gano")
            
    elif p1_opcion == "🦎":
        if p2_opcion == "🖖":
            print("🦎 envena a 🖖")
            print(f"{p1} gano")
        elif p2_opcion == "📄":
            print("🦎 come a 📄")
            print(f"{p1} gano")
        elif p2_opcion == "🗿":
            print("🗿 tritura a 🦎")
            print(f"{p2} gano")
        elif p2_opcion == "✂️":
            print("✂️ decapita a 🦎")
            print(f"{p2} gano")

    elif p1_opcion == "🖖":
        if p2_opcion == "✂️":
            print("🖖 aplasta a ✂️")
            print(f"{p1} gano")
        elif p2_opcion == "🗿":
            print("🖖 vaporiza a 🗿")
            print(f"{p1} gano")
        elif p2_opcion == "🦎":
            print("🦎 envena a 🖖")
            print(f"{p2} gano")
        elif p2_opcion == "📄":
            print("📄 desaprueba a 🖖")
            print(f"{p2} gano")


# ("🗿", "📄", "✂️", "🦎", "🖖")

cachipun("🗿","🦎")
cachipun("🗿","tijera")
cachipun("🖖","🖖")
cachipun("spock","🦎")

