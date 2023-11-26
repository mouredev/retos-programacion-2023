const opcionesJuego = ['🪨', '📄', '✂️', '🦎', '🖖'];

function calcularGanador(jugador1, jugador2){

    const indexPlayer1 = opcionesJuego.indexOf(jugador1)
    const indexPlayer2 = opcionesJuego.indexOf(jugador2)


    const opcionesGanar = [
        [2, 1], // ✂️ corta 📄
        [1, 0], // 📄 cubre 🪨
        [0, 3], // 🪨 aplasta 🦎
        [3, 4], // 🦎 envenena 🖖
        [4, 2], // 🖖 rompe ✂️
        [2, 3], // ✂️ decapita 🦎
        [3, 1], // 🦎 come 📄
        [1, 4], // 📄 desautoriza 🖖
        [4, 0], // 🖖 vaporiza 🪨
        [0, 2], // 🪨 aplasta ✂️
    ]

    if (indexPlayer1 === indexPlayer2){
        return 'Tie'
    }

    if(opcionesGanar.some(par => par[0] === indexPlayer1 && par[1] === indexPlayer2)){
        return 'Jugador 1 gana'
    }else {
        return 'Jugador 2 Gana'
    }
}

function jugarPartidas(jugadas){
    
    for( const jugada of jugadas){

        const resultado = calcularGanador(jugada[0],jugada[1])

        console.log(`Resultado de la partia: ${resultado}`)
    }

}

const jugadas=[
        ['🪨','✂️'], 
        ['✂️','🪨'],
        ['📄','✂️'],
        ['🪨', '✂️'],
        ['🦎', '🖖'],
        ['📄', '🦎'],
        ['✂️', '🪨']
    ]
jugarPartidas(jugadas)
