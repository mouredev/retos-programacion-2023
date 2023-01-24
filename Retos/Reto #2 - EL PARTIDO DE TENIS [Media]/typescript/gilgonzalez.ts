function partidoTenis(puntuaciones:string[]){

    const puntos = ['LOVE',15,30,40]
    let j1 = 0;
    let j2 = 0;
    for ( const puntuacion of puntuaciones) {
        if (puntuacion == 'P1'){
            j1++;
        }
        else 
        {
            j2++
        }
        //COMPROBAR QUE AÚN NO TIENEN PUNTOS SUFICIENTES PARA GANAR 
        if(j1 <4 && j2 < 4){
            console.log(puntos[j1]+'-'+puntos[j2])
        }
        //COMPROBAR SI VAN EMPATE
        else if(j1===j2){
            console.log('DEUCE')
        }
        //COMPROBAR SI P1 TIENE VENTAJA
        else if(j1-j2===1){
            console.log('Ventaja P1')
        }
        //COMPROBAR SI P2 TIENE VENTAJA
        else if(j2-j1===1){
            console.log('Ventaja P2')
        }
        //COMPROBAR VICTORIA DE P1
        else if (j1>j2) {
            console.log('Victoria P1')
            break;
        }
        else {
            console.log('Victoria P2')
            break;
        }
    }  
}