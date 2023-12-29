import Foundation

let alphabet = Array("abcdefghijklmnñopqrstuvwxyz")
var letterValues: [Character: Int] = [:]

for (index, letter) in alphabet.enumerated() {
    letterValues[letter] = index + 1
}

func getPoints(word: String) -> Int {
    var points = 0

    for letter in word {
        if let number = letterValues[letter] {
            points += number
        }
    }

    return points
}

func play() {
    var finish = false

    while !finish {
        print()
        print("Escribe una palabra:")

        if let word = readLine(){

            let points = getPoints(word: word)
            print()
            print("Puntuación: \(points)")

            if points == 100 {
                print("Has ganado!")
                finish = true
            }
        }
    }
}

play()


