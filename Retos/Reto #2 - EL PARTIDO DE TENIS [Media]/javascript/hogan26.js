class Jugador{
    constructor(){
        this.puntaje = 0
    }
    anotacion(){
        this.puntaje++
    }
    obtener_puntaje(){
        return this.puntaje
    }
}

class PartidoTenis{
    constructor(secuencia){
        this.jugador1 = new Jugador()
        this.jugador2 = new Jugador()
        this.secuencia = secuencia
        this.diferencia = 0
        this.terminado = false
    }

    calcular_diferencia(){
        this.diferencia = Math.abs(this.jugador1.obtener_puntaje() - this.jugador2.obtener_puntaje())            
    }

    imprimir_jugada(){
        let definicion_puntajes = {0 : 'love',1 : '15',2 : '30',3 : '40'}
        let jugador1 = this.jugador1.obtener_puntaje()
        let jugador2 = this.jugador2.obtener_puntaje()

        if (jugador1 >=3 && jugador2 >=3 && this.diferencia == 0) console.log("Deuce")
        else if (jugador1 >3 && jugador1>jugador2 && this.diferencia == 1) console.log("Ventaja Jugador 1")
        else if (jugador2 >3 && jugador2>jugador1 && this.diferencia == 1) console.log("Ventaja Jugador 2")
        else if (jugador1 >3 && jugador1>jugador2 && this.diferencia == 2){
            console.log("Gana Jugador 1")
            this.terminado = true
        }else if (jugador2 >=3 && jugador2>jugador1 && this.diferencia == 2){
            console.log("Gana Jugador 2")
            this.terminado = true
        }else console.log(definicion_puntajes[jugador1]+" - "+definicion_puntajes[jugador2])
    }

    proceso(secuencia){
        for(let jugador of secuencia){
            if (jugador == 'P1') this.jugador1.anotacion()
            else if (jugador == 'P2') this.jugador2.anotacion()
            else alert("Error en la secuencia")
            this.calcular_diferencia()    
            this.imprimir_jugada()
            if (self.terminado) break
        }
    }
}

let secuencia = ['P1','P1','P2','P2','P1','P2','P1','P2','P2','P2']
const partido = new PartidoTenis()
partido.proceso(secuencia)