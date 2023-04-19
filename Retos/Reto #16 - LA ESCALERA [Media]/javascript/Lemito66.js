/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 *
 * Ejemplo: 4
 *         _
 *       _|
 *     _|
 *   _|
 * _|
 *
 */

const ladder = (number = 0) => {
  // repeat es un método de String que repite el string tantas veces como se le indique
  let result = "";
  if (number > 0) {
    result += `${" ".repeat(number + 1)}_\n`;
    for (let i = 0; i < number; i++) {
      result += `${" ".repeat(number - i - 1)}_|\n`;
    }
  } else if (number < 0) {
    for (let i = 0; i < Math.abs(number); i++) {
      result += `${" ".repeat(i)}|_\n`;
    }
    result += `${" ".repeat(Math.abs(number))}|`;
  } else {
    result = "__";
  }
  return result;
};

console.log(ladder(-3));
