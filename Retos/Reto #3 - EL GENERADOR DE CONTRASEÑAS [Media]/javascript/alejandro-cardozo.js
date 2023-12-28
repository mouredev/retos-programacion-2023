/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

/**
 *  Retrieves an string representing a new password.
 *  @param {number} len Number between 8 and 16 representing the output length
 *  @param {boolean} upper boolean specifying if the output contains uppercase letters. Default value: false
 *  @param {boolean} numbers boolean specifying if the output contains numbers. Default value: false
 *  @param {boolean} symbols boolean specifying if the output contains symbols. Default value: false
 *  @returns {string} Shuffled String created according to the parameters passed
 */

function generatePassword(
  len,
  upper = false,
  numbers = false,
  symbols = false
) {
  if (len < 8 || len > 16) return;
  let chars = [];
  while (len--) {
    chars.push(String.fromCharCode(Math.floor(Math.random() * 26) + 97));
  }
  if (upper) {
    for (let i in chars) {
      if (i % 2 === 0) chars[i] = chars[i].toUpperCase();
    }
  }
  if (numbers) {
    for (let i in chars) {
      if (i % 3 === 0)
        chars[i] = String.fromCharCode(Math.floor(Math.random() * 10) + 48);
    }
  }
  if (symbols) {
    for (let i in chars) {
      if (i % 5 === 0)
        chars[i] = String.fromCharCode(Math.floor(Math.random() * 15) + 33);
    }
  }
  return shuffle(chars).join('');
}

// Helper Function
const shuffle = (arr) => {
  const shuffledArray = [];
  let len = arr.length;
  while (len--) {
    let randomIndex = Math.round(Math.random() * len);
    let randomNumber = arr.splice(randomIndex, 1);
    shuffledArray.push(...randomNumber);
  }
  return shuffledArray;
};

/** tests
* console.log(generatePassword(8));
* console.log(generatePassword(10, true));
* console.log(generatePassword(12, true, true));
* console.log(generatePassword(14, true, true, true));
* console.log(generatePassword(16, true, false, true));
*/