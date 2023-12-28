/*
* Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
* - La función recibirá el mes y el año y retornará verdadero o falso.
*/

const isFriday13 = (month, year) => {
  const date = new Date(year, month - 1, 13);
  return date.getDay() === 5;
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
