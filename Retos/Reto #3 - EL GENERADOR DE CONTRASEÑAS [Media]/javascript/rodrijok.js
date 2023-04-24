/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

function passwordGenerator(mayus, numbers, simbols, password_length = 8){
    let all_lowercase_letters = "abcdefghijklmnopqrstuvwxyz";
    let all_uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let all_numbers = "0123456789";
    let all_simbolos = "!#$%&/()=?¡¿";
    let password = "";
    let characters = "";

    if(mayus){
        characters += all_uppercase_letters + all_lowercase_letters;
    }else{
        characters += all_lowercase_letters;
    }

    if(numbers) characters += all_numbers;
    if(simbols) characters += all_simbolos;

    if(password_length >= 8 && password_length <= 16){
        for(let i = 0; i < password_length; i++){
            password += characters.charAt(Math.floor(Math.random() * characters.length));
        }
    }else{
        console.log("La longitud debe ser entre 8 y 16");
    }

    return password;
}

// console.log(passwordGenerator(true, true, true, 8));
// console.log(passwordGenerator(false, false, false, 16));
// console.log(passwordGenerator(true, false, false, 16));
// console.log(passwordGenerator(true, false, true, 14));
// console.log(passwordGenerator(false, true, true, 99));
// console.log(passwordGenerator(false, true, true, 1));