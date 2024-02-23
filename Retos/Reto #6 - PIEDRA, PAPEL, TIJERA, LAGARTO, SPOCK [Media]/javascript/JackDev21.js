

const playrounds = (rondas) => {

  let opcionesJuego = {
    "🗿": ["🦎", "✂️"], // Piedra vence a lagarto y tijera
    "📄": ["🗿", "🖖"], // Papel vence a piedra y Spock
    "✂️": ["📄", "🦎"], // Tijera vence a papel y lagarto
    "🦎": ["🖖", "📄"], // Lagarto vence a Spock y papel
    "🖖": ["✂️", "🗿"]  // Spock vence a tijera y piedra
  };


  let puntosPlayerOne = 0;
  let puntosPlayerTwo = 0;

  // Iteración sobre cada ronda de juego
  rondas.forEach((rondas) => {
    // Desestructuración de la ronda para obtener las elecciones de cada jugador
    const [eleccionPlayerOne, eleccionPlayerTwo] = rondas;

    // Verificación de si las elecciones de ambos jugadores son válidas
    if (opcionesJuego[eleccionPlayerOne] && opcionesJuego[eleccionPlayerTwo]) {
      // Verificación de si la elección del jugador 1 vence a la del jugador 2
      if (opcionesJuego[eleccionPlayerOne].includes(eleccionPlayerTwo)) {
        puntosPlayerOne++; // Incrementar puntos del jugador 1
      }
      // Verificación de si la elección del jugador 2 vence a la del jugador 1
      else if (opcionesJuego[eleccionPlayerTwo].includes(eleccionPlayerOne)) {
        puntosPlayerTwo++; // Incrementar puntos del jugador 2
      }
    }
    // Si las elecciones no son válidas, imprimir un mensaje de error
    else {
      console.error("Error: Opciones inválidas");
    }
  })


  if (puntosPlayerOne > puntosPlayerTwo) {
    return `Player 1 Gana: ${puntosPlayerOne} - ${puntosPlayerTwo}`;
  } else if (puntosPlayerTwo > puntosPlayerOne) {
    return `Player 2 Gana: ${puntosPlayerTwo} - ${puntosPlayerOne}`;
  } else {
    return `Empate: ${puntosPlayerOne} - ${puntosPlayerTwo}`;
  }
}

// Ejemplos de rondas de juego y resultados
console.log(playrounds([["🗿", "🗿"], ["📄", "📄"], ["🖖", "📄"]]));
console.log(playrounds([["🗿", "✂️"], ["✂️", "🗿"], ["🖖", "✂️"]]));
console.log(playrounds([["🗿", "🦎"], ["✂️", "🗿"], ["📄", "🦎"]]));
console.log(playrounds([["🗿", "✂️"], ["🖖", "🖖"], ["📄", "✂️"]]));
