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

type Hand = '🗿' | '📄' | '✂️' | '🦎' | '🖖'

const handWinsTo: { [key in Hand]: Hand[] } = {
  '🗿': ['✂️', '🦎'],
  '📄': ['🗿', '🖖'],
  '✂️': ['📄', '🦎'],
  '🦎': ['📄', '🖖'],
  '🖖': ['🗿', '✂️'],
};

const piedraPapelTijerasLagartoSpock = (game: [Hand, Hand][]) => {
  if (!game) return 'No game provided'

  const playerPoints = game.reduce((points: [number, number], [player1, player2]: [Hand, Hand]) => {
    if (handWinsTo[player1].includes(player2)) points[0]++;
    if (handWinsTo[player2].includes(player1)) points[1]++;

    return points
  }, [0, 0])

  if (playerPoints[0] === playerPoints[1]) return 'Tie'
  return `Player 1: ${playerPoints[0]} - Player 2: ${playerPoints[1]}`
}

const hands: [Hand, Hand][] = [['🗿', '✂️'], ['✂️','🗿'], ['📄','✂️']]

console.log(piedraPapelTijerasLagartoSpock(hands))