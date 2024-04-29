import Foundation


// Declaración de arrays: minusculas, mayusculas, numeros y simbolos.
let lowercaseCharactersArray = Array("abcdefghijklmnopqrstuvwxyz") // Minusculas.
let uppercaseCharactersArray = Array("ABCDEFGHIJKLMNOPQRSTUVWXYZ") // Mayusculas.
let numbersArray = Array("123456789") // Numeros.
let simbolsArray = Array(",./?><¯˘;:¿\\'\"|»ÆÚ[]{}”’=-)(*&ˆ%$#@!±§±⁄€‹›ﬁ‡°·‚—±") // Simbolos.

// Array donde se añadiran los arrays que se seleccionen en la creación de la contraseña.
var passwordArray: [Character] = []


// Pide por consola la longitud de la contraseña.
print("\nCual es la longitud que quieres la contraseña. (min: 8, max: 16):")
guard let length = readLine() else {
    fatalError()
}
// Almacena el valor introducido por consola, si no se introduce nada se asigna el valor 12 por defecto.
var lengthInput = Int(length) ?? 12


// Pide por consola si quieres letras minusculas en la contraseña, si se introduce s es Si y si se introduce n es No.
print("\nQuieres letras minusculas: (s/n)")
guard let lowerCharacters = readLine() else {
    fatalError()
}
// Declaración de variable Booleana para la funcion de crear contraseña.
var lowerCharactersFlag = false
// Evalua si se a introducido s o n.
switch lowerCharacters {
case "s":
    lowerCharactersFlag = true // Si se introduce s se pone a true.
case "n":
    lowerCharactersFlag = false // Si se introduce n se pone en false.
default:
    lowerCharactersFlag = true // si no se introduce nada por defecto se pone true.
}


// Pide por consola si quieres letras mayusculas en la contraseña, si se introduce s es Si y si se introduce n es No.
print("\nQuieres letras mayusculas: (s/n)")
guard let upperCharacters = readLine() else {
    fatalError()
}
// Declaración de variable Booleana para la funcion de crear contraseña.
var upperCharactersFlag = false
// Evalua si se a introducido s o n.
switch upperCharacters {
case "s":
    upperCharactersFlag = true // Si se introduce s se pone a true.
case "n":
    upperCharactersFlag = false // Si se introduce n se pone a false.
default:
    upperCharactersFlag = true // si no se introduce nada por defecto se pone true.
}


// Pide por consola si quieres números en la contraseña, si se introduce s es Si y si se introduce n es No.
print("\nQuieres números: (s/n)")
guard let numbers = readLine() else {
    fatalError()
}
// Declaración de variable Booleana para la funcion de crear contraseña.
var numbersFlag = false
// Evalua si se a introducido s o n.
switch numbers {
case "s":
    numbersFlag = true // Si se introduce s se pone a true.
case "n":
    numbersFlag = false // Si se introduce n se pone a false.
default:
    numbersFlag = true // si no se introduce nada por defecto se pone true.
}


// Pide por consola si quieres simbolos en la contraseña, si se introduce s es Si y si se introduce n es No.
print("\nQuieres simbolos: (s/n)")
guard let simbols = readLine() else {
    fatalError()
}
// Declaración de variable Booleana para la funcion de crear contraseña.
var simbolsFlag = false
// Evalua si se a introducido s o n.
switch simbols {
case "s":
    simbolsFlag = true // Si se introduce s se pone a true.
case "n":
    simbolsFlag = false // Si se introduce n se pone a false.
default:
    simbolsFlag = true // si no se introduce nada por defecto se pone true.
}


// Declaración de la variable password con el valor del retorno de la funcion generatePassword con los parametros de las variables Flag.
let password = generatePassword(length: lengthInput, lowercaseCharacters: lowerCharactersFlag, uppercaseCharacters: upperCharactersFlag, number: numbersFlag, simbols: simbolsFlag)
// Imprime la contaseña.
print("\nLa contraseña es: \(password)")



// Declaración de la función para generar la contraseña.
func generatePassword(length l: Int, lowercaseCharacters cl: Bool, uppercaseCharacters cu: Bool, number n: Bool, simbols s: Bool) -> String {
    
    var length = l 
    var password = ""
    
    // Si el parametro lowerCharacter es true añade las letras minusculas al array de la contraseña.
    if cl {
        passwordArray.append(contentsOf: lowercaseCharactersArray)
    }
    
    // Si el parametro upperCharacters es true añade las letras mayusculas al array de la contraseña.
    if cu {
        passwordArray.append(contentsOf: uppercaseCharactersArray)
    }
    
    // Si el parametro números es true añade los números al array de la contraseña.
    if n {
        passwordArray.append(contentsOf: numbersArray)    }
    
    // Si el parametro simbols es true añade los simbolos al array de la contraseña.
    if s {
        passwordArray.append(contentsOf: simbolsArray)
    }
    
    // Si la longitud es menor a 8 o mayor a 16 la variable length se pone a 12.
    if l < 8 || l > 16 {
        length = 12
    }
    
    // Itera las veces que indique la variable length.
    for _ in 0..<length {
        // Si el array passwordArray contiene elementos elije un elemento random y lo asigna a la variable random.
        if let randomElement = passwordArray.randomElement() {
            // Añade el elemento random a la variable password.
            password.append(String(randomElement))
        }
    }
    // Devulve la variable password.
    return password
}

