import Foundation

(1 ... 100).forEach {
    var result: String = ""
    
    if $0 % 3 == 0 {
        result.append("fizz")
    }
    
    if $0 % 5 == 0 {
        result.append("buzz")
    }
    
    if result.isEmpty {
        result.append($0.description)
    }
    
    print(result)
}