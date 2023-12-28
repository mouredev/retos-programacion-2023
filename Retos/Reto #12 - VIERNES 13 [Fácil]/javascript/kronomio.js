/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

const isFridayThirteen = (month, year) => {
  const date = new Date(year, month - 1, 13);
  return date.getDay() === 5;
};

console.log(isFridayThirteen(10,2023)); // true

//Siguiendo la misma linea, voy a listar los proximos 3 martes 13

const nextFridayThirteen = () => {
  let cont = 0;
  const fechaActual = new Date();
  let año = fechaActual.getFullYear();
console.log("****Proximos Viernes 13****");
  while (cont < 3) {
    for (
      i = 0;
      i < 11;
      i++ //month
    ) {
      if (isFridayThirteen(i, año)) {
        const date = new Date(año, i - 1, 13);
        
        console.log(date.toLocaleDateString());
        cont++;
      }
    }

    año++;
  }
};

nextFridayThirteen();
