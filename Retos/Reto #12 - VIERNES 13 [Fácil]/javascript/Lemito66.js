/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

const fridayThirteen = (year, month) => {
  try {
    // Se resta menos 1 al mes porque el mes 0 es enero y el mes 11 es diciembre.
    return new Date(year, month - 1, 13).getDay() === 5; // Se digita 5 porque el día 5 es viernes.
  } catch (error) {
    return false;
  }
};

console.log(fridayThirteen(2023, 10));
