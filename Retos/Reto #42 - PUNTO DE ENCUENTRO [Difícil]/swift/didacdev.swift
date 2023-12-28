import Foundation

class Object {
    
    let position: (Double, Double)
    let speed: (Double, Double)
    
    init(position: (Double, Double), speed: (Double, Double)) {
        
        self.position = position
        self.speed = speed
    }
}

enum MyCustomError: Error {
    case DivisionByZero
}

func substract(vectorA: (Double, Double), vectorB: (Double, Double)) -> (Double, Double) {
    
    let i = vectorA.0 - vectorB.0
    let j = vectorA.1 - vectorB.1
    
    return (i, j)
}

func add(vectorA: (Double, Double), vectorB: (Double, Double)) -> (Double, Double) {
    
    let i = vectorA.0 + vectorB.0
    let j = vectorA.1 + vectorB.1
    
    return (i, j)
}

func multiply(vector: (Double, Double), time: Double) -> (Double, Double) {
    return (vector.0*time, vector.1*time)
}

func vectorMagnitude(vector: (Double, Double)) -> Double {
    return sqrt(pow(vector.0, 2) + pow(vector.1, 2))
}

func getMeeting(objectA: Object, objectB: Object) {
    var time: Double = 0.0
    
    do {
        time = vectorMagnitude(vector: substract(vectorA: objectA.position, vectorB: objectB.position)) / vectorMagnitude(vector: substract(vectorA: objectB.speed, vectorB: objectA.speed))
    } catch {
        print("Los vectores no se pueden encontrar")
        return
    }
    
    
    let positionA = add(vectorA: objectA.position, vectorB: multiply(vector: objectA.speed, time: time))
    let positionB = add(vectorA: objectB.position, vectorB: multiply(vector: objectB.speed, time: time))
    
    if abs(positionA.0 - positionB.0) < 0.0001 && abs(positionA.1 - positionB.1) < 0.0001 {
        
        print("Los objetos se encuentran en el punto \(positionA) pasados \(time) segundos")
            
    }
    
}


let objectA = Object(position: (2, 2), speed: (2, -1))
let objectB = Object(position: (4, 2), speed: (1, -1))
getMeeting(objectA: objectA, objectB: objectB)

