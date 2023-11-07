/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */
//Funcion recursiva
function timer(start, seconds) {

    if (start === 0) return

    setTimeout(() => {//la llamda se realiza despues del tiempo indicado
        console.log(start);
        timer(start - 1, seconds);
    }, seconds * 1000);
    
}
timer(5,1);

//con ciclo for
function timer (start,seconds) {
    
    for(let i=start; i>0; i--){
        setTimeout(()=>{// se ejecuta todo el ciclo for por lo que todos se ejecutaran al mismo tiempo, para resolver esto los timepos deben variar
            console.log(i)
        },(seconds*1000)*(start-i+1))
    }

}
timer(5,1)