import Foundation

func ganador(juegos: [(String,String)]) -> String {
    var arr = ["🗿", "🦎", "🖖", "✂️", "📄"]
    var diff = 0
    for juego in juegos {
        var a = arr.firstIndex(of: juego.0)!
        if [arr[((a+1) % 5)], arr[((a+3) % 5)]].contains(juego.1) {
            diff += 1
        } else if juego.0 == juego.1 {
            continue
        }else{
            diff -= 1
        }
        
    }
    
    return diff > 0 ? "Player 1" : (diff < 0 ? "Player 2" : "Tie")
}


ganador(juegos: [("🖖", "🖖")])
ganador(juegos: [("🗿","✂️"), ("✂️","🗿"), ("📄","🖖")])
