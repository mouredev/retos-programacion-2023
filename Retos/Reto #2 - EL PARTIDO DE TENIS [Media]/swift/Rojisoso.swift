import Foundation


func JuegodeTenis(juego: Array<String>) {
    
    var i = 0
    var P1 = 0, P2 = 0
    
    let Puntuacion = [0:"Love",1:"15",2:"30",3:"40"]
    while  i < juego.count {
        
        if juego[i] == "P1"{
            P1 += 1
        }
        else if juego[i] == "P2"{
            P2 += 1
        }
        else{
            print("Se introdujo un valor incorrecto, vuelve a introducir los valores")
            print("Nadie ha ganado")
            i = juego.count
        }
        
        
        if  P1<4 && P2<4 && i<5  {
            print("\(Puntuacion[P1]!) - \(Puntuacion[P2]!)")
        }
        else if (P1 == P2) && (P1>2) {
            print("Deuce")
        }
        else if (P1 == P2 + 1) && (P2>2) {
            print("Ventaja P1")
        }
        else if (P2 == P1 + 1) && (P1>2) {
            print("Ventaja P2")
        }
        else if (P1 == P2 + 2) && (P2>2) {
            print("Ha ganado el P1")
        }
        else if (P2 == P1 + 2) && (P1>2) {
            print("Ha ganado el P2")
        }
    i += 1
    }
}

var MyArray = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
JuegodeTenis(juego: MyArray)
