


function passwordGenerate(length, number = false, symbol = false, mayus = false) { 

    



let numbers = '0123456789';
let lowerCase = 'abcdefghijklmnopqrstuvwxyz';
let upperCase = lowerCase.toUpperCase();
let symbols = '.?,;-_¡!¿*%&$/()[]{}|@><';

let finalPassword = lowerCase;

let password = '';

if (mayus) finalPassword += upperCase;
if (symbol) finalPassword += symbols; 
if (number) finalPassword += numbers; 

    
    for (let x = 0; x < length; x++) { 
        
        password += finalPassword[Math.floor(Math.random() * finalPassword.length)]

    
    }
    console.log(password)

};
 

passwordGenerate(8, false, true, true);
passwordGenerate(10, true, true, false);
passwordGenerate(13, true, true, true);
passwordGenerate(16, true, false, true);

