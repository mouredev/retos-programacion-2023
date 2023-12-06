import Foundation

//---------------- Variables ---------------------------

let riddles = [
    ("Si me tumbas, soy todo. Si me cortas por la cintura, me quedo en nada. ¿Qué soy?", "ocho"),
    ("¿Cuántos ladrillos se necesitan para completar un edificio hecho de ladrillos?", "uno"),
    ("Estás en un laberinto completamente a oscuras y tienes una vela, una antorcha, un puñado de paja y una sola cerilla. ¿Qué enciendes primero?", "cerilla"),
    ("¿Qué es lo que no está ni dentro ni fuera de la casa, pero que es necesario para cualquier hogar?", "vetanas"),
    ("El hombre que lo vendió no lo quería. El hombre que lo compró no lo necesitaba. El hombre que lo usó no lo conocía.", "ataúd"),
    ("20+20+20=60. ¿Cómo puedes hacer 60 nuevamente usando el mismo número 3 veces?", "55+5"),
    ("¿Qué palabra se pronuncia incorrectamente incluso si está escrita correctamente?", "incorrectamente"),
    ("Llevo mi casa a cuestas y camino sin tener patas. Dejo un hilillo de plata por donde mi cuerpo pasa.", "caracol"),
    ("Tiene un gran tamaño, memoria famosa, piel dura y la nariz más grande que pueda haber en el mundo.", "elefante"),
    ("Voy construyendo mis redes entre ramas y en rincones para que caigan en ellas las moscas incautas.", "araña"),
    ("Todas las mañanas suena a la misma hora para decirnos que salgamos de la cama.", "despertador"),
    ("Rabo cortito y orejas largas, corro y salto muy ligerito.", "conejo"),
    ("Si dices mi nombre, se rompe.", "silencio"),
    ("No es planeta y tiene luna, no es puerta y tiene marco.", "espejo"),
    ("Soy ave y también llana, pero no tengo alas ni pico.", "avellana"),
    ("Te digo y te repito y te debo avisar que, por más que te diga, no lo vas a adivinar.", "té")
]

let numbers = getRandomNumbers(limit: riddles.count)

var house: [[Room]] = []

// --------------------- Clases --------------------
class Room {
    
    var cardinalPoints = [cardinalPoint]()
    
    enum cardinalPoint {
        case north
        case south
        case west
        case east
    }
    
    init(cardinalPoints: [cardinalPoint]) {
        
        self.cardinalPoints = cardinalPoints
        
    }
    
    func getCardinalPoins() -> [cardinalPoint] {
        
        return cardinalPoints
        
    }
    
}

class UsualRoom: Room {
    let riddle: (question:String, answer:String)
    
    init(cardinalPoints: [cardinalPoint], riddle: (String, String)){
        
        self.riddle = riddle
        super.init(cardinalPoints: cardinalPoints)
        
    }
    
    func getRiddle() -> (String, String) {
        return riddle
    }
    
}

class DoorRoom: Room {
    
    override init(cardinalPoints: [cardinalPoint]) {
        
        super.init(cardinalPoints: cardinalPoints)
        
    }
}

class LollipopRoom: Room {
    
    init() {
        
        super.init(cardinalPoints: [])
        
    }
    
}

class GhostRoom: Room {
    let riddleOne: (question:String, answer:String)
    let riddleTwo: (question:String, answer:String)
    
    init(cardinalPoints: [cardinalPoint], riddleOne: (String, String), riddleTwo: (String, String)) {
        
        self.riddleOne = riddleOne
        self.riddleTwo = riddleTwo
        super.init(cardinalPoints: cardinalPoints)
        
    }
    
    func getRiddleOne() -> (String, String) {
        return riddleOne
    }
    
    func getRiddleTwo() -> (String, String) {
        return riddleTwo
    }
}

//------------------ Funciones ---------------------------------
func getRandomNumbers(limit: Int) -> [Int]{
    var randomNumbers: [Int] = []
    
    for index in 1...limit {
        randomNumbers.append(index)
    }
    
    return randomNumbers.shuffled()
}

func probabilityTrue(prob: Double) -> Bool {
    let randomNumber = Double.random(in: 0...1)
    return randomNumber <= prob
}

func getRandomRiddle() -> (String, String) {
    riddles[Int.random(in: 0...riddles.count - 1)]
}

