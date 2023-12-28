/*
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.

- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
  15 - Love
  30 - Love
  30 - 15
  30 - 30
  40 - 30
  Deuce
  Ventaja P1
  Ha ganado el P1
- Si quieres, puedes controlar errores en la entrada de datos.   
- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
*/
const scores_of_the_game = [
    'P1',
    'P1',
    'P2',
    'P2',
    'P1',
    'P2',
    'P1',
    'P2',
    'P1',
    'P2',
    'P2',
    'P2',
  ]
  
  function tennisGame(scores_game) {
    const scores = ['Love', '15', '30', '40']
    let p1_score = 0
    let p2_score = 0
  
    for (let i = 0; i <= scores_game.length; i++) {
      if (scores_game[i] === 'P1') {
        p1_score++
        console.log('Point for P1')
      } else if (scores_game[i] === 'P2') {
        p2_score++
        console.log('Point for P2')
      } else {
        console.log(`This input ${scores_game[i]} is not valid`)
        return
      }
  
      let p1 = p1_score < 4 ? scores[p1_score] : p1_score
      let p2 = p2_score < 4 ? scores[p2_score] : p2_score
  
      if ((p1_score >= 3 || p2_score >= 3) && p1_score == p2_score) {
        console.log(`Scoreboard:\nDeuce`)
      } else if (p1_score >= 4 || p2_score >= 4){
        if (Math.abs(p1_score - p2_score) >= 2){
          if (p1_score > p2_score) {
            console.log(`Scoreboard:\nThe Winner is PLAYER 1`)
          } else {
            console.log(`Scoreboard:\nThe Winner is PLAYER 2`)
          }
        } else if (p1_score > p2_score) {
          console.log(`Scoreboard:\nAdvantage for P1`)
        } else {
          console.log(`Scoreboard:\nAdvantage for P2`)
        } 
      } else {
        console.log(`Scoreboard:\nPlayer 1: ${p1}\nPlayer 2: ${p2}`)
      }
    }
    console.log('Full time!!')
  }
  
  tennisGame(scores_of_the_game)
  