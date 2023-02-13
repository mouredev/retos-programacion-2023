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

function game(players) {
  let p1_points = 0
  let p2_points = 0
  let msj = ""
  const win_moves= {
      "🗿": ["✂️", "🦎"],
      "📄": ["🗿", "🖖"],
      "✂️" : ["📄","🦎"],
      "🦎": ["📄","🖖"],
      "🖖": ["✂️","🗿"]  
    }  
  
  
   players.forEach(function(player){
     if(player.length < 2){
       return "Necesitas al menos una jugada de 2 personas"
      }      
     else{
     for (let  element in win_moves[player[1]]){
          if (win_moves[player[1]][element] === player[0]){
            p2_points++
            
          }            
          
          
          else if(win_moves[player[0]][element] === player[1]){
            p1_points++
            
          }
     }
    
     
     }
   });
   if (p1_points > p2_points){
    return "Jugador 1 es el ganador"
   }
   else if(p1_points == p2_points){
    return "Juegos empatados"
   }
   else{
    return "Jugador 2 es el ganador"
   }
   
   
};
  
  
  
  console.log(game([["🗿","✂️"], ["✂️","🗿"],["📄","✂️"]]));
  console.log(game([["🗿","🖖"],["✂️","🗿"]]));
  console.log(game([["🦎","🖖"], ["✂️","🦎"], ["📄","🗿"]]))
  console.log(game([["✂️","🦎"], ["📄","🗿"]]))
  

  