/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
 */


const findTriples = (limite) =>{
    //base de los triples pitagoricos.
    const a = 3;
    const b = 4;
    const c = 5;
    //condicional por si se coloca un limite menor a "c".
    if (limite<c) {
        console.log("No se pueden crear los triples");
    };
    //se efectua una division del limite entre c para obtener la cantidad de veces que
    //las constantes se sumarán. Luego, el resultado se convierte en entero.
    const getTriples = Math.floor(limite/c);
    //se crea el array que contendra a todos los triples.
    let allTriples = [];
    //se crea un bucle para que se realizen las operaciones la cantidad de veces que
    //indique la operación "getTriples".
    for (let i=1; i<=getTriples; i++) {
        const A = a*i;
        const B = b*i;
        const C = c*i;
        const triples = [A,B,C];
        allTriples =[...allTriples,triples];
    }
    //retornamos el array con los arrays que contienen los triples.
    return allTriples;
}

console.log(findTriples(101));
// PD: es mi primer codigo aquí en la comunidad, si puedo mejorar el código o comenté algo mal
//haganmelo saber.  GRACIAS ;)
