fun main() {
    inicio()
}

 fun inicio(){
    var puntosJugadorUno = 0
    var puntosJugadorDos = 0
    var jugadas = listOf("spock","lagarto","piedra","papel","tijera")
    var printGanador = listOf("Empate","jugador Uno","jugador Dos")
    
    for(contador in 0..5){
        var jugadaUno = rand(0,4)
        var jugadaDos =  rand(0,4)
        var ganador = 0 
        
        if(jugadaUno != jugadaDos)
        	 ganador = selectGanador(jugadaUno,jugadaDos)
       
        println("jugador Uno : ${jugadas[jugadaUno]}" )
        println("jugador Dos : ${jugadas[jugadaDos]}")
        println("Ganador : ${printGanador[ganador]}")
        println(" ")
        
        if(jugadaUno != jugadaDos){
            if(ganador == 1)
        		  puntosJugadorUno++
        	  else
        		  puntosJugadorDos++
        }
    }
    
    if(puntosJugadorUno == puntosJugadorDos){
        println("La partidad esta empate")
    }else{
        if(puntosJugadorUno < puntosJugadorDos)
     		  println("jugador Dos gano con ${puntosJugadorDos} puntos")
        else
     		  println("jugador Uno gano con ${puntosJugadorUno} puntos")
    }
}

 fun selectGanador(jugadaUno:Int,jugadaDos:Int):Int{
    //0-spock	1-lagarto
    if(jugadaUno == 0 && jugadaDos == 1)
    	return 1
    if(jugadaUno == 1 && jugadaDos == 0)
    	return 2
   
    //0-spock	2-piedra
    if(jugadaUno == 0 && jugadaDos == 2)
    	return 1
    if(jugadaUno == 2 && jugadaDos == 0)
    	return 2
   
    //2-piedra	1-lagarto
    if(jugadaUno == 1 && jugadaDos == 2)
    	return 1
    if(jugadaUno == 2 && jugadaDos == 1)
    	return 2
   
    //0-spock	3-papel
    if(jugadaUno == 0 && jugadaDos == 3)
    	return 1
    if(jugadaUno == 3 && jugadaDos == 0)
    	return 2
   
    //0-spock	4-tijera
    if(jugadaUno == 0 && jugadaDos == 4)
    	return 1
    if(jugadaUno == 4 && jugadaDos == 0)
    	return 2
   
     //1-lagarto 	2-piedra
    if(jugadaUno == 1 && jugadaDos == 2)
    	return 1
    if(jugadaUno == 2 && jugadaDos == 1)
    	return 2
   
     //1-lagarto 	3-papel
    if(jugadaUno == 1 && jugadaDos == 3)
      return 1
    if(jugadaUno == 3 && jugadaDos == 1)
    	return 2
   
     //1-lagarto 	4-tijera
    if(jugadaUno == 1 && jugadaDos == 4)
    	return 1
    if(jugadaUno == 4 && jugadaDos == 1)
    	return 2
   
    //2-piedra	 	3-papel
    if(jugadaUno == 2 && jugadaDos == 3)
    	return 1
    if(jugadaUno == 3 && jugadaDos == 2)
    	return 2
   
     //2-piedra		4-tijera
    if(jugadaUno == 2 && jugadaDos == 4)
    	return 1
    if(jugadaUno == 4 && jugadaDos == 2)
    	return 2
   
    //3-papel		4-tijera
    if(jugadaUno == 3 && jugadaDos == 4)
    	return 1
    if(jugadaUno == 4 && jugadaDos == 3)
    	return 2
    else
    	return 0
}

 fun rand(start: Int, end: Int): Int {
    require(start <= end) { "Illegal Argument" }
    return (start..end).random()
}
