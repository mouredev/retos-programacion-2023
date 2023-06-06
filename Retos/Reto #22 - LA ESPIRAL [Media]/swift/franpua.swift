import Foundation

func spiral(size: Int) {
    
    let superior = size % 2 != 0 ? Int((Double((size + 1) / 2))) : size / 2
    for index in 0..<superior {
        if index == 0 {
            print(String(repeating: "═", count: size - 1) + "╗")
        } else {
            print(String(repeating: "║", count: index - 1) + "╔" + String(repeating: "═", count: (size - (2 * index) - 1)) + "╗" + String(repeating: "║", count: index))
        }
    }
    for index in superior..<size {
        print(String(repeating: "║", count: size - index - 1) + "╚" + String(repeating: "═", count: (2 * index) - size) + "╝" + String(repeating: "║", count: size - index - 1))
    }


}
print(spiral(size: 9))