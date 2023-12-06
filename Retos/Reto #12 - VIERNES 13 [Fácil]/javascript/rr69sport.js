/*
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
const weekdays = {
  0: "Domingo",
  1: "Lunes",
  2: "Martes",
  3: "Miércoles",
  4: "Jueves",
  5: "Viernes",
  6: "Sábado"
}
const isItFridayThe13th = (userDate) => {
  const date = new Date(userDate.year, userDate.month - 1, 13)
  const weekday = date.getDay()
  return weekdays[weekday] === "Viernes"
}

console.log(isItFridayThe13th({year: 2023, month: 4}))