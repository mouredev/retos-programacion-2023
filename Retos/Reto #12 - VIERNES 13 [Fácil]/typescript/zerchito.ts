/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
{
  function hasFriday13th (month: string, year: string): boolean {
    const date = new Date(`${month}, 13 ${year}`);
    const dateDay = date.getDay();
    const FRIDAY = 5;
     return dateDay === FRIDAY;
  };

  console.log(hasFriday13th('January', '2023'));
  console.log(hasFriday13th('April', '2023'));
}
