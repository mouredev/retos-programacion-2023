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

/* 
* Posibilidades
✂️ > 📄
📄 > 🗿
🗿 > 🦎
🦎 > 🖖
🖖 > ✂️
✂️ > 🦎
🦎 > 📄
📄 > 🖖
🖖 > 🗿
🗿 > ✂️
*/

const ejemploEntrada = [["🗿","✂️"], ["✂️","🗿"], ["📄","✂️"], ['🦎','🖖'], ['🖖','🗿'], ["✂️","📄"], ['✂️', '✂️']]


function playRPSLS (arrayGames) {
  let mostWinner = ''
  let player1Won = 0
  let player2Won = 0

  // Analizar cada juego y sumar quien gana
  
  for (let game of arrayGames) {
    let winner = ''
    // const player1Choice = game[0]
    // const player2Choice = game[1]
    const [player1Choice, player2Choice] = game

    if (player1Choice === player2Choice) {
      console.log('Tie')
      continue
    } else if (
      player1Choice === "✂️" && player2Choice === "📄" ||
      player1Choice === "📄" && player2Choice === "🗿" ||
      player1Choice === "🗿" && player2Choice === "🦎" ||
      player1Choice === "🦎" && player2Choice === "🖖" ||
      player1Choice === "🖖" && player2Choice === "✂️" ||
      player1Choice === "✂️" && player2Choice === "🦎" ||
      player1Choice === "🦎" && player2Choice === "📄" ||
      player1Choice === "📄" && player2Choice === "🖖" ||
      player1Choice === "🖖" && player2Choice === "🗿" ||
      player1Choice === "🗿" && player2Choice === "✂️") {
        winner = 'Player 1'
    } else {
      winner = 'Player 2'
    }
    if (winner === 'Player 1') player1Won++
    if (winner === 'Player 2') player2Won++
    console.log(winner, player1Won, player2Won)
  }

  // Se decide quien gana
  if (player1Won > player2Won) {
    mostWinner = 'Player 1'
  } else if (player1Won < player2Won) {
    mostWinner = 'Player 2'
  } else {
    mostWinner = 'Tie'
  }
  return mostWinner
}

const result = playRPSLS(ejemploEntrada)

console.log(`El Ganador es ${result}`)


