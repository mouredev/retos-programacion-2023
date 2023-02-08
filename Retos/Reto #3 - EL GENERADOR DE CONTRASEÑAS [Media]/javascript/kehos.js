/*
 * Reto #2 - El generador de contraseñas
 * Propuesta de solución realizada por Kehos
 * https://github.com/Kehos
 * 18/01/2023
 * 
 * Funcionamiento:
 * ejecutar archivo con el comando "node kehos.js"
 * 
 * Se puede añadir los siguientes parámetros:
 * - chars:   Acepta un valor numérico entre 8 y 16. Define los caracteres que tendrá la contraseña, si se entra un número fuera del rango se ajusta al límite más cercano.
 *            EJEMPLO: chars=10 -> contraseña de 10 caracteres | chars=100 -> contraseña de 16 caracteres
 * 
 * - caps:    Acepta un valor booleano. Define si la contraseña puede tener letras mayúsculas.
 *            EJEMPLO: caps=true -> La contraseña podrá tener letras mayúsculas
 * 
 * - num:     Acepta un valor booleano. Define si la contraseña puede tener números.
 *            EJEMPLO: num=true -> La contraseña podrá tener caracteres numéricos
 * 
 * - symbol:  Aceptra un valor booleano. Define si la contraseña puede tener símbolos.
 *            EJEMPLO: symbol=true -> La contraseña podrá tener caracteres símbolos
 * 
 * Si se añade un mismo parámetro varias veces se escogerá siempre el último valor.
 * EJEMPLO: node kehos.js caps=true caps=false -> La contraseña no podrá tener letras mayúsculas
 */

// Generator config
const MIN_CHARACTERS = 8;
const MAX_CHARACTERS = 16;
const DEFAULT_CHARACTERS = MIN_CHARACTERS;
let currentLength = DEFAULT_CHARACTERS;
let hasCaps = false;
let hasNumbers = false;
let hasSymbols = false;

// Character sets
const CHARS = 'abcdefghijklmnñopqrstuvwxyz';
const CAPS_CHARS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ';
const NUMBERS = '0123456789';
const SYMBOLS = '!#$%&=?(¿¡^*{+-_;]:€¬|@~<';
const PARAMS = {
  CHARS: 'chars',
  CAPS: 'caps',
  NUM: 'num',
  SYMBOL: 'symbol'
};
const ACCEPTED_PARAMS = [ PARAMS.CHARS, PARAMS.CAPS, PARAMS.NUM, PARAMS.SYMBOL ];
let charSet = CHARS;

// Check for possible command line parameters
function checkParams() {
  const args = process.argv;
  if (args.length >= 3) {
    for (let i = 2; i < args.length; i++) {
      const param = args[i].split('=');
      if (param.length === 2 && ACCEPTED_PARAMS.includes(param[0].toLowerCase())) {
        processParam(param);
      }
    }
  }
  prepareCharactersSet();
}

// Process param and set config properties
function processParam(param) {
  switch (param[0]) {
    case PARAMS.CHARS:
      // Set password length
      const charsParam = parseInt(param[1]);
      if (!isNaN(charsParam)) {
        if (charsParam >= MIN_CHARACTERS && charsParam <= MAX_CHARACTERS) {
          currentLength = charsParam;
        } else if (charsParam < MIN_CHARACTERS) {
          currentLength = MIN_CHARACTERS;
        } else if (charsParam > MAX_CHARACTERS) {
          currentLength = MAX_CHARACTERS;
        }
      }
      break;
    case PARAMS.CAPS:
      // Activate caps possibility
      hasCaps = (param[1] === 'true');
      break;
    case PARAMS.NUM:
      // Activate numbers possibility
      hasNumbers = (param[1] === 'true');
      break;
    case PARAMS.SYMBOL:
      // Activate symbols possibility
      hasSymbols = (param[1] === 'true');
      break;
  }
}

// Set current characters set with configured properties
function prepareCharactersSet() {
  if (hasCaps) {
    charSet += CAPS_CHARS;
  }
  if (hasNumbers) {
    charSet += NUMBERS;
  }
  if (hasSymbols) {
    charSet += SYMBOLS;
  }

  console.log(
    `\nCurrent password config\n- Password length: ${currentLength}\n- Can have caps: ${hasCaps}\n- Can have numbers: ${hasNumbers}\n- Can have symbols: ${hasSymbols}
    \nResulting set of characters to generate password: ${charSet}\n`
  );
}

// Password generation
function generatePassword() {
  let password = '';
  for (let i = 0; i < currentLength; i++) {
    const index = Math.floor(Math.random() * charSet.length);
    password += charSet.charAt(index);
  }
  return password;
}

// Check for possible params
checkParams();

// Generate random password
console.log(`Generated password: ${generatePassword()}`);
