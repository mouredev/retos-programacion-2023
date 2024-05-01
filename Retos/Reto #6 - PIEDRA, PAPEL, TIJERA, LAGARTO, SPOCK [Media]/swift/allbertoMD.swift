import Foundation


let elements = ["🗿", "📄", "🔪", "🦎", "🖖"]

var playP1 = ""
var playP2 = ""

var numberOfPlays = 0

var winsP1 = 0
var winsP2 = 0

var plays = 0

print("Cuantas jugadas quieres hacer? (min: 1, max: 100)")
guard let nOfPlays = readLine(), let numberOfPlays = Int(nOfPlays) else {
    fatalError()
}

if numberOfPlays < 1 {
    print("\n[!] - Numero de jugadas no valido! EL NÚMERO TIENE QUE SER MAYOR A 1.")
    exit(1)
}
if numberOfPlays > 100 {
        print("\n[!] - Numero de jugadas no valido! EL NÚMERO TIENE QUE SER MENOR A 100.")
        exit(1)
}

while true {
    if plays == numberOfPlays {
        break
    }
    guard let pP1 = elements.randomElement() else {
        fatalError()
    }
    guard let pP2 = elements.randomElement() else {
        fatalError()
    }
    
    plays += 1
    
    print("\(pP1) ---- \(pP2)")
    
    if pP1 == "🗿" && pP2 == "🔪" {
        winsP1 += 1
        print("Piedra aplasta tijeras.")
    }
    if pP1 == "🗿" && pP2 == "🦎" {
        winsP1 += 1
        print("Piedra aplasta lagarto.")
    }
    if pP1 == "📄" && pP2 == "🗿" {
        winsP1 += 1
        print("Papel cubre piedar.")
    }
    if pP1 == "📄" && pP2 == "🖖" {
        winsP1 += 1
        print("Papel desautoriza a Spock.")
    }
    if pP1 == "🔪" && pP2 == "📄" {
        winsP1 += 1
        print("Tijeras corta papel.")
    }
    if pP1 == "🔪" && pP2 == "🦎" {
        winsP1 += 1
        print("Tijeras decapita a lagarto.")
    }
    if pP1 == "🦎" && pP2 == "📄" {
        winsP1 += 1
        print("Lagarto se come paple.")
    }
    if pP1 == "🦎" && pP2 == "🖖" {
        winsP1 += 1
        print("Lagarto envenena a Spock.")
    }
    if pP1 == "🖖" && pP2 == "🔪" {
        winsP1 += 1
        print("Spock destroza tijeras.")
    }
    if pP1 == "🖖" && pP2 == "🗿" {
        winsP1 += 1
        print("Spock vaporiza piedra.")
    }
    
    if pP2 == "🗿" && pP1 == "🔪" {
        winsP2 += 1
        print("Piedra aplasta tijeras.")
    }
    if pP2 == "🗿" && pP1 == "🦎" {
        winsP2 += 1
        print("Piedra aplasta lagarto.")
    }
    if pP2 == "📄" && pP1 == "🗿" {
        winsP2 += 1
        print("Papel cubre piedar.")
    }
    if pP2 == "📄" && pP1 == "🖖" {
        winsP2 += 1
        print("Papel desautoriza a Spock.")
    }
    if pP2 == "🔪" && pP1 == "📄" {
        winsP2 += 1
        print("Tijeras corta papel.")
    }
    if pP2 == "🔪" && pP1 == "🦎" {
        winsP2 += 1
        print("Tijeras decapita a lagarto.")
    }
    if pP2 == "🦎" && pP1 == "📄" {
        winsP2 += 1
        print("Lagarto se come paple.")
    }
    if pP2 == "🦎" && pP1 == "🖖" {
        winsP2 += 1
        print("Lagarto envenena a Spock.")
    }
    if pP2 == "🖖" && pP1 == "🔪" {
        winsP2 += 1
        print("Spock destroza tijeras.")
    }
    if pP2 == "🖖" && pP1 == "🗿" {
        winsP2 += 1
        print("Spock vaporiza piedra.")
    }
    
    if pP1 == "🗿" && pP2 == "🗿" {
        print("Tie.")
    }
    if pP1 == "📄" && pP2 == "📄" {
        print("Tie.")
    }
    if pP1 == "🔪" && pP2 == "🔪" {
        print("Tie.")
    }
    if pP1 == "🦎" && pP2 == "🦎" {
        print("Tie.")
    }
    if pP1 == "🖖" && pP2 == "🖖" {
        print("Tie.")
    }
}

if winsP1 > winsP2 {
    print("\nGana el Player1 \(winsP1) a \(winsP2).")
}
if winsP2 > winsP1 {
        print("\nGana el Player2 \(winsP2) a \(winsP1).")

}
if winsP1 == winsP2 {
    print("\nEmpate a \(winsP1).")
}


