func mach(_ jugadas:[String]) -> Void{
    
    let punto: [String] = ["Love", "15", "30", "40", "Deduce", "Ventaja", "Winner" ]
    var puntos1: Int = 0
    var puntos2: Int = 0
    
    for jugada in jugadas {
        switch jugada {
            case "P1":
                puntos1 += 1
            case "P2":
                puntos2 += 1
            default:
                print("Alguna jugada es incorrecta")
                return
        }
        
        
        if puntos1 >= 3 && puntos1 >= 3 && puntos1 == puntos2{
            print("Deuce")
        }else if puntos1 >= 4 && puntos1 >= 4 && puntos1 > puntos2 && puntos1 - puntos2 < 2{
            print("Ventaja P1")
        }else if puntos2 >= 4 && puntos2 >= 4 && puntos2 > puntos1 && puntos2 - puntos1 < 2{
            print("Ventaja P2")
        }else if puntos1 > 3 && puntos1 > puntos2{
            print("Ha ganano el P1")
            return
        }else if puntos2 > 3 && puntos2 > puntos2{
            print("Ha ganano el P2")
            return
        }else if puntos1 <= 3 && puntos2 <= 3 {
            print(punto[puntos1], "-", punto[puntos2])
        }
    }
    return
    
}

mach(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])