func setHouse() {
    
    for row in 1...4 {
        
        var rooms: [Room] = [Room(cardinalPoints: []), Room(cardinalPoints: []), Room(cardinalPoints: []), Room(cardinalPoints: [])]
        
        switch row {
            
            // First row
        case 1:
            
            for room in 0..<rooms.count {
                
                if probabilityTrue(prob: 0.3) {
                    
                    switch room {
                        // First col
                    case 0:
                        rooms[room] = GhostRoom(cardinalPoints: [Room.cardinalPoint.east, Room.cardinalPoint.south], riddleOne: getRandomRiddle(), riddleTwo: getRandomRiddle())
                        // Last col
                    case 3:
                        rooms[room] = GhostRoom(cardinalPoints: [Room.cardinalPoint.west, Room.cardinalPoint.south], riddleOne: getRandomRiddle(), riddleTwo: getRandomRiddle())
                    default:
                        rooms[room] = GhostRoom(cardinalPoints: [Room.cardinalPoint.east, Room.cardinalPoint.west, Room.cardinalPoint.south], riddleOne: getRandomRiddle(), riddleTwo: getRandomRiddle())
                    }
                    
                } else {
                    
                    switch room {
                        // First col
                    case 0:
                        rooms[room] = UsualRoom(cardinalPoints: [Room.cardinalPoint.east, Room.cardinalPoint.south], riddle: getRandomRiddle())
                        // Last col
                    case 3:
                        rooms[room] = UsualRoom(cardinalPoints: [Room.cardinalPoint.west, Room.cardinalPoint.south], riddle: getRandomRiddle())
                    default:
                        rooms[room] = UsualRoom(cardinalPoints: [Room.cardinalPoint.east, Room.cardinalPoint.west, Room.cardinalPoint.south], riddle: getRandomRiddle())
                    }
                    
                }
                
            }
            
            let doorRoom: Int = Int.random(in: 0...3)
            
            switch doorRoom {
            case 0:
                rooms[doorRoom] = DoorRoom(cardinalPoints: [Room.cardinalPoint.east, Room.cardinalPoint.south])
            case 3:
                rooms[doorRoom] = DoorRoom(cardinalPoints: [Room.cardinalPoint.west, Room.cardinalPoint.south])
            default:
                rooms[doorRoom] = DoorRoom(cardinalPoints: [Room.cardinalPoint.west, Room.cardinalPoint.south, Room.cardinalPoint.east])
            }
            
            
            // Last row
        case 4:
            
            for room in 0..<rooms.count {
                
                if probabilityTrue(prob: 0.3) {
                    
                    switch room {
                    case 0:
                        rooms[room] = GhostRoom(cardinalPoints: [Room.cardinalPoint.east, Room.cardinalPoint.north], riddleOne: getRandomRiddle(), riddleTwo: getRandomRiddle())
                    case 3:
                        rooms[room] = GhostRoom(cardinalPoints: [Room.cardinalPoint.west, Room.cardinalPoint.north], riddleOne: getRandomRiddle(), riddleTwo: getRandomRiddle())
                    default:
                        rooms[room] = GhostRoom(cardinalPoints: [Room.cardinalPoint.east, Room.cardinalPoint.west, Room.cardinalPoint.north], riddleOne: getRandomRiddle(), riddleTwo: getRandomRiddle())
                    }
                    
                } else {
                    
                    switch room {
                    case 0:
                        rooms[room] = UsualRoom(cardinalPoints: [Room.cardinalPoint.east, Room.cardinalPoint.north], riddle: getRandomRiddle())
                    case 3:
                        rooms[room] = UsualRoom(cardinalPoints: [Room.cardinalPoint.west, Room.cardinalPoint.north], riddle: getRandomRiddle())
                    default:
                        rooms[room] = UsualRoom(cardinalPoints: [Room.cardinalPoint.east, Room.cardinalPoint.west, Room.cardinalPoint.north], riddle: getRandomRiddle())
                    }
                    
                }
                
            }
            
            let lollipopRoom: Int = Int.random(in: 0...3)
            rooms[lollipopRoom] = LollipopRoom()
            
            // Inter row
        default:
            
            for room in 0..<rooms.count {
                
                if probabilityTrue(prob: 0.3) {
                    
                    switch room {
                    case 0:
                        rooms[room] = GhostRoom(cardinalPoints: [Room.cardinalPoint.east, Room.cardinalPoint.north, Room.cardinalPoint.south], riddleOne: getRandomRiddle(), riddleTwo: getRandomRiddle())
                    case 3:
                        rooms[room] = GhostRoom(cardinalPoints: [Room.cardinalPoint.west, Room.cardinalPoint.north, Room.cardinalPoint.south], riddleOne: getRandomRiddle(), riddleTwo: getRandomRiddle())
                    default:
                        rooms[room] = GhostRoom(cardinalPoints: [Room.cardinalPoint.east, Room.cardinalPoint.west, Room.cardinalPoint.north, Room.cardinalPoint.south], riddleOne: getRandomRiddle(), riddleTwo: getRandomRiddle())
                    }
                    
                } else {
                    
                    switch room {
                    case 0:
                        rooms[room] = UsualRoom(cardinalPoints: [Room.cardinalPoint.east, Room.cardinalPoint.north, Room.cardinalPoint.south], riddle: getRandomRiddle())
                    case 3:
                        rooms[room] = UsualRoom(cardinalPoints: [Room.cardinalPoint.west, Room.cardinalPoint.north, Room.cardinalPoint.south], riddle: getRandomRiddle())
                    default:
                        rooms[room] = UsualRoom(cardinalPoints: [Room.cardinalPoint.east, Room.cardinalPoint.west, Room.cardinalPoint.north, Room.cardinalPoint.south], riddle: getRandomRiddle())
                    }
                    
                }
                
            }
            
        }
        
        house.append(rooms)
        
    }
    
    return
    
}

