class BasesNumber {
    private var decimal: Int
    private var octa, hexa: String

    init(decimal: Int) {
        self.decimal = decimal
        self.octa = ""
        self.hexa = ""
    }

    func toString() -> String {
        return "decimal: \(decimal) - octadecimal: \(octa) - hexadecimal: \(hexa)"
    }

    func calculateOctadecimal() {
        var rest = decimal % 8
        var quotient: Int = decimal / 8
        while(quotient > 8) {
            octa = "\(rest)\(octa)"
            rest = quotient % 8
            quotient = quotient / 8
        }
        octa = "\(quotient)\(rest)\(octa)"
    }

    func calculateHexadecimal() {
        var rest = decimal % 16
        var quotient: Int = decimal / 16
        while(quotient > 16) {
            hexa = "\(rest.toHex())\(hexa)"
            rest = quotient % 16
            quotient = quotient / 16
        }
        hexa = "\(quotient.toHex())\(rest.toHex())\(hexa)"
    }
}

extension Int {
    func toHex() -> String {
        switch(self) {
        case 10: return "A"
        case 11: return "B"
        case 12: return "C"
        case 13: return "D"
        case 14: return "E"
        case 15: return "F"
        default: return "\(self)"
        }
    }
}

func calculateBases(_ number: Int) -> BasesNumber {
    let result = BasesNumber.init(decimal: number)
    result.calculateOctadecimal()
    result.calculateHexadecimal()
    return result
}

print(calculateBases(768).toString())
print(calculateBases(460).toString())