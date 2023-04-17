// Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
// - La función recibirá el mes y el año y retornará verdadero o falso.

const isFriday13th = (month: string, year: string) => {
    const date = new Date(`${month}, 13 ${year}`);
    const currentDay = date.getDay();
    const FRIDAY_DAY = 5;
     return currentDay === FRIDAY_DAY;
};
  
isFriday13th('june', '2023'); // false
isFriday13th('octuber', '2023'); // true