func getStart() -> (Int, Int) {
    var start = (0, 0)
    
    for index in 0...3 {
        
        if house[0][index] is DoorRoom {
            start.1 = index
        }
    }
    
    return start
}

func getEnd() -> (Int, Int) {
    var end = (3, 0)
    
    for index in 0...3 {
        
        if house[3][index] is LollipopRoom {
            end.1 = index
        }
    }
    
    return end
}

func getCardinalPoints(room: (Int, Int)) -> [String] {
    
    let cardinalPoints = house[room.0][room.1].getCardinalPoins()
    var stringCardinalPoints = [String]()
    
    for cardinalPoint in cardinalPoints {
        
        switch cardinalPoint {
        case Room.cardinalPoint.north:
            stringCardinalPoints.append("north")
        case Room.cardinalPoint.south:
            stringCardinalPoints.append("south")
        case Room.cardinalPoint.west:
            stringCardinalPoints.append("west")
        case Room.cardinalPoint.east:
            stringCardinalPoints.append("east")
        }
        
    }
    
    return stringCardinalPoints
    
}

func goNorth(room: (Int, Int)) -> (Int, Int) {
    
    let newRow = room.0 - 1
    let newRoom = (newRow, room.1)
    
    return newRoom
    
}

func goSouth(room: (Int, Int)) -> (Int, Int) {
    
    let newRow = room.0 + 1
    let newRoom = (newRow, room.1)
    
    return newRoom
    
}

func goEast(room: (Int, Int)) -> (Int, Int) {
    
    let newRow = room.1 + 1
    let newRoom = (room.0, newRow)
    
    return newRoom
    
}

func goWest(room: (Int, Int)) -> (Int, Int) {
    
    let newRow = room.1 - 1
    let newRoom = (room.0, newRow)
    
    return newRoom
    
}

func startGame() {
    setHouse()
    var actualRoom: (Int, Int) = getStart()
    let endRoom: (Int, Int) = getEnd()
    
    var quit = false
    
    while (actualRoom.0 != endRoom.0 || actualRoom.1 != endRoom.1) && !quit {
        var newRoom: (Int, Int) = (0, 0)
        
        print("\nPuedes moverte al:")
        
        var cardinalPoints = getCardinalPoints(room: actualRoom)
        
        cardinalPoints.forEach { (cardinalPoint) in
            print("- \(cardinalPoint)")
        }
        
        cardinalPoints += ["salir"]

        print("\nQué camino eliges: ")
        if let choice = readLine() {
            
            if cardinalPoints.contains(choice) {
                switch choice {
                case "north":
                    newRoom = goNorth(room: actualRoom)
                case "south":
                    newRoom = goSouth(room: actualRoom)
                case "east":
                    newRoom = goEast(room: actualRoom)
                case "west":
                    newRoom = goWest(room: actualRoom)
                default:
                    quit = true
                }
                
                if !quit {
                    let room = house[newRoom.0][newRoom.1]
                    
                    if let usualRoom = room as? UsualRoom {
                        print("\nEs una habitación vacía")
                        
                        let riddle = usualRoom.getRiddle()
                        print("Tienes un acertijo:")
                        print("> \(riddle.0)")
                        print("Respuesta:")
                        
                        if let answer = readLine() {
                            if answer == riddle.1 {
                                actualRoom = newRoom
                                print("Respuesta correcta ✅")
                            } else {
                                print("Respuesta incorrecta ❌. Sigues en la misma habitación")
                            }
                        }
                        
                    } else if let ghostRoom = room as? GhostRoom {
                        print("\nEsta habitación tiene un fantasma 👻")
                        
                        let riddleOne = ghostRoom.getRiddleOne()
                        let riddleTwo = ghostRoom.getRiddleTwo()
                        print("Primer acertijo:")
                        print("> \(riddleOne.0)")
                        print("* Respuesta:")
                        
                        if let answer = readLine() {
                            if answer == riddleOne.1 {
                                print("Respuesta correcta ✅")
                                print("Segundo acertijo:")
                                print("> \(riddleTwo.0)")
                                print("* Respuesta:")
                                
                                if let answer = readLine() {
                                    if answer == riddleTwo.1 {
                                        actualRoom = newRoom
                                        print("Respuesta correcta ✅")
                                    }
                                } else {
                                    print("Respuesta incorrecta ❌. Sigues en la misma habitación")
                                }
                            } else {
                                print("Respuesta incorrecta ❌. Sigues en la misma habitación")
                            }
                        }
                    } else if room is DoorRoom {
                        print("\nEstás en el inicio 🚪")
                        actualRoom = newRoom
                    } else {
                        actualRoom = newRoom
                    }
                    
                } else {
                    print("\nEres un cobarde! 💀")
                }
                
            } else {
                print("\n ⚠️ No puedes moverte en esa dirección")
            }
        }
    }
    
    if actualRoom == endRoom {
        print("\n🎉 Enhorabuena, has ganado!!")
    }
    
}


startGame()

