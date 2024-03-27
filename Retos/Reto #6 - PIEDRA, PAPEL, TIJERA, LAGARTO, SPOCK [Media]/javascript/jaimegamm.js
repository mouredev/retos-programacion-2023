// # ## Enunciado
// # ```
// # /*
// #  * Crea un programa que calcule quien gana más partidas al piedra,
// #  * papel, tijera, lagarto, spock.
// #  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
// #  * - La función recibe un listado que contiene pares, representando cada jugada.
// #  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
// #  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
// #  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
// #  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
// #  */
// # ```
// # ## Enunciado
// # ```
// # /*
// #  * Crea un programa que calcule quien gana más partidas al piedra,
// #  * papel, tijera, lagarto, spock.
// #  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
// #  * - La función recibe un listado que contiene pares, representando cada jugada.
// #  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
// #  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
// #  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
// #  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
// #  */
// # ```

function calcularGanador(partidas) {
    // Reglas del juego
    const reglas = {
      "🗿": ["✂️", "🦎"],
      "📄": ["🗿", "🖖"],
      "✂️": ["📄", "🦎"],
      "🦎": ["📄", "🖖"],
      "🖖": ["🗿", "✂️"]
    };
  
    // Contadores de victorias para cada jugador
    let jugador1Victorias = 0;
    let jugador2Victorias = 0;
  
    // Iterar a través de las partidas
    partidas.forEach(partida => {
      const jugadaJugador1 = partida[0];
      const jugadaJugador2 = partida[1];
  
      // Verificar si las jugadas son válidas
      if (reglas.hasOwnProperty(jugadaJugador1) && reglas.hasOwnProperty(jugadaJugador2)) {
        
        // Verificar el ganador de la partida
        if (reglas[jugadaJugador1].indexOf(jugadaJugador2) !== -1) {
          jugador1Victorias++;
        } else if (reglas[jugadaJugador2].indexOf(jugadaJugador1) !== -1) {
          jugador2Victorias++;
        }
      } else {
        console.error("Jugadas no válidas:", jugadaJugador1, jugadaJugador2);
      }
    });
  
    // Determinar el resultado final
    if (jugador1Victorias > jugador2Victorias) {
      return "Player 1";
    } else if (jugador2Victorias > jugador1Victorias) {
      return "Player 2";
    } else {
      return "Tie";
    }
  }
  
  // Ejemplo de uso
  const partidasEjemplo = [["🗿", "🖖"], ["🖖", "🦎"], ["📄", "🦎"]];
  const resultado = calcularGanador(partidasEjemplo);
  console.log(resultado);