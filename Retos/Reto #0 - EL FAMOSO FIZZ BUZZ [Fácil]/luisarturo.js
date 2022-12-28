/**
 * Funcion para calcular si el número
 * es multiplo por medio de la division
 */

function multiple( values, multiple) {
    result = values % multiple;

    if( result == 0)
        return true
    else
        return false
}


for (let index = 1; index <= 100; index++) {
    if ( multiple(index,3) && multiple(index, 5)) {
        console.log("fizzbuzz")
    } else if (multiple(index, 3)) {
        console.log("fizz");
    } else if (multiple(index, 5)) {
        console.log("buzz");
    } else {
        console.log(index);
    }

}