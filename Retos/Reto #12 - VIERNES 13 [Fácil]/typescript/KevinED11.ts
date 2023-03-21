/*
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */


type Viernes13Return = (mes: number, año: number) => boolean


const viernes13: Viernes13Return = (mes: number, año:number): boolean => {
  const fecha: Date = new Date(año, mes - 1, 13);
  console.log(Date)
		return fecha.getDay() === 5;

	}


console.log(viernes13(5, 2022))