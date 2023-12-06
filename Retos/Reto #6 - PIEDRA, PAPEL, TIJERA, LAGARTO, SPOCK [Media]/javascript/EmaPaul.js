/*
  Crea un programa que calcule quien gana más partidas al piedra,
  papel, tijera, lagarto, spock.
  - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
  - La función recibe un listado que contiene pares, representando cada jugada.
  - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
  "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
  - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
  - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
*/

// Reglas
// "🗿": ["✂️", "🦎"], // Piedra aplasta a lagarto y a tijera
// "📄": ["🗿", "🖖"], // Papel tapa a piedra y desautoriza a Spock
// "✂️": ["📄", "🦎"], // Tijera corta a papel y decapita a lagarto
// "🦎": ["📄", "🖖"], // Lagarto devora a papel y envenena a Spock
// "🖖": ["🗿", "✂️"], // Spock vaporiza a piedra y rompe tijera

function sheldon_challenge(arr) {

  let player_1 = 0;
  let player_2 = 0;

  arr.map(([player1,player2])=>{
    if(player1==="🗿" && (player2==="✂️" || player2==="🦎")){
      player_1 = player_1 + 1
    }else if(player1==="📄" && (player2==="🗿" || player2==="🖖")){
      player_1 = player_1 + 1
    }else if(player1==="✂️" && (player2==="📄" || player2==="🦎")){
      player_1 = player_1 + 1
    }else if(player1==="🦎" && (player2==="📄" || player2==="🖖")){
      player_1 = player_1 + 1
    }else if(player1==="🖖" && (player2==="🗿" || player2==="✂️")){
      player_1 = player_1 + 1
    }else if(player2==="🗿" && (player1==="✂️" || player1==="🦎")){
      player_2 = player_2 + 1
    }else if(player2==="📄" && (player1==="🗿" || player1==="🖖")){
      player_2 = player_2 + 1
    }else if(player2==="✂️" && (player1==="📄" || player1==="🦎")){
      player_2 = player_2 + 1
    }else if(player1==="🦎" && (player2==="📄" || player2==="🖖")){
      player_2 = player_2 + 1
    }else if(player1==="🖖" && (player2==="🗿" || player2==="✂️")){
      player_2 = player_2 + 1
    }
  })

  if(player_1 > player_2){
    return "Player 1"
  }else if(player_2 > player_1){
    return "Player 2"
  }

}

console.log(sheldon_challenge([["🗿", "✂️"],["✂️", "🗿"],["📄", "✂️"]])
);
