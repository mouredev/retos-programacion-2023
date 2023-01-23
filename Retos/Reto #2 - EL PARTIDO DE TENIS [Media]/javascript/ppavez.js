/*# Reto #2: EL PARTIDO DE TENIS
#### Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23
## Enunciado
*/
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */


const SCORES = {
    love: "Love",
    fifteen: "15",
    thirty: "30",
    forty: "40",
    deuce: "Deuce",
    advantage: "Ventaja",
    game: "Ha ganado el "
}

const matchTennis = (match) => {
    const PLAYER_SCORE = {
      P1: SCORES.love,
      P2: SCORES.love
    };
    let endGame = false;
    console.log('**** juego iniciado ****');
    
    match.forEach(point => {
      if(!endGame){
        switch(PLAYER_SCORE[point]) {
          case SCORES.love:
            PLAYER_SCORE[point] = SCORES.fifteen
            break;
          case SCORES.fifteen:
            PLAYER_SCORE[point] = SCORES.thirty
            break;
          case SCORES.thirty:
            PLAYER_SCORE[point] = SCORES.forty
            if(PLAYER_SCORE.P1 == SCORES.forty && PLAYER_SCORE.P2 == SCORES.forty){
              PLAYER_SCORE.P1 = SCORES.deuce;
              PLAYER_SCORE.P2 = SCORES.deuce;
            }
            break;
          case SCORES.forty:
            PLAYER_SCORE[point] = SCORES.game
            endGame = true;
            break;
            
          case SCORES.deuce:
            if(PLAYER_SCORE.P1 == SCORES.deuce && PLAYER_SCORE.P2 == SCORES.deuce)
              PLAYER_SCORE[point] = SCORES.advantage;
            else{
              PLAYER_SCORE.P1 = SCORES.deuce;
              PLAYER_SCORE.P2 = SCORES.deuce;
            }
              
            break;
          case SCORES.advantage:
              PLAYER_SCORE[point] = SCORES.game;
              endGame = true;
            break;
          default:
            console.log('punto invalido.')
        }
      
        if(PLAYER_SCORE[point] == SCORES.game || PLAYER_SCORE[point] == SCORES.advantage){
          console.log(PLAYER_SCORE[point] + point)
        }else if(PLAYER_SCORE[point] == SCORES.deuce)
          console.log(PLAYER_SCORE[point])
        else 
          console.log(PLAYER_SCORE.P1 + ' - ' + PLAYER_SCORE.P2)
          
        if(PLAYER_SCORE[point] == SCORES.game)
          console.log('**** juego finalizado ****');
      }
    });
}

matchTennis(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2', 'P1', 'P1']);
matchTennis(['P3', 'P2', 'P2', 'P2', 'P2']);