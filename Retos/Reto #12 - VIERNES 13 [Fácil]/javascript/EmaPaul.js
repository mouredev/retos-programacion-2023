/*
  Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
  - La función recibirá el mes y el año y retornará verdadero o falso.
*/

function friday_13(month,year){
  const date = new Date(year,month-1,13)
  if(date.getDate() === 13 && date.getDay() === 5) {
    return true;
  } else {
    return false;
  }
}

console.log(friday_13(1,2023)) // true
console.log(friday_13(2,2023)) // false
console.log(friday_13(3,2022)) // false
console.log(friday_13(3,2020)) // true
console.log(friday_13(10,2023)) // true
console.log(friday_13(8,2023)) // false
console.log(friday_13(9,2024)) // true

