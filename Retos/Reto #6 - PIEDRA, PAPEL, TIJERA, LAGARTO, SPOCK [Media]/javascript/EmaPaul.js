/*
  Crea un programa que calcule quien gana mΓ‘s partidas al piedra,
  papel, tijera, lagarto, spock.
  - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
  - La funciΓ³n recibe un listado que contiene pares, representando cada jugada.
  - El par puede contener combinaciones de "πΏ" (piedra), "π" (papel),
  "βοΈ" (tijera), "π¦" (lagarto) o "π" (spock).
  - Ejemplo. Entrada: [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ")]. Resultado: "Player 2".
  - Debes buscar informaciΓ³n sobre cΓ³mo se juega con estas 5 posibilidades.
*/

// Reglas
// "πΏ": ["βοΈ", "π¦"], // Piedra aplasta a lagarto y a tijera
// "π": ["πΏ", "π"], // Papel tapa a piedra y desautoriza a Spock
// "βοΈ": ["π", "π¦"], // Tijera corta a papel y decapita a lagarto
// "π¦": ["π", "π"], // Lagarto devora a papel y envenena a Spock
// "π": ["πΏ", "βοΈ"], // Spock vaporiza a piedra y rompe tijera

function sheldon_challenge(arr) {

  let player_1 = 0;
  let player_2 = 0;

  arr.map(([player1,player2])=>{
    if(player1==="πΏ" && (player2==="βοΈ" || player2==="π¦")){
      player_1 = player_1 + 1
    }else if(player1==="π" && (player2==="πΏ" || player2==="π")){
      player_1 = player_1 + 1
    }else if(player1==="βοΈ" && (player2==="π" || player2==="π¦")){
      player_1 = player_1 + 1
    }else if(player1==="π¦" && (player2==="π" || player2==="π")){
      player_1 = player_1 + 1
    }else if(player1==="π" && (player2==="πΏ" || player2==="βοΈ")){
      player_1 = player_1 + 1
    }else if(player2==="πΏ" && (player1==="βοΈ" || player1==="π¦")){
      player_2 = player_2 + 1
    }else if(player2==="π" && (player1==="πΏ" || player1==="π")){
      player_2 = player_2 + 1
    }else if(player2==="βοΈ" && (player1==="π" || player1==="π¦")){
      player_2 = player_2 + 1
    }else if(player1==="π¦" && (player2==="π" || player2==="π")){
      player_2 = player_2 + 1
    }else if(player1==="π" && (player2==="πΏ" || player2==="βοΈ")){
      player_2 = player_2 + 1
    }
  })

  if(player_1 > player_2){
    return "Player 1"
  }else if(player_2 > player_1){
    return "Player 2"
  }

}

console.log(sheldon_challenge([["πΏ", "βοΈ"],["βοΈ", "πΏ"],["π", "βοΈ"]])
);
