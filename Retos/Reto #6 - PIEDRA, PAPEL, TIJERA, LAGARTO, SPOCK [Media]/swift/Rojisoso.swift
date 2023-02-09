import Foundation

var MArray = [[String]]()
MArray = [["🖖","🦎"],["🪨","📄"],["✂️","📄"]]

func rules(Game: Array<String>) ->Int{
    
    if Game[0] == "🖖"{
        if Game[1] == "📄"{
            return 1
        }
        else if Game[1] == "✂️"{
            return 0
        }
        else if Game[1] == "🪨"{
            return 0
        }
        else if Game[1] == "🦎"{
            return 1
        }
        else if Game[1] == "🖖"{
            return 2
        }
    }
    else if Game[0] == "📄"{
        if Game[1] == "🖖"{
            return 0
        }
        else if Game[1] == "✂️"{
            return 1
        }
        else if Game[1] == "🪨"{
            return 0
        }
        else if Game[1] == "🦎"{
            return 1
        }
        else if Game[1] == "📄"{
            return 2
        }
    }
    else if Game[0] == "✂️"{
        if Game[1] == "📄"{
            return 0
        }
        else if Game[1] == "🖖"{
            return 1
        }
        else if Game[1] == "🪨"{
            return 1
        }
        else if Game[1] == "🦎"{
            return 0
        }
        else if Game[1] == "✂️"{
            return 2
        }
    }
    else if Game[0] == "🦎"{
        if Game[1] == "📄"{
            return 1
        }
        else if Game[1] == "🖖"{
            return 0
        }
        else if Game[1] == "🪨"{
            return 1
        }
        else if Game[1] == "✂️"{
            return 1
        }
        else if Game[1] == "🦎"{
            return 2
        }
    }
    else if Game[0] == "🪨"{
        if Game[1] == "📄"{
            return 1
        }
        else if Game[1] == "🖖"{
            return 1
        }
        else if Game[1] == "✂️"{
            return 0
        }
        else if Game[1] == "🦎"{
            return 0
        }
        else if Game[1] == "🪨"{
            return 2
        }
    }
    return 3
}

func RPSLS( entrada: Array<Array<String>> ) {
    
    let counter = entrada.count
    var i = 0
    var player1 = 0, player2 = 0
    while(i<counter){
        
        var countergame = rules(Game: entrada[i])
        
        if countergame == 0{
            player1 += 1
            print("Decisión de jugador 1 ->",entrada[i].first!, "vence a decisión de jugador 2 ->" , entrada[i].last!)
        }
        else if countergame == 1{
            player2 += 1
            print("Decisión de jugador 2 ->",entrada[i].last!, "vence a decisión de jugador 1 ->" , entrada[i].first!)
        }
        else if countergame == 2{
            print("Decisión de jugador 1 ->",entrada[i].last!, "empata con la decisión de jugador 2 ->" , entrada[i].first!)
        }
        else if countergame == 3{
            print("se introdujeron valores incorrectos, esta ronda no contará, verifique las entradas")
        }
        i += 1
    }
    
    if player1>player2 {
        print("Ganó Jugador 1")
    }
    else if player2>player1{
        print("Ganó Jugador 2")
    }
    else if player1 == player2{
        print("Empate entre ambos jugadores")
    }
    
}

MArray = [["🖖","🦎"],["🪨","📄"],["✂️","📄"],["🦎","📄"],["🪨","🪨"]]
RPSLS(entrada: MArray)
