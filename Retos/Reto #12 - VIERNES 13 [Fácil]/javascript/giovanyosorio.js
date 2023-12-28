/* Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
La función recibirá el mes y el año y retornará verdadero o falso. */


function viernes13(year, month) {
    var date = new Date(year, month - 1, 13);

    if (date.getDay() == 5) {
        console.log("El mes " + month + " del año " + year + " si tiene viernes 13");
    } else {
        console.log("El mes " + month + " del año " + year + " no tiene viernes 13");
    }

}

viernes13(2020, 3)

viernes13(2020, 1)