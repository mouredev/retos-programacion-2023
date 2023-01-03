const leet = new Map();
leet.set('A', '4');
leet.set('B', 'I3');
leet.set('C', '[');
leet.set('D', ')');
leet.set('E', '3');
leet.set('F', '|=');
leet.set('G', '&');
leet.set('H', '#');
leet.set('I', '1');
leet.set('J', ',_|');
leet.set('K', '>|');
leet.set('L', '£');
leet.set('M', '/\\/\\');
leet.set('N', '^/');
leet.set('O', '0');
leet.set('P', '|*');
leet.set('Q', '(_,)');
leet.set('R', 'I2');
leet.set('S', '5');
leet.set('T', '7');
leet.set('U', '(_)');
leet.set('V', '\\/');
leet.set('W', '\\/\\/');
leet.set('X', '><');
leet.set('Y', 'j');
leet.set('Z', '2');
leet.set('1', 'L');
leet.set('2', 'R');
leet.set('3', 'E');
leet.set('4', 'A');
leet.set('5', 'S');
leet.set('6', 'b');
leet.set('7', 'T');
leet.set('8', 'B');
leet.set('9', 'g');
leet.set('0', 'o');

function cifrar(text) {
  if (!text || text.length === 0) {
    return text;
  }
  text = text.toUpperCase();

  let stringLeet = '';
  for (let index = 0; index < text.length; index++) {
    const letter = text[index];
    stringLeet += leet.get(letter) || ' ';
  }
  return stringLeet;
}

console.clear();
console.log(cifrar('Eduer')); // 3)(_)3I2
console.log(cifrar('Backend Developer')); // I34[>|3^/) )3\/3£0|*3I2
console.log(cifrar('32s')); // ER
console.log(cifrar('Estoy destinado a ser un gran exito en esta vida.')); // 3570j )3571^/4)0 4 53I2 (_)^/ &I24^/ 3><170 3^/ 3574 \/1)4
