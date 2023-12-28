import Foundation

private enum HogwartsHouseValue {
    case COURAGE, BRAVERY, DETERMINATION, DARING, HONESTY, LOYALTY, HARD_WORK, FRIENDSHIP, CLEVERNESS, CREATIVITY, KNOWLEDGE, CURIOSITY, CUNNING, AMBITION, WIT
}

private enum HogwartsHouse {
    case GRYFFINDOR, HUFFLEPUFF, RAVENCLAW, SLYTHERIN
    
    var values: [HogwartsHouseValue] {
        switch self {
        case .GRYFFINDOR: return [HogwartsHouseValue.COURAGE, HogwartsHouseValue.BRAVERY, HogwartsHouseValue.DETERMINATION, HogwartsHouseValue.DARING]
        case .HUFFLEPUFF: return [HogwartsHouseValue.HONESTY, HogwartsHouseValue.LOYALTY, HogwartsHouseValue.HARD_WORK, HogwartsHouseValue.FRIENDSHIP]
        case .RAVENCLAW: return [HogwartsHouseValue.CLEVERNESS, HogwartsHouseValue.CREATIVITY, HogwartsHouseValue.KNOWLEDGE, HogwartsHouseValue.CURIOSITY]
        case .SLYTHERIN: return [HogwartsHouseValue.CUNNING, HogwartsHouseValue.AMBITION, HogwartsHouseValue.WIT, HogwartsHouseValue.DETERMINATION]
        }
    }
}

private struct HogwartsAlumnHouse {
    let house: HogwartsHouse
    var affinity: Int = 0
    
    mutating func updateAffinity(values: [HogwartsHouseValue]) {
        values.forEach {
            if(house.values.contains($0)) {
                affinity += 1
            }
        }
    }
}

private var griffindorHouse = HogwartsAlumnHouse(house: HogwartsHouse.GRYFFINDOR)
private var hufflepuffHouse = HogwartsAlumnHouse(house: HogwartsHouse.HUFFLEPUFF)
private var ravenclawHouse = HogwartsAlumnHouse(house: HogwartsHouse.RAVENCLAW)
private var slytherinHouse = HogwartsAlumnHouse(house: HogwartsHouse.SLYTHERIN)
private var alumnValues = [HogwartsHouseValue]()

print("¿Qué actividad mágica te gustaría aprender más?")
print("a) Transformaciones de objetos y personas")
print("b) Creación de pociones mágicas")
print("c) Control y manipulación del clima")
print("d) Protección contra las artes oscuras")
print("Selecciona una respuesta de las anteriores:")
if let answer1 = readLine() {
    switch(answer1) {
    case "a": alumnValues += [HogwartsHouseValue.CREATIVITY, HogwartsHouseValue.AMBITION]
    case "b": alumnValues += [HogwartsHouseValue.KNOWLEDGE, HogwartsHouseValue.CURIOSITY]
    case "c": alumnValues += [HogwartsHouseValue.DETERMINATION, HogwartsHouseValue.AMBITION]
    case "d": alumnValues += [HogwartsHouseValue.BRAVERY, HogwartsHouseValue.CLEVERNESS]
    default: print("wrong answer")
    }

    print("¿Qué tipo de aventuras te gustaría vivir en Hogwarts?")
    print("a) Conocer lugares nuevos e interesante")
    print("b) Tener emocionantes duelos mágicos")
    print("c) Resolver misterios y acertijos")
    print("d) Ayudar a los demás y hacer amigos nuevos")
    print("Selecciona una respuesta de las anteriores:")
    if let answer2 = readLine() {
        switch(answer2) {
        case "a": alumnValues += [HogwartsHouseValue.CURIOSITY, HogwartsHouseValue.COURAGE]
        case "b": alumnValues += [HogwartsHouseValue.COURAGE, HogwartsHouseValue.BRAVERY]
        case "c": alumnValues += [HogwartsHouseValue.CLEVERNESS, HogwartsHouseValue.CREATIVITY]
        case "d": alumnValues += [HogwartsHouseValue.FRIENDSHIP, HogwartsHouseValue.LOYALTY]
        default: print("wrong answer")
        }

        print("¿Qué habilidades te gustaría desarrollar durante tu tiempo en Hogwarts?")
        print("a) Aprender hechizos poderosos")
        print("b) Desarrollar habilidades atléticas y físicas")
        print("c) Mejorar tu capacidad de comunicación y liderazgo")
        print("d) Aprender a trabajar en equipo y a colaborar con otros")
        print("Selecciona una respuesta de las anteriores:")
        if let answer3 = readLine() {
            switch(answer3) {
            case "a": alumnValues += [HogwartsHouseValue.AMBITION, HogwartsHouseValue.HARD_WORK]
            case "b": alumnValues += [HogwartsHouseValue.HARD_WORK, HogwartsHouseValue.DETERMINATION]
            case "c": alumnValues += [HogwartsHouseValue.CLEVERNESS, HogwartsHouseValue.CREATIVITY]
            case "d": alumnValues += [HogwartsHouseValue.LOYALTY, HogwartsHouseValue.KNOWLEDGE]
            default: print("wrong answer")
            }

            print("Qué tipo de magia te resulta más interesante?")
            print("a) Hechizos que te permiten viajar a lugares lejanos")
            print("b) Hechizos que te permiten controlar elementos naturales")
            print("c) Hechizos que te permiten transformar objetos y personas")
            print("d) Hechizos que te permiten sanar heridas y enfermedades")
            print("Selecciona una respuesta de las anteriores:")
            print("Selecciona una respuesta de las anteriores:")
            if let answer4 = readLine() {
                switch(answer4) {
                case "a": alumnValues += [HogwartsHouseValue.CURIOSITY, HogwartsHouseValue.AMBITION]
                case "b": alumnValues += [HogwartsHouseValue.KNOWLEDGE, HogwartsHouseValue.CREATIVITY]
                case "c": alumnValues += [HogwartsHouseValue.CREATIVITY, HogwartsHouseValue.AMBITION]
                case "d": alumnValues += [HogwartsHouseValue.KNOWLEDGE, HogwartsHouseValue.HONESTY]
                default: print("wrong answer")
                }
            }


            print("¿Qué actitud o comportamiento consideras que es más importante para triunfar en Hogwarts?")
            print("a) Ser valiente y arriesgado")
            print("b) Ser trabajador y constante")
            print("c) Ser inteligente y astuto")
            print("d) Ser leal y honesto")
            print("Selecciona una respuesta de las anteriores:")    
            if let answer5 = readLine() {
                switch(answer5) {
                case "a": alumnValues += [HogwartsHouseValue.BRAVERY, HogwartsHouseValue.DETERMINATION]
                case "b": alumnValues += [HogwartsHouseValue.AMBITION, HogwartsHouseValue.HARD_WORK]
                case "c": alumnValues += [HogwartsHouseValue.CUNNING, HogwartsHouseValue.WIT]
                case "d": alumnValues += [HogwartsHouseValue.LOYALTY, HogwartsHouseValue.HONESTY]
                default: print("wrong answer")
                }
    
                griffindorHouse.updateAffinity(values: alumnValues)
                hufflepuffHouse.updateAffinity(values: alumnValues)
                ravenclawHouse.updateAffinity(values: alumnValues)
                slytherinHouse.updateAffinity(values: alumnValues)
                print([griffindorHouse, hufflepuffHouse, ravenclawHouse, slytherinHouse].sorted{ $0.affinity > $1.affinity}.first!.house)
            }
        }
    }
}