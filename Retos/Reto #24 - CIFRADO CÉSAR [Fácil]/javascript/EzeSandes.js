const ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';

/**
 *
 * @param {String} str
 * @param {Number} offset
 */
function caesarEncrypt(str, offset = 3) {
  return str
    .split('')
    .map(letter => {
      const idx = (ALPHA.indexOf(letter) + offset) % ALPHA.length;
      return ALPHA[idx];
    })
    .join('');
}

/**
 *
 * @param {String} str
 * @param {Number} offset
 */
function caesarDecrypt(str, offset = 3) {
  return str
    .split('')
    .map(letter => {
      const idx = ALPHA.indexOf(letter) - offset;
      return ALPHA[idx < 0 ? ALPHA.length - Math.abs(idx) : idx];
    })
    .join('');
}

////////////////////////////////////////////// ENCRYPT

// console.log(caesarEncrypt('abc'));
// console.log(caesarEncrypt('xyz'));
// console.log(caesarEncrypt('XYZ'));
// console.log(caesarEncrypt('XYZ', 4));
// console.log(caesarEncrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 6));

////////////////////////////////////////////// DECRYPT

// console.log(caesarDecrypt('abc', 3)); // XYZ
// console.log(caesarDecrypt('def', 3)); // abc
// console.log(caesarDecrypt('def', 6)); // XYZ
// console.log(caesarDecrypt('GHIJKLMNOPQRSTUVWXYZABCDEF', 6)); // ABCDEFGHIJKLMNOPQRSTUVWXYZ

////////////////////////////////////////////// BOTH METHODS

function caesarsCode(str, offset = 3, encrypt = true) {
  return encrypt ? caesarEncrypt(str, offset) : caesarDecrypt(str, offset);
}

console.log(caesarsCode('abc', 3, true)); // def
console.log(caesarsCode('abc', 3, false)); // XYZ
