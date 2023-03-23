/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

let defaultArray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v" ,"w" ,"x","y", "z"]
const upperArray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V" ,"W" ,"X","Y", "Z"]
const symbolsArray = ["ª","!","·","$","%","&","/","(",")","=","?","¿","*","^","¨","Ç","_",":",";","„","…","–","}","{","~","[","]","‚","´","≠","”","“","÷","¬","∞","¢","#","@","|","\\","≤","<","\""]
const numbersArray = ["0","1","2","3","4","5","6","7","8","9"]


//Funcion que da un entero entro 0 y un maximo pasado por parametro
const randomInt = (max)=>{
    number = Math.floor(Math.random() * (max - 1) + 0);
    return number;
}

//Funcion que genera la password
const password = (longitud=16, numbers=false, symbols=false, upper=false)=> {
    let password = [];
    if (longitud < 8 || longitud > 16){
        return "Introduce una longitud entre 8 y 16 caracteres"
    }

    if (numbers){
        defaultArray = defaultArray.concat(numbersArray)
        password.push(numbersArray[randomInt(parseInt(numbersArray.length))])
    }

    if(symbols){
        defaultArray = defaultArray.concat(symbolsArray)
        password.push(symbolsArray[randomInt(parseInt(symbolsArray.length))])
    }

    if(upper){
        defaultArray = defaultArray.concat(upperArray)
        password.push(upperArray[randomInt(parseInt(upperArray.length))])
    }

    //passwordType.push[smallArray]

    while (password.length != longitud) {

        password.push(defaultArray[randomInt(parseInt(defaultArray.length))])
    }

    const shuffledPassowrd = password.sort((a, b) => 0.5 - Math.random());
    
    return (shuffledPassowrd.join(""));
}

console.log(password(13,numbers=true, symbols=true, upper=true))