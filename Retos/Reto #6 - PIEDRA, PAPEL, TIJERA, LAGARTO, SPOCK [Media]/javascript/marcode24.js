// # # Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
// # #### Dificultad: Media | Publicación: 06/02/23 | Corrección: 13/02/23

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

const getWinner = (combinations) => {
  const options = {
    '🗿': ['✂️', '🦎'],
    '📄': ['🗿', '🖖'],
    '✂️': ['📄', '🦎'],
    '🦎': ['📄', '🖖'],
    '🖖': ['🗿', '✂️'],
  };

  const results = combinations.reduce((acc, [player1, player2]) => {
    if (options[player1].includes(player2)) {
      acc.player1++;
    } else if (options[player2].includes(player1)) {
      acc.player2++;
    }
    return acc;
  }, { player1: 0, player2: 0 });

  if (results.player1 > results.player2) {
    return 'PLAYER 1';
  }

  if (results.player2 > results.player1) {
    return 'PLAYER 2';
  }

  return 'TIE';
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
