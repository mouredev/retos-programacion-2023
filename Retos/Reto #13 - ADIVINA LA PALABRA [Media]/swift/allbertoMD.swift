
import Foundation


let originalWord = "mouredev" // Palabra que se tiene que adivinar.
var gameWord = "" // String donde se almacenara la palabra del juego con menos caracteres.
let wordCount = originalWord.count // Variable donde se almacenan la contidad de caracteres de la palabra original.
let sixtyPercent = Int(Double(wordCount) * 0.60) // Variable que calcula el 60% de caracteres para sustituir por "_".
var strikes = 0 // Variable donde se almacenan los fallos al intentar adivinar la palabra o caracteres.
var flag = false // Variable que se pondra en true si se adivina un caracter, y en false se sumara un strike (un fallo).

var characters: [Character] = [] // Array para almacenar los caracteres de la palabra original.
var deletedCharactersDictionary: [Int:String] = [:] // Diccionario dende se almacenan los caracteres sustituidos por "_".
var numbers: [Int] = [] // Array donde se almacenan la contidad de caracter de la palabra original para obtener los elementos aleatorios.



// Lanza la función que grnera la palabra del juego.
createGameWord()

// Lanza la función que comienza el juego.
game()




// Función que genera la palabra del juego.
func createGameWord() {
    numbers = Array(0..<wordCount) // Crea el array con los números de la cantidad de caracteres de la palabra original.
    characters = Array(originalWord) // Crea el array con los caracteres de la palabra original.

    // Iteración en el 60% de los caracteres de la palabra original.
    for _ in 0..<sixtyPercent {
        
        // Genera un numero aleatorio del array de numeros para sustituir caracteres en la palabra original.
        guard let randomNumber = numbers.randomElement() else {
            fatalError()
        }
        let char = String(characters[randomNumber]) // Variable donde se almacena el caracter aleatorio.
        deletedCharactersDictionary[randomNumber] = char // Almacena el valor del caracter aleatorio con la vlave del numero aleatorio.
        numbers.removeAll { randomNumber == $0 } // Elimina el número que salio como aleatorio del array para que no se vuelva a usar.
        characters.remove(at: randomNumber) // Elimina del array de caracteres el caracter en el indice de número aleatorio.
        characters.insert("_", at: randomNumber) // Inserta "-" en el indice del número aleatorio.
    }
    
    // Añade los caracteres modificados del array de caracteres a la variable de la palabra del juego.
    for character in characters {
        gameWord.append(character)
    }
}



// Función del juego.
func game() {
    print("Tienes 3 oportunidades para adivinar la palabra.")

    // Loop que se ejecutara hasta que la palabra del juego sea igual a la palabra original.
    while gameWord != originalWord {
        print(gameWord)
        
        print("Que letra quieres introducir:")

        // Recive el caracter o palabra para adivinar por consola.
        guard let input = readLine() else {
            fatalError()
        }
        
        // Si la palabra introducida es igual a la palabra original se gana el juego y sale del loop.
        if input == originalWord {
            print("Ganaste.")
            break
        }
        
        // Itera por el diccionario y comprueba si el valor es igual al caracter introducido.
        for (key, value) in deletedCharactersDictionary {
            
            // Comprueba se el caracter introducido es igual al valor.
            if value == input {
                flag = true // Si el caracter introducido coincide la variable se pone a true
                characters.remove(at: key) // Se elimina el caracter del array que coincida con la clave que es igual al introducido.
                characters.insert(Character(value), at: key) // Inserta el caracter introducido en la posición del indice de la clave.
            }
            
        }

        // Si la flag es false se suma un strike (un fallo) e imprime el numero de strikes.
        if !flag {
            strikes += 1
            print("Tienes \(strikes) strikes.")
        }

        // Si los strikes (fallos) seon igual a 3 se pierde el fuego y sale del loop.
        if strikes == 3 {
            print("Perdiste.")
            break
        }
        
        gameWord.removeAll() // Elimina los caracteres de la variable del juego.

        // Añade los elementos nuevos del arry de caracteres al la variable del juego.
        for character in characters {
            gameWord.append(character)
        }
        
        // Si la variable del juego es igual a la variable original se gana el juego.
        if gameWord == originalWord {
            print("Ganaste.")
        }
        
        flag = false // Vuelve a ponar la glag a false.
    }
}

