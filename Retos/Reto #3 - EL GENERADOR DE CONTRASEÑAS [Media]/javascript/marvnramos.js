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

  const randomKey = getIndex(key.length)
  const randomObjectMember = obj[key[randomKey]];
  return randomObjectMember;

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
    else if(!upperCase && !withNumbers && withSymbols){
        for(let i = 0; i < passwordLength; i++){
            let parameter = '';
            let flag = true;
            
            while(flag){
                parameter = getParameter(parameters);
                
                if(parameter !== parameters.numbers){
                    flag = false;
                }
            };
            
            const index = getIndex(parameter.length);

            password += parameter[index];
        }
        return password;
    }
    else if (upperCase && withNumbers && !withSymbols) {
        for(let i = 0; i < passwordLength; i++){
            const parametersWithNoSymbols = { alphabet : [...parameters.alphabet], numbers: [...parameters.numbers]};

            const parameter = getParameter(parametersWithNoSymbols);
            const index = getIndex(parameter.length);

            password += parameter[index];

        }

        return password;
    }
    
    else if(upperCase && !withNumbers && !withSymbols){
        for(let i = 0; i < passwordLength; i++){
            const parameter = parameters.alphabet;
            const index = getIndex(parameter.length);

            password += parameter[index];
        }
        return password.toUpperCase();
    }
}


const passwordGenerator = (passwordLength, upperCase, withNumbers, withSymbols) =>{
    const password = getPassword(passwordLength, upperCase, withNumbers, withSymbols);

    const validPasswordLength = passwordLength >= 8 && passwordLength <= 16;

    if(!validPasswordLength){
        return 'La longitud de la contraseña debe estar entre 8 y 16';
    }

    return password;    
};


const newPassword1 = passwordGenerator(12, true, true, true); // capital letters, numbers and symbols
const newPassword2 = passwordGenerator(10, false, true, true); // lowercase letters, numbers and symbols
const newPassword3 = passwordGenerator(10, false, false, false); // lowercase letters only
const newPassword4 = passwordGenerator(10,false, false, true); // lowercase letters and symbols
const newPassword5 = passwordGenerator(10, true, true, false); // capital letters and numbers
const newPassword6 = passwordGenerator(10, true, false, false); // capital letters only


//----------------------

console.log(newPassword1); // primera condicion con upper
console.log(newPassword2); // segunda condicion con lower
console.log(newPassword3); // just lower cases
console.log(newPassword4); // no capital letters or numbers
console.log(newPassword5) // no symbols
console.log(newPassword6) // just upper cases