/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */


// console.log(Math.floor(Math.random()*array.length))
// const symbolsArray = ["~", "@", "_", "/", "+", ":"]

const passwordGenerator = (passwordLength = 8, uppercase = false, numbers = false, symbols = false) => {

    const validPasswordLength = () => {
        return passwordLength >= 8 && passwordLength <= 16;
    }

    if (!validPasswordLength()) {
        console.log("el rango de la constraseña debe estar entre 8 y 16 caracteres")
        return
    }

    const lowercaseArray = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'];
    const uppercaseArray = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    const numbersArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    const symbolsArray = ["~", "@", "_", "/", "+", ":"]
    let passwordArray = lowercaseArray
    
    if (uppercase) passwordArray = passwordArray.concat(uppercaseArray)
    if (numbers) passwordArray = passwordArray.concat(numbersArray)
    if (symbols) passwordArray = passwordArray.concat(symbolsArray)

    let password = ""

    for (let i = 0; i < passwordLength; i++) {
        const nextCaracter = Math.floor(Math.random()*passwordArray.length) 
        password += passwordArray[nextCaracter]        
    }

    console.log(password)
}

passwordGenerator()
passwordGenerator(10)
passwordGenerator(10, true)
passwordGenerator(10, true, true)
passwordGenerator(10, true, true, true)