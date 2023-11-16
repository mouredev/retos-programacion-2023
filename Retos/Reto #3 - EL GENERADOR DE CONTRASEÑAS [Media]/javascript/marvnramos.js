/*
 * RETO #3: GENERADOR DE CONTRASEÑAS
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */



// const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
// const numbers = [0,1,2,3,4,5,6,7,8,9];
// const symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|']

const parameters = {
    alphabet: [
        'a', 'b', 'c', 'd', 'e', 
        'f', 'g', 'h', 'i', 'j', 
        'k', 'l', 'm', 'n', 'o', 
        'p', 'q', 'r', 's', 't', 
        'u', 'v', 'w', 'x', 'y', 
        'z'
    ],
    symbols: [
        '!', '@', '#', '$', '%', 
        '^', '&', '*', '(', ')', 
        '_', '+', '-', '=', '[', 
        ']', '{', '}', ';', ':', 
        ',', '.', '<', '>', '/', 
        '?', '|'
    ],
    numbers: [0,1,2,3,4,5,6,7,8,9]
}

const getIndex = (num) => {
    if(!num){
        return 'Parámetro requerido.';
    }
    
    const randomNumber = Math.floor(Math.random()*num);
    
    return randomNumber;
};

const getParameter = (obj) => {
  if (!obj) {
    return 'Parámetro requerido.';
  }

  const key = Object.keys(obj);
  if(key === 0){
    return 'Objeto vacío.';
  }
//   Math.floor(Math.random() * key.length);
  const randomKey = getIndex(key.length)
  const randomObjectMember = obj[key[randomKey]];

  return randomObjectMember;
  ;

};

const getPassword = (passwordLength, upperCase, withNumbers, withSymbols) =>{
    let password = '';

    const regexWithUpperCase = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};:,.<>\/?|]).*$/;
    const regexWithLowerCase = /^(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};:,.<>\/?|]).*$/;



    if(upperCase && withNumbers && withSymbols){
        for(let i = 0; i < passwordLength; i++){
            const parameter = getParameter(parameters);
            const index = getIndex(parameter.length);
    
            password += parameter[index];
        }
        password = password.toUpperCase();

        return regexWithUpperCase.test(password) ? password : getPassword(upperCase, withNumbers, withSymbols);
    }
    else if(!upperCase && !withNumbers && !withSymbols){
        for(let i = 0; i < passwordLength; i++){
            const parameter = parameters.alphabet;
            const index = getIndex(parameter.length);

            password += parameter[index];
        }
        return password;
    }
    else if(!upperCase && withNumbers && withSymbols){
        for(let i = 0; i < passwordLength; i++){
            const parameter = getParameter(parameters);
            const index = getIndex(parameter.length);
    
            password += parameter[index];
        }

        return regexWithLowerCase.test(password) ? password : getPassword(upperCase, withNumbers, withSymbols);
    }
    // else if(!upperCase && !withNumbers && withSymbols){
    //     for(let i = 0; i < passwordLength; i++){
    //         const parameter = getParameter(parameters) !=  ? parameter  : ;
    //     }
}


const passwordGenerator = (passwordLength, upperCase, withNumbers, withSymbols) =>{
    let password = getPassword(passwordLength, upperCase, withNumbers, withSymbols);

    const validPasswordLength = passwordLength >= 8 && passwordLength <= 16;

    if(!validPasswordLength){
        return 'La longitud de la contraseña debe estar entre 8 y 16';
    }

    return password;
    
    
    
};

const passwordLength = 8;
const upperCase = false;
const withNumbers = true; 
const withSymbols = true;

const newPassword1 = passwordGenerator(12, true, true, true)
const newPassword2 = passwordGenerator(10, false, true, true);
const newPassword3 = passwordGenerator(10, false, false, false);


console.log(newPassword1); // primera condicion con upper
console.log(newPassword2); // segunda condicion con lower
console.log(newPassword3)

// console.log(getParameter(parameters))
