/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */
function esPrimo(numero){
    if (numero == 0 || numero == 1 || numero == 4) return false;
	for (let x = 2; x < numero / 2; x++) {
		if (numero % x == 0) return false;
	}
    return true;
}

function primosGemelos(rango = 10){
    let primosGemelos="";

    for(let i=1; i<=rango; i++){
        if(esPrimo(i) && esPrimo(i+2)){
            primosGemelos += "("+i+", "+(i+2)+") ";
        }
    }

    console.log(primosGemelos);

}

primosGemelos(10);
primosGemelos(30);