/*# Reto #3: EL GENERADOR DE CONTRASEÑAS
#### Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23
## Enunciado
*/
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const LENGHT = {
    min: 8,
    max: 16
}

const CHARACTERS_PARAMETERS = {
    capitalLetters: 'abcdefghijklmnñopqrstuvwxyz',
    numbers: '0123456789',
    simbols: '~`!@#$%^&*()_-+={[}]|\:;"<,>.?/',
}

const generatePassword = () => {
    let password = '';
    const passwordLenght = Math.round(Math.random() * (LENGHT.max - LENGHT.min) + LENGHT.min);
    const capitalLettersLenght = CHARACTERS_PARAMETERS.capitalLetters.length;
    const numberLenght = CHARACTERS_PARAMETERS.numbers.length;
    const simbolsLenght = CHARACTERS_PARAMETERS.simbols.length;
    
    for(let x=0; x<passwordLenght; x++){
      let typeCharacter = Math.round(Math.random() * (3 - 1) + 1)
      let spaceCharacter;
      let capitalLetter = false;
      
      switch (typeCharacter) {
        case 1:
          spaceCharacter = Math.round(Math.random() * (capitalLettersLenght - 1) + 1);
          Math.round(Math.random()) == 1 ? capitalLetter = true : capitalLetter = false;
          capitalLetter 
            ? password += CHARACTERS_PARAMETERS.capitalLetters.charAt(spaceCharacter).toUpperCase()
            : password += CHARACTERS_PARAMETERS.capitalLetters.charAt(spaceCharacter);
          break;
        case 2:
           spaceCharacter = Math.round(Math.random() * (numberLenght - 1) + 1);
           password += CHARACTERS_PARAMETERS.numbers.charAt(spaceCharacter);
          break;
        case 3:
          spaceCharacter = Math.round(Math.random() * (simbolsLenght - 1) + 1);
          password += CHARACTERS_PARAMETERS.simbols.charAt(spaceCharacter);
          break;
      }
    }
    
    return  password
}


console.log(generatePassword());