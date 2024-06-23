//Si quieres compartir tu propia solución de un ejercicio con la comunidad, crea un fichero de código con tu nombre y extensión, y realiza una PULL REQUEST contra el repositorio.

let numeros = () => {
    for (let count = 0; count <= 100; count++) {
        if (count % 3 == 0 && count % 5 == 0) {
            console.log("fizzbuzz");
        } else if (count % 5 == 0) {
            console.log("buzz")
        } else if (count % 3 == 0) {
            console.log("fizz");
        } else {
            console.log(count);
        }
    }
}
numeros(); 
