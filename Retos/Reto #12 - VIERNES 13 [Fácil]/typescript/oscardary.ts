/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

function esViernes13(anho: number, mes: number){
    let fecha = new Date(anho, mes-1, 13)
    return fecha.getDay() === 5
}

console.log("el mes tiene viernes-13?")
console.log(esViernes13(2024, 12))