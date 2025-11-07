/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

const meses = {
  enero: 0,
  febrero: 1,
  marzo: 2,
  abril: 3,
  mayo: 4,
  junio: 5,
  julio: 6,
  agosto: 7,
  septiembre: 8,
  octubre: 9,
  noviembre: 10,
  diciembre: 11
};

function tieneViernes13(mes, anio) {
     const valorDelMes = meses[mes.toLowerCase()];
     if (valorDelMes === undefined) {
         return "Mes inválido";
     }
     const fecha = new Date(anio, valorDelMes, 13);
     return fecha.getDay() === 5;
}

console.log(tieneViernes13("octubre", 2023));
console.log(tieneViernes13("febrero", 2024)); 
console.log(tieneViernes13("diciembre", 2019));