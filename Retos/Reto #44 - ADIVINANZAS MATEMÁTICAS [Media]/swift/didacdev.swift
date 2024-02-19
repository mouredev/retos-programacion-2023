import Foundation

enum Operations {
    case sum
    case sub
    case mul
    case div
}

var rightAnswers = 0
var finish: Bool = false

enum MyError: Error {
    case runtimeError(String)
}

func randomOperation() -> Operations {
    let random = Int.random(in: 0...3)
    switch random {
    case 0:
        return .sum
    case 1:
        return .sub
    case 2:
        return .mul
    default:
        return .div
    }
}

func operation() -> (String, Int) {
    var numberOne = 0
    var numberTwo = 0
    var result = 0

    do {
        numberOne = try getNumber(digits: getDigitsX())
        numberTwo = try getNumber(digits: getDigitsY())
    } catch {
        print(error)
    }

    let sign = randomOperation()

    switch sign {
    case Operations.sum:
        result = numberOne + numberTwo
        return ("\(numberOne) + \(numberTwo)", result)
    case Operations.sub:
        result = numberOne - numberTwo
        return ("\(numberOne) - \(numberTwo)", result)
    case Operations.mul:
        result = numberOne * numberTwo
        return ("\(numberOne) * \(numberTwo)", result)
    case Operations.div:
        result = numberOne / numberTwo
        return ("\(numberOne) / \(numberTwo)", result)
    }

}

func getNumber(digits: Int) throws  -> Int {
    var numberString = ""

    for _ in 1...digits {
        let randomNumber = String(Int.random(in:0...9))
        numberString += randomNumber
    }

    if let number = Int(numberString) {
        return number
    } else {
        throw MyError.runtimeError("No se ha podido convertir el String en Int")
    }
}

func getDigitsX() -> Int {

    return (((rightAnswers - 1) + 5) / 10 + 1)
}

func getDigitsY() -> Int {

    return ((rightAnswers - 1) / 10 + 1)
}

func askQuestion() {
    let question = operation()

    print()
    print(question.0)

    let semaphore = DispatchSemaphore(value: 0)

    var answer: String?

    DispatchQueue.global().async {
        answer = readLine()
        semaphore.signal()
    }

    if semaphore.wait(timeout: .now() + 3) == .timedOut {
        print("Te quedaste sin tiempo 💀")
        finish = true
    } else if let answer = answer {
        if answer == String(question.1) {
            rightAnswers += 1
            print("✅ ¡¡Respuesta correcta!!")
            print("Llevas \(rightAnswers) puntos")
        } else {
            print("❌ Error")
            finish = true
        }
    }
}

while !finish {
    askQuestion()
}
