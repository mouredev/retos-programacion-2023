import Foundation

// Este reto solo funciona en línea de comando.
// Se debe llamar usando `swift reto44.swift` para probarlo.
// Es por esta razón que no funciona en Swift Playgrounds.

func generateOperation(level: Int) -> (String, Int) {
    let operations = ["+", "-", "*", "/"]
    let selectedOperation = operations.randomElement()!
    var operand1: Int
    var operand2: Int

    if selectedOperation == "/" {
        repeat {
            operand1 = Int.random(in: 1...maxByLevel(level))
            operand2 = Int.random(in: 1...maxByLevel(level))
        } while operand1 % operand2 != 0
    } else {
        operand1 = Int.random(in: 0...maxByLevel(level))
        operand2 = Int.random(in: 0...maxByLevel(level))
    }

    let question = "\(operand1) \(selectedOperation) \(operand2)"
    let answer = evaluateOperation(operand1, operand2, selectedOperation)
    
    return (question, answer)
}

func maxByLevel(_ level: Int) -> Int {
    switch level {
        case 1: return 9
        case 2: return 99
        case 3: return 999
        default: return 9
    }
}

func evaluateOperation(_ operand1: Int, _ operand2: Int, _ operation: String) -> Int {
    switch operation {
        case "+": return operand1 + operand2
        case "-": return operand1 - operand2
        case "*": return operand1 * operand2
        case "/": return operand2 != 0 ? operand1 / operand2 : 0
        default: return 0
    }
}

func startQuestion(question: String, correctAnswer: Int) -> Bool {
    print(question)
    print("Your answer: ", terminator: "")
    let startTime = Date()

    guard let input = readLine() else {
        print("No answer was provided.")
        return false
    }
    
    guard let userAnswer = Int(input) else {
        print("Please enter a valid number.")
        return false
    }

    let timeElapsed = Date().timeIntervalSince(startTime)
    return timeElapsed <= 3 && userAnswer == correctAnswer
}

var hits = 0
var level = 1

while true {
    let (question, correctAnswer) = generateOperation(level: level)
    let isCorrect = startQuestion(question: question, correctAnswer: correctAnswer)
    
    if !isCorrect {
        print("Game over. You got \(hits) right.")
        break
    } else {
        hits += 1
        if hits % 5 == 0 { level += 1 }
    }
}
