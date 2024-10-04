/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const data = {
  CAPS: 'ABCDEFGHIJKLMNÑOPKRSTUVWXYZ',
  LOWERCASE: 'abcdefghijklmnñopkrstuvwxyz',
  DIGITS: '1234567890',
  SYMBOLS: '!#$%&*+-:<=>?@_|~',
};

const howLongThePasswordIs = 10;
const rule = {
  MIN: 8,
  MAX: 16,
};

const mix = [data.CAPS, data.DIGITS, data.LOWERCASE, data.SYMBOLS]
  .toString()
  .replace(',', '')
  .split('')
  .sort(() => Math.random() - 0.5)
  .join('');

const mixing = (strData) => {
  const finalData = strData
    .slice(0, howLongThePasswordIs)
    .split('')
    .sort(() => Math.random() - 0.5)
    .join('')
    .toString();
  return finalData;
};

if (howLongThePasswordIs >= rule.MIN && howLongThePasswordIs <= rule.MAX) {
  console.log('✅✅✅ Generating your new password...');
  console.log(`Password with CAPS: ${mixing(data.CAPS)}`);
  console.log(`Password with lowerCase: ${mixing(data.LOWERCASE)}`);
  console.log(`Password with digits: ${mixing(data.DIGITS)}`);
  console.log(`Password with symbols: ${mixing(data.SYMBOLS)}`);
  console.log(`Mixing Password: ${mixing(mix)}`);
}
