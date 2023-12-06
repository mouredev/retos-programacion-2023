import Foundation

func drawTriforceTop(rows: Int) {
    let triangleHeight = 2 * rows - 1
    let middleRow = triangleHeight / 2
    
    for row in 0..<middleRow {
        var rowString = ""
        
        for _ in 0..<(middleRow - row) {
            rowString += " "
        }
        
        for _ in 0..<(2 * row + 1) {
            rowString += "*"
        }
        
        print(rowString)
    }
}

// Ejemplo de uso
let numRows = 5
drawTriforceTop(rows: numRows)


