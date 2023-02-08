/**
 *
 * @param {Object} options
 * @returns String
 */

function generatePassword(origParams = {}) {
  const objParam = Object.assign(
    { length: 10, uppercase: true, numbers: true, symbols: true },
    origParams
  );

  let chars = '',
    password = '',
    alp = 'abcdefghijklmnopqrstuvwxyz';

  chars += objParam.numbers ? '0123456789' : '';

  chars += objParam.uppercase
    ? `${alp.toUpperCase()}${alp}`
    : 'abcdefghijklmnopqrstuvwxyz';

  chars += objParam.symbols ? '/?!@#$%^&*()_-+={}[]:;<>,.' : '';

  for (let i = 0; i < objParam.length; i++) {
    password += chars[Math.floor(Math.random() * chars.length)];
  }

  return password;
}

const options = {
  length: 10,
  uppercase: false,
  numbers: false,
  symbols: true,
};

let res = generatePassword(options);

console.log(res);
