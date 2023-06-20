import Foundation

func printTriforce(numberOfRow: Int) {
    
    let asterisks = "*"
    let spaces = " "
    
    var singleTriangleRowItem = ""
    var doubleTriangleRowItem = ""
    
    var singleTriangle: [String] = []
    var doubleTriangle: [String] = []
    
    var stepper = 0
    
    if numberOfRow <= 1 {
        print("Numero de filas no valido, debe ser mayor a 1")
        
    } else {
        for item in (numberOfRow...numberOfRow + (numberOfRow - 1)).reversed() {
            for _ in 0...item {
                singleTriangleRowItem.append(spaces)
            }
            singleTriangleRowItem.removeLast()
            singleTriangle.append(singleTriangleRowItem)
            singleTriangleRowItem.removeAll()
        }
        
        for item in 1...numberOfRow {
            if stepper < singleTriangle.count {
                for _ in 0..<item * 2 - 1 {
                    singleTriangle[stepper].append(asterisks)
                }
                stepper += 1
            }
        }
        
        stepper = 0
        
        for item in (0..<numberOfRow).reversed() {
            for _ in 0...item {
                doubleTriangleRowItem.append(spaces)
            }
            doubleTriangleRowItem.removeLast()
            doubleTriangle.append(doubleTriangleRowItem)
            doubleTriangleRowItem.removeAll()
        }
        
        for item in 1...numberOfRow {
            if stepper < doubleTriangle.count {
                for _ in 0..<item * 2 - 1 {
                    doubleTriangle[stepper].append(asterisks)
                }
                stepper += 1
            }
        }
        
        stepper = 0
        
        for item in (1...numberOfRow).reversed() {
            if stepper < doubleTriangle.count {
                for _ in 0..<item * 2 - 1 {
                    doubleTriangle[stepper].append(spaces)
                }
                stepper += 1
            }
        }
        
        stepper = 0
        
        for item in 1...numberOfRow {
            if stepper < doubleTriangle.count {
                for _ in 0..<item * 2 - 1 {
                    doubleTriangle[stepper].append(asterisks)
                }
                stepper += 1
            }
        }

        print("Trifuerza \(numberOfRow)")
        
        for row in singleTriangle {
            print(row)
        }
        
        for row in doubleTriangle {
            print(row)
        }
    }
}

print("Introduce el numero de lineas de la trifuerza:")

var validInput = false

while !validInput {
    if let input = readLine(), let number = Int(input) {
        printTriforce(numberOfRow: number)
        validInput = true
    } else {
        print("debes introducir un numero")
    }
}

