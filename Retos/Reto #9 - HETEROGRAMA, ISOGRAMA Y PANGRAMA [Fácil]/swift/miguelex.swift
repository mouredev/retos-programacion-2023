import Foundation

func removeDiacritics(cadena: String) -> String {
    let diacriticos = [
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "à": "a", "è": "e", "ì": "i", "ò": "o", "ù": "u",
        "ä": "a", "ë": "e", "ï": "i", "ö": "o", "ü": "u",
        "â": "a", "ê": "e", "î": "i", "ô": "o", "û": "u",
        "ã": "a", "ñ": "n", "õ": "o",
        "ç": "c"
    ]
    
    var cadena_sin_diacriticos = ""
    for caracter in cadena {
        if let caracter_no_diacritico = diacriticos[String(caracter)] {
            cadena_sin_diacriticos += caracter_no_diacritico
        } else {
            cadena_sin_diacriticos += String(caracter)
        }
    }
    
    return cadena_sin_diacriticos
}

func isHeterogram(cadena: String) -> Bool {
    return cadena.count == Set(removeDiacritics(cadena: cadena)).count
}

func isIsogram(cadena: String) -> Bool {
    var letras_vistas = Set<Character>()
    for letra in removeDiacritics(cadena: cadena) {
        if letras_vistas.contains(letra) {
            return false
        }
        letras_vistas.insert(letra)
    }
    return true
}

func isPangram(cadena: String) -> Bool {
    let alfabeto = Set("abcdefghijklmnopqrstuvwxyz")
    let cadena = removeDiacritics(cadena: cadena.lowercased())
    var alfabeto_restante = alfabeto
    for letra in cadena {
        if alfabeto_restante.contains(letra) {
            alfabeto_restante.remove(letra)
        }
        if alfabeto_restante.isEmpty {
            return true
        }
    }
    return false
}


  let string1 = "murcielago"
  let string2 = "esdrújula"
  let string3 = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja"

  print(isHeterogram(cadena: string1))  // true
  print(isHeterogram(cadena: string2))  // false
  print(isIsogram(cadena: string1))  // true
  print(isIsogram(cadena: string2))  // false
  print(isPangram(cadena: string3))  // true