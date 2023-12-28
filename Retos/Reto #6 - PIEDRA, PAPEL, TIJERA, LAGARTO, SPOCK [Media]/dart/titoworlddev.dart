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

List<List<String>> gameInput1 = [
  ["🗿", "✂️"],
  ["✂️", "🗿"],
  ["📄", "✂️"]
];
List<List<String>> gameInput2 = [
  ["🗿", "✂️"],
  ["✂️", "🗿"],
  ["📄", "✂️"],
  ["🗿", "📄"],
  ["🗿", "🦎"],
  ["🦎", "📄"],
  ["📄", "🖖"],
  ["🖖", "✂️"],
  ["✂️", "🦎"],
  ["🦎", "🖖"],
  ["🖖", "🗿"],
  ["🗿", "🗿"],
  ["📄", "📄"],
  ["✂️", "✂️"],
  ["🦎", "🦎"],
  ["🖖", "🖖"],
];

String piedraPapelTijeraLagartoSpock(List<List<String>> input) {
  int player1 = 0;
  int player2 = 0;
  String result = '';

  void addPointToWinner(List<String> play) {
    if (play.join() == "📄✂️" || play.join() == "✂️📄") {
      play[0] == "✂️" ? player1++ : player2++;
    } else if (play.join() == "🗿📄" || play.join() == "📄🗿") {
      play[0] == '📄' ? player1++ : player2++;
    } else if (play.join() == "🗿🦎" || play.join() == "🦎🗿") {
      play[0] == '🗿' ? player1++ : player2++;
    } else if (play.join() == "🦎🖖" || play.join() == "🖖🦎") {
      play[0] == '🦎' ? player1++ : player2++;
    } else if (play.join() == "🖖✂️" || play.join() == "✂️🖖") {
      play[0] == '🖖' ? player1++ : player2++;
    } else if (play.join() == "✂️🦎" || play.join() == "🦎✂️") {
      play[0] == '✂️' ? player1++ : player2++;
    } else if (play.join() == "🦎📄" || play.join() == "📄🦎") {
      play[0] == '🦎' ? player1++ : player2++;
    } else if (play.join() == "📄🖖" || play.join() == "🖖📄") {
      play[0] == '📄' ? player1++ : player2++;
    } else if (play.join() == "🖖🗿" || play.join() == "🗿🖖") {
      play[0] == '🖖' ? player1++ : player2++;
    } else if (play.join() == "🗿✂️" || play.join() == "✂️🗿") {
      play[0] == '🗿' ? player1++ : player2++;
    }
  }

  input.forEach((e) => addPointToWinner(e));

  result = player1 == player2
      ? 'Tie'
      : player1 > player2
          ? 'Player 1'
          : 'Player 2';

  return result;
}

void main() {
  print(piedraPapelTijeraLagartoSpock(gameInput1));
  print(piedraPapelTijeraLagartoSpock(gameInput2));
}
