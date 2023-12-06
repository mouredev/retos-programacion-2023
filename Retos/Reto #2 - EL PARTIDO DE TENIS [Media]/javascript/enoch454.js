const partidoTenis = (inputAnotaciones) => {
    const dictInd = {'P1': 0, 'P2':1};
    const puntajes = ['Love', '15', '30', '40'];
    let isDouce = false;
    let isVentaja = false;
    let conteoAnotaciones = [0, 0];//ind 0: P1, ind 1: P2
    let ultimoJugador = '';
    
    for(let i = 0; i < inputAnotaciones.length; i++){
        let jugador = inputAnotaciones[i];
        conteoAnotaciones[dictInd[jugador]]++;
        //console.log(conteoAnotaciones);
        isDouce = (conteoAnotaciones[0] === conteoAnotaciones[1] 
            && conteoAnotaciones[0] >= 3);
        isVentaja = (conteoAnotaciones[0] !== conteoAnotaciones[1] 
            && (conteoAnotaciones[0] > 3 || conteoAnotaciones[1] > 3));
        //let puntaje = puntajes[conteoAnotaciones[dictInd[jugador]]];
        //console.log(jugador, dictInd[jugador]);
        if(isDouce){
            console.log('Deuce');
        } else if(isVentaja){
            let jugadorVentaja = (conteoAnotaciones[0] > conteoAnotaciones[1])
                                ?'P1':'P2';
            if(jugadorVentaja === ultimoJugador){
                console.log('Ha ganado el ' + jugadorVentaja);      
            }else{
                console.log('Ventaja ' + jugadorVentaja);
                ultimoJugador = jugadorVentaja;
            }
        }else {
            console.log(puntajes[conteoAnotaciones[dictInd['P1']]] + " - "
            + puntajes[conteoAnotaciones[dictInd['P2']]]);
        }
    }
}; 

let pruebaInput = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];
let segundaPrueba = [
       'P1',
       'P1',
       'P1',
       'P2',
       'P2',
       'P2',
       'P2',
       'P1',
       'P1',
       'P1',
     ];

partidoTenis(segundaPrueba);

