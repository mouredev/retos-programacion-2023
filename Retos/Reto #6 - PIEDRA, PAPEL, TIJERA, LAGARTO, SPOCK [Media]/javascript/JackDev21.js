/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */


const playrounds = (rondas) => {

  let opcionesJuego = {
    "🗿": ["🦎", "✂️"],
    "📄": ["🗿", "🖖"],
    "✂️": ["📄", "🦎"],
    "🦎": ["🖖", "📄"],
    "🖖": ["✂️", "🗿"]
  };

  let puntosPlayerOne = 0;
  let puntosPlayerTwo = 0;

  rondas.forEach((rondas) => {
    const [eleccionPlayerOne, eleccionPlayerTwo] = rondas;

    if (opcionesJuego[eleccionPlayerOne] && opcionesJuego[eleccionPlayerTwo]) {
      if (opcionesJuego[eleccionPlayerOne].includes(eleccionPlayerTwo)) {
        puntosPlayerOne++
      } else if (opcionesJuego[eleccionPlayerTwo].includes(eleccionPlayerOne)) {
        puntosPlayerTwo++
      }
    } else {
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

console.log(playrounds([["🗿", "🗿"], ["📄", "📄"], ["🖖", "📄"]]));
console.log(playrounds([["🗿", "✂️"], ["✂️", "🗿"], ["🖖", "✂️"]]));
console.log(playrounds([["🗿", "🦎"], ["✂️", "🗿"], ["📄", "🦎"]]));
console.log(playrounds([["🗿", "✂️"], ["🖖", "🖖"], ["📄", "✂️"]]))
