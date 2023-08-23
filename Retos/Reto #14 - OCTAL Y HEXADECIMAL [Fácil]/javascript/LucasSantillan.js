/* Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

function octalHexa(num) {
  // transforma Octal
  let n = num;
  let r = 0;
  let x = 1
  while(n != 0) {
    r = num < 8 && num > -8 ? r += n % 8 : r += n % 8 * x;
    n = Math.trunc(n / 8);
    x *= 10;
  }
  console.log(`El número octal de ${num} es ${r}`);

  // transforma Hexadecimal
  n = num;
  r = '';
  let sH = '0123456789ABCDEF';
  while(n != 0) {
    r = num <= -1 ? sH[(n % 16) * -1] + r : sH[n % 16] + r;
    n = Math.trunc(n / 16);
  }
  r = r === '' ? 0 : r;
  r = num <= -1 ? '-' + r : r;
  console.log(`El número hexadecimal de ${num} es ${r}`);
}

octalHexa(0);
octalHexa(-699);
octalHexa(699);
octalHexa(-7);
octalHexa(730);

