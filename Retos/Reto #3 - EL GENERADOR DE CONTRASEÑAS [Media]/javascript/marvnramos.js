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

  const randomKey = Math.floor(Math.random() * key.length);
  const randomObjectMember = obj[key[randomKey]];

  return randomObjectMember;
  ;

};

const getPasswordWithAllParameters = (passwordLength, upperCase, withNumbers, withSymbols) =>{
    let password = '';
    const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};:,.<>\/?|]).*$/;

    if(upperCase, withNumbers, withSymbols){
        for(let i = 0; i <= passwordLength - 1; i++){
            const parameter = getParameter(parameters);
            const index = getIndex(parameter.length);
    
            password += parameter[index];
        }

        password = password.toUpperCase();

        return regex.test(password) ? password : getPassword(upperCase, withNumbers, withSymbols);
    }
}
const getPasswordWithLowerCase = ()=>{
    // logica
}

const passwordGenerator = (passwordLength, upperCase, withNumbers, withSymbols) =>{
    let password = '';

    const validPasswordLength = passwordLength >= 8 && passwordLength <= 16;

    if(!validPasswordLength){
        return 'La longitud de la contraseña debe estar entre 8 y 16';
    } 

    if(upperCase, withNumbers, withSymbols){
        password = getPasswordWithAllParameters(passwordLength, upperCase, withNumbers, withSymbols);
        return password;
    }
    else if( upperCase === true && (withNumbers, withSymbols) === false){
        // logica
    }
    
    
};


console.log(passwordGenerator(8, true, true, true));
// console.log(getParameter(parameters))
