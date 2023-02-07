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
var COMBINATIONS = {
	"🗿": ["🦎", "✂️"],
	"📄": ["🗿", "🖖"],
	"✂️": ["📄", "🦎"],
	"🦎": ["🖖", "📄"],
	"🖖": ["✂️", "🗿"]
}

function getWinner(results){
  let p1 = 0
  let p2 = 0
  
  for(let i = 0; i < results.length; i++){
    if (results[i][0] != results[i][1]){
      if (COMBINATIONS[results[i][0]].includes(results[i][1])){
        p1 += 1
      }
      else{
        p2 += 1
      }
    }
  }
  
  if (p1 > p2){
    return "Player 1"
  }
  else if (p2 > p1) {
    return "Player 2"
  }
  else{
    return "Tie"
  }
}

console.log(getWinner([["🗿", "✂️"], ["✂️", "🗿"], ["📄", "✂️"]]))
console.log(getWinner([["🗿", "🗿"], ["✂️", "✂️"], ["🦎", "🦎"]]))
console.log(getWinner([["✂️", "✂️"], ["🦎", "🖖"], ["🦎", "✂️"]]))
console.log(getWinner([["✂️", "✂️"], ["🦎", "🖖"], ["🗿", "✂️"]]))
