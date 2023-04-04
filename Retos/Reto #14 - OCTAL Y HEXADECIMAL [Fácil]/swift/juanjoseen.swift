//
//  juanjoseen.swift
//  
//
//  Created by Juan Jose Elias Navarro on 03/04/23.
//

import UIKit

func decToOct(_ dec: Int) -> String {
    var octal: String = ""
    var num: Int = dec
    while num > 0 {
        let res: Int = num % 8
        octal = String(format: "%d", res) + octal
        num = Int(num / 8)
    }
    return octal
}

func decToHex(_ dec: Int) -> String {
    var hexa: String = ""
    var bin: String = decToBin(dec)
    bin = completeFour(bin)
    let total: Int = Int(bin.count / 4)
    for i in 0..<total {
        let start = bin.index(bin.startIndex, offsetBy: i * 4)
        let end = bin.index(bin.startIndex, offsetBy: i * 4 + 3)
        let range = start...end
        let subBin: String = String(bin[range])
        hexa += binToHex(subBin)
    }
    return hexa
}

func binToHex(_ bin: String) -> String {
    switch bin {
    case "0001":
        return "1"
    case "0010":
        return "2"
    case "0011":
        return "3"
    case "0100":
        return "4"
    case "0101":
        return "5"
    case "0110":
        return "6"
    case "0111":
        return "7"
    case "1000":
        return "8"
    case "1001":
        return "9"
    case "1010":
        return "a"
    case "1011":
        return "b"
    case "1100":
        return "c"
    case "1101":
        return "d"
    case "1110":
        return "e"
    case "1111":
        return "f"
    default:
        return "0"
    }
}

func completeFour(_ num: String) -> String {
    var bin: String = num
    while bin.count % 4 != 0 {
        bin = "0" + bin
    }
    return bin
}

func decToBin(_ dec: Int) -> String {
    var binary: String = ""
    var num = dec
    while (num > 0) {
        let res: Int = num % 2
        binary = String(format: "%d", res) + binary
        num = Int(num / 2)
    }
    return binary
}

print(decToOct(28))
print(decToHex(37))
print(decToOct(28474))
print(decToHex(7364))
