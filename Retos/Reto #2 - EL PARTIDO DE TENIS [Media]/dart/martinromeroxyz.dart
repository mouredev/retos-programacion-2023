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

main() {
  
  List<String> game = List.of(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);
  
  Map<String, int> score = {
    'P1': 0,
    'P2': 0
  };
  
  int pointsToWin = 4;
  
  for(var player in game) {
    
    score[player] = score[player]! + 1;

    if(score['P1']! == pointsToWin && score['P2']! == pointsToWin) {
      score['P1'] = 0;
      score['P2'] = 0;
      pointsToWin = 2;
    } else if(score['P1'] == pointsToWin) {
      print('P1 wins');
    } else if(score['P2'] == pointsToWin) {
      print('P2 wins');
    }
  }  
}

