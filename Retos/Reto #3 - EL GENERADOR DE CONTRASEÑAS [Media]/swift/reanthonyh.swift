import Foundation

class GroupCharacters {

  var min: Int
  var max: Int

  init(min: Int, max: Int) {
    self.min = min
    self.max = max
  }

  func getLength() -> Int {
    let length = max - min
    return length
  }

  func getRandomCharacter() -> String {
    let randomNumber = Int.random(in: 0...getLength()) + self.min
    return String(UnicodeScalar(UInt8(randomNumber)))
  }
}

func generatePassword(
  length: Int, noCaps: Bool = false, noNumbers: Bool = false, noSymbols: Bool = false
) -> String {
  let BOT_LIMIT = 8
  let TOP_LIMIT = 16
  var passwordLength: Int = length

  if length < BOT_LIMIT { passwordLength = BOT_LIMIT }
  if length > TOP_LIMIT { passwordLength = TOP_LIMIT }

  var password = ""

  var availableCharacers = [GroupCharacters]()
  let minus = GroupCharacters(min: 97, max: 122)

  availableCharacers.append(minus)
  if !noCaps {
    let mayus = GroupCharacters(min: 65, max: 90)
    availableCharacers.append(mayus)
  }
  if !noNumbers {
    let numbers = GroupCharacters(min: 48, max: 57)
    availableCharacers.append(numbers)
  }
  if !noSymbols {
    let symbolsA = GroupCharacters(min: 33, max: 47)
    let symbolsB = GroupCharacters(min: 58, max: 96)
    let symbolsC = GroupCharacters(min: 123, max: 125)
    availableCharacers.append(contentsOf: [symbolsA, symbolsB, symbolsC])
  }

  for _ in 0..<passwordLength {
    let selector = Int.random(in: 0..<availableCharacers.count)
    let character = availableCharacers[selector].getRandomCharacter()
    password += character
  }

  return password
}

let simplePassword = generatePassword(length: 3, noCaps: true, noNumbers: true, noSymbols: true)
print("Simple Password : \(simplePassword)")

let noNumbersPassword = generatePassword(length: 12, noNumbers: true)
print("Password without Numbers: \(noNumbersPassword)")

let noSymbolsPassword = generatePassword(length: 14, noSymbols: true)
print("Password without Symbols : \(noSymbolsPassword)")

let complexPassword = generatePassword(length: 90)
print("Complex Password : \(complexPassword)")
