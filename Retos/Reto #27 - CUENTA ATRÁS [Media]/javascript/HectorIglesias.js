function cuenta_atras(numero, intervalo){
    let tiempo = intervalo*1000;
    
    console.log(numero)
    
    if(numero > 0){
        numero = numero - 1 
        if(numero != 0){
            setTimeout(cuenta_atras, tiempo, numero, intervalo)
        }
    }
  
}

cuenta_atras(3,1);