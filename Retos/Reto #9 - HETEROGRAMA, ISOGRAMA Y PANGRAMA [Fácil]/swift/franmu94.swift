import Foundation

func heterograma(cadena: String) -> Bool {
    Set(cadena).count == cadena.count
}

func isograma(cadena: String) -> Bool {
    var dict = [Character:Int]()
    for i in Set(cadena) {
        dict[i] = cadena.filter{ $0 == i }.count
    }
    return Set(dict.values).count == 1
}

func pangrama(cadena: String) -> Bool {
    Set(cadena.uppercased().filter{ $0.isLetter }).count == 27
}



heterograma(cadena: "qwertyuio")

isograma(cadena: "qwertyuio_qwertyuio_qwertyuio_")

pangrama(cadena:"qwertyuiopasdfghjklñzxcvbnm")

