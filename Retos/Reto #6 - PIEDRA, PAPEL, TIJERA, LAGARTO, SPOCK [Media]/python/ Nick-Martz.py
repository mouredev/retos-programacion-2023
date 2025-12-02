import random as rm

def game_rock_papper_cut():
    while True:
        try:
            def condicional_game(a,b):
                if a ==1 and b == 2:
                    print("Pc: 📄\nTu: 🪨")
                    print("Perdiste")
                elif a ==2 and b ==3:
                    print("Pc: ✂️\n Tu: 📄")
                    print("Perdiste")
                elif a ==3 and b ==1:
                    print("Pc: 🪨\n Tu: ✂️")
                    print("Perdiste")
                elif a ==1 and b == 3:
                    print("Pc: 🪨\nTu: 📄")
                    print("Ganaste")
                elif a ==2 and b ==1:
                    print("Pc: 📄\n Tu: 🪨")
                    print("Ganaste")
                elif a ==3 and b ==2:
                    print("Pc: ✂️\n Tu: 📄")
                    print("Ganaste")
                elif a == b:
                    print("Empate")
            def input_game():
                Player = int(input("1: Piedra\n2: Papel\n3: Tijera\n<<|>> "))
                Pc = rm.randint(1,3)
                condicional_game(Player,Pc)
            input_game()     

        except TypeError as TyErxx:
            print(TyErxx)
            print("😡Solamente Numeros😡")
            input_game()
        except NameError as NamErxx:
            print(NamErxx)
        except ValueError as ValErxx:
            print(ValErxx)
game_rock_papper_cut()
