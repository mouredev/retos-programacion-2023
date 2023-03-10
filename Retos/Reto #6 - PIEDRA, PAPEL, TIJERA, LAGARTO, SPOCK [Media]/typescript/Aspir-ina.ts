/*
 * Crea un programa que calcule quien gana mΓ‘s partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La funciΓ³n recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "πΏ" (piedra), "π" (papel),
 *   "βοΈ" (tijera), "π¦" (lagarto) o "π" (spock).
 * - Ejemplo. Entrada: [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ")]. Resultado: "Player 2".
 * - Debes buscar informaciΓ³n sobre cΓ³mo se juega con estas 5 posibilidades.
 */

type Hand = 'πΏ' | 'π' | 'βοΈ' | 'π¦' | 'π'

const handWinsTo: { [key in Hand]: Hand[] } = {
  'πΏ': ['βοΈ', 'π¦'],
  'π': ['πΏ', 'π'],
  'βοΈ': ['π', 'π¦'],
  'π¦': ['π', 'π'],
  'π': ['πΏ', 'βοΈ'],
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

const hands: [Hand, Hand][] = [['πΏ', 'βοΈ'], ['βοΈ','πΏ'], ['π','βοΈ']]

console.log(piedraPapelTijerasLagartoSpock(hands))