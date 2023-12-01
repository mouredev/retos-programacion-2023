import Foundation

var participants: [String] = []

showMenu()

print("Introduce una opcion y pulsa Enter")

var validInput = true

while validInput {
    if let input: String = readLine(), let option = Int(input) {
        switch option {
            case 1:
                print("Añadir participante")
                addParticipant()
            case 2:
                print("Eliminar participante")
                deleteParticipant()
            case 3:
                print("Mostrar participantes")
                showParticipants()
            case 4:
                print("Lanzar sorteo")
                toHoldRaffle()
                validInput = false
            case 5:
                print("Salir")
                validInput = false
            default:
                print("Enter a valid option")
        }
    }
}

func showMenu() {
    print("\n")
    print("[1]-Añadir participante")
    print("[2]-Borrar participante")
    print("[3]-Mostrar participantes")
    print("[4]-Lanzar sorteo")
    print("[5]-Salir")
}

func addParticipant() {
    print("Introduce el numbre del participante")

    if let input = readLine() {
        participants.append(input)
    }
    print("Participante añadido")
    
    showMenu()
}

func deleteParticipant() {
    print("Introduce el nombre del participante que quieres eliminar")
    
    if let input = readLine() {
        if let index = participants.firstIndex(of: input) {
            participants.remove(at: index)
        }
    }
    print("Participante eliminado")

    showMenu()
}

func showParticipants() {
    print("Todos los participantes:")
    
    for participant in participants {
        print(participant)
    }
    showMenu()
}

func toHoldRaffle() {
    if let winner = participants.randomElement() {
        print("El ganador de concurso es: \(winner)")
    }
}
