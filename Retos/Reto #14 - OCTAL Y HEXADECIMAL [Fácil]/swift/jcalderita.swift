import Foundation

func octal(num: Int) -> Int {
    func convert(num: Int, rest: [Int] = []) -> [Int] {
        guard num != 0 else { return rest }
        
        return convert(num: num / 8, rest: [num % 8] + rest)
    }
    
    let rest = convert(num: num)
    return rest.reduce(0) {
        $0 * 10 + $1
    }
}

func hexadecimal(num: Int) -> String {
    let hexValues = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    func convert(num: Int, hex:[String] = []) -> [String] {
        guard num > 15 else { return [hexValues[num]] + hex }
        
        return convert(num: num / 16, hex: [hexValues[num % 16]] + hex)
    }
    
    let hex = convert(num: num)
    return hex.reduce("") {
        "\($0)\($1)"
    }
}


print(octal(num: 456))
print(hexadecimal(num: 456))
