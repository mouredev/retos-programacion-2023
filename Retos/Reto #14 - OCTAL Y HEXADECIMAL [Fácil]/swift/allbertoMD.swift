import Foundation


var hexadecimalQuotient = 0
var hexadecimalRemainder = 0
var divisionHexadecimalNumbers: [String] = []
var hexadecimalNumbersArray: [String] = []
var hexadecimalNumber = "0x"

var stepper = 0

var octalQuotient = 0
var octalRemainder = 0
var divisionOctalNumbers: [String] = []
var octalNumbersArray: [String] = []
var octalNumber = "0o"



print("\nIntroduce el número que quieres convertir en hexadecimal:")
guard let input = readLine(), var decimalToHexadecimalNumber = Int(input) else {
    fatalError()
}

repeat {
    hexadecimalQuotient = decimalToHexadecimalNumber / 16
    hexadecimalRemainder = decimalToHexadecimalNumber % 16
    divisionHexadecimalNumbers.append(String(hexadecimalRemainder))
    decimalToHexadecimalNumber = hexadecimalQuotient
} while hexadecimalQuotient != 0

hexadecimalNumbersArray.append(contentsOf: divisionHexadecimalNumbers)

for number in divisionHexadecimalNumbers {
    if number == "10" {
        hexadecimalNumbersArray.remove(at: stepper)
        hexadecimalNumbersArray.insert("A", at: stepper)
    } else if number == "11" {
        hexadecimalNumbersArray.remove(at: stepper)
        hexadecimalNumbersArray.insert("B", at: stepper)
    }
    else if number == "12" {
        hexadecimalNumbersArray.remove(at: stepper)
        hexadecimalNumbersArray.insert("C", at: stepper)
    }
    else if number ==  "13" {
        hexadecimalNumbersArray.remove(at: stepper)
        hexadecimalNumbersArray.insert("D", at: stepper)
    }
    else if number == "14" {
        hexadecimalNumbersArray.remove(at: stepper)
        hexadecimalNumbersArray.insert("D", at: stepper)
    }
    else if number == "15" {
        hexadecimalNumbersArray.remove(at: stepper)
        hexadecimalNumbersArray.insert("E", at: stepper)
    }
    else if number == "16" {
        hexadecimalNumbersArray.remove(at: stepper)
        hexadecimalNumbersArray.insert("F", at: stepper)
    }
    
    stepper += 1
}

hexadecimalNumbersArray.reverse()

for item in hexadecimalNumbersArray {
    hexadecimalNumber.append(item)
}

print(hexadecimalNumber)



print("\nIntroduce el número que quieres convertir en octal:")
guard let input = readLine(), var decimalToOctalNumber = Int(input) else {
    fatalError()
}

repeat {
    octalQuotient = decimalToOctalNumber / 8
    octalRemainder = decimalToOctalNumber % 8
    octalNumbersArray.append(String(octalRemainder))
    decimalToOctalNumber = octalQuotient
} while octalQuotient != 0

octalNumbersArray.reverse()

for item in octalNumbersArray {
    octalNumber.append(item)
}

print(octalNumber)

