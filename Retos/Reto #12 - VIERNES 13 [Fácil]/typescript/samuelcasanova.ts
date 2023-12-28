/*
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

const FRIDAY_DAY_OF_WEEK = 5

const isFriday13 = (month: number, year: number): boolean => {
  return new Date(year, month - 1, 13).getDay() === FRIDAY_DAY_OF_WEEK
}

console.log(`isFriday13(1, 2022) returns ${isFriday13(1, 2022)}, expected false`)
console.log(`isFriday13(5, 2022) returns ${isFriday13(5, 2022)}, expected true`)
console.log(`isFriday13(1, 2023) returns ${isFriday13(1, 2023)}, expected true`)
console.log(`isFriday13(2, 2023) returns ${isFriday13(2, 2023)}, expected false`)
console.log(`isFriday13(3, 2023) returns ${isFriday13(3, 2023)}, expected false`)
console.log(`isFriday13(10, 2023) returns ${isFriday13(10, 2023)}, expected true`)