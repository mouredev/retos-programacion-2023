import Foundation

class DataBase {
    var participants: [String] = []

    func addParticipant(name: String) {
        if !exists(name: name) {
            participants.append(name)
            print("Participante añadido!")
        } else {
            print("El participante ya existe")
        }
    }

    func exists(name: String) -> Bool {
        for participant in participants {
            if participant == name {
                return true
            }
        }

        return false
    }

    func getParticipants() -> [String]{
        return participants
    }

    func deleteParticipant(name: String) {
        if let index = participants.firstIndex(of: name) {
            participants.remove(at: index)
            print("Participante eliminado")
        } else {
            print("El participante no existe")
        }
    }

    func getRandomParticipant() -> String {
        let randomNumber = Int.random(in: 0..<participants.count)
        return participants[randomNumber]
    }
}

class App {
    private var dataBase = DataBase()
    private var exit = false

    func chooseOption() {
        print("\nBienvenido/a al programa de administración del calendario de adviento. 🎄")
        print("Elige una de las siguientes opciones:")
        print("- Añadir participante (1)")
        print("- Borrar participante (2)")
        print("- Mostrar participantes (3)")
        print("- Lanzar sorteo (4)")
        print("- Salir (5)")

        if let option = readLine() {
            switch option {
            case "1":
                addParticipant()
            case "2":
                deleteParticipant()
            case "3":
                getParticipants()
            case "4":
                doRaffle()
            case "5":
                print("Hasta pronto 👋")
                exit = true
            default:
                print("⚠️ Esa opción no existe")
            }
        }
    }

    func addParticipant() {
        print("\nNombre del participante:")

        if let name = readLine() {
            dataBase.addParticipant(name: name)
        }


    }

    func getParticipants() {
        print("\nParticipantes:")
        for participant in dataBase.getParticipants() {
            print("- \(participant)")
        }
    }

    func deleteParticipant() {
        print("\nNombre del participante:")
        if let name = readLine() {
            dataBase.deleteParticipant(name: name)
        }
    }

    func doRaffle() {
        print("\nHaciendo el sorteo:")
        let winer = dataBase.getRandomParticipant()
        print("El ganador/a es \(winer)! 🎉")
    }

    func getExit() -> Bool {
        return exit
    }
}

var app = App()

while !app.getExit() {
    app.chooseOption()
}


