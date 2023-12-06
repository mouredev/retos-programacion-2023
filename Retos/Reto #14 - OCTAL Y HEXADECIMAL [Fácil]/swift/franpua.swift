import Foundation

func convertToOctAndHex(number: Int) -> String {
    var resultHex = ""
    var resultOct = ""
    var numberToConvert = number
    
    while numberToConvert != 0 {
        let remainder = numberToConvert % 8
        resultOct = "\(remainder)" + resultOct
        numberToConvert /= 8
    }
    
    let hexValues = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    numberToConvert = number
    while numberToConvert != 0 {
        let remainder = numberToConvert % 16
        resultHex = hexValues[remainder] + resultHex
        numberToConvert /= 16
    }
    
    return resultHex == "" ? "0" : resultOct == "" ? "0" : "El número \(number) en hexadecimal es igual a: \(resultHex) y en octal es igual a: \(resultOct)"
}
print(convertToOctAndHex(number: 495))