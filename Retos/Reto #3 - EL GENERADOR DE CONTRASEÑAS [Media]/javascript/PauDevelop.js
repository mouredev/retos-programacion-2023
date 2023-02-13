//FUNCIÓN QUE DEVUELVE UN NÚMERO ALEATORIO ENTRE 0 Y 'numMax'
const randomNum = (numMax) => Math.floor(Math.random() * numMax)  

//GENERADOR DE CONTRASEÑAS ALEATORIAS
//Primer valor: Longitud (entre 8 y 16)
//Segundo valor: Tiene mayúscular? (true o false)
//Tercer valor: Tiene números? (true o false)
//Cuarto valor: Tiene símbolos? (true o  false)
//En caso de solo establecer la longitud, genera una contraseña unícamente de letras minúsculas
const passwordGenerator = (num, hasCapitalLetters, hasNumbers, hasSymbols) => {
    let elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    const capitalLetters = elements.map(letter => letter.toUpperCase());
    const numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    const symbols = ['º', 'ª', '!', '|', '@', '·', '#', '$', '€', '%', '&', '/', '(', ')', '=', '?', '¿', '¡', '^', '', '[', '+', '*', ']', '¨', '{', '}', ',', ';', '.', ':', '-', '_', '<', '>']

    hasCapitalLetters ? elements = [...elements, ...capitalLetters] : elements
    hasNumbers ? elements = [...elements, ...numbers] : elements
    hasSymbols ? elements = [...elements, ...symbols] : elements

    let password = new Array(num)
    for (let i = 0; i < password.length; i++) {
        let randomElement = elements[randomNum(elements.length)]
        password[i] = randomElement
    }

    return (num >= 8) && (num <= 16) ? password.join('') : 'Establece una longitud entre 8 y 16 caracteres'
}


console.log(passwordGenerator(3, false, false, true))
console.log(passwordGenerator(10, true, false, false))
console.log(passwordGenerator(5, false, false, false))
console.log(passwordGenerator(15, true, true, true))
console.log(passwordGenerator(8, false, true, false))
console.log(passwordGenerator(12, true, false, true))
console.log(passwordGenerator(8))
console.log(passwordGenerator(16, true, true, false))
console.log(passwordGenerator(25, true, false, true))