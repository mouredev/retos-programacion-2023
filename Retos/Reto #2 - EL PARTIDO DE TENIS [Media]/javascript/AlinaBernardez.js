const puntos = ['Love', 15, 30, 40];
let P1 = 0;
let P2 = 0;

const partido = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1','P2', 'P1','P2','P1','P1'];


partido.map(punto => {
    let resultado;
    punto === 'P1' ? P1++ : P2++;
    if(P1 < 4 || P2 < 4) {
        resultado = puntos[P1] + ' - ' + puntos[P2]
    }
    else if(P1 >= 4 && P1 !== P2) {
        resultado = 'Ventaja P1';
        if(P1 - P2 === 2) {
            resultado = '¡Ganador: P1!';
            //Resetear secuencia para que no admita más puntuación.
        }
    }
    else if(P2 >= 4 && P1 !== P2) {
        resultado = 'Ventaja P2'
        if(P2 - P1 === 2) {
            resultado = 'Ganador: P2'
            //Resetear secuencia para que no admita más puntuación.
        }
    }
    else if(P1 >= 3 && P2 >= 3 && P1 === P2) {
        resultado = 'Deuce';
    }
    console.log(resultado)
})