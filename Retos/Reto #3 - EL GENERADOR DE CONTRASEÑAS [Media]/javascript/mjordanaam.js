/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const UPPERCASE = "ABCDEFGHIJKLMNOPKRSTUVWXYZ";
const LOWERCASE = UPPERCASE.toLowerCase();
const NUMBERS = "0123456789";
const SPECIAL = "*@$%_:./^~>#()<";

function generatePasword(length, uppercase, lowercase, numbers, special){
  password = "";
  counter = 0;
  characters = "";

  if(length > 7 && length < 17){

    if (uppercase === true){
      password += UPPERCASE.charAt(Math.floor(Math.random() * UPPERCASE.length+1));
      counter += 1;
      characters += UPPERCASE;
    }
    
    if (lowercase === true){
      password += LOWERCASE.charAt(Math.floor(Math.random() * LOWERCASE.length+1));
      counter += 1;
      characters += LOWERCASE;
    }

    if (numbers === true){
      password += NUMBERS.charAt(Math.floor(Math.random() * NUMBERS.length+1));
      counter += 1;
      characters += NUMBERS;
    }

    if (special === true){
      password += SPECIAL.charAt(Math.floor(Math.random() * SPECIAL.length+1));
      counter += 1;
      characters += SPECIAL;
    }

    if (password !== ""){
      provisional = [];

      for(let j = 0; j < counter; j++){
        provisional[j] = password[j];
      }

      shuffledArray = provisional.sort((a, b) => 0.5 - Math.random());

      password = "";

      for(let k = 0; k < counter; k++){
        password += provisional[k];
      }

      for (let i = 0; i < length - counter; i++) {
        password += characters.charAt(Math.floor(Math.random() * characters.length+1));
      }
    }
  }else{
    password += "Invalid length";
  }

  return password;
}

password = generatePasword(8, true, true, true, true);
console.log(password);

password = generatePasword(15, true, false, false, false);
console.log(password);

password = generatePasword(10, true, true, false, false);
console.log(password);

password = generatePasword(8, true, true, false, true);
console.log(password);

password = generatePasword(16, false, false, true, true);
console.log(password);

password = generatePasword(5, true, true, true, true);
console.log(password);

password = generatePasword(17, true, true, true, true);
console.log(password);
