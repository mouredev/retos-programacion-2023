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

List<List<String>> gameInput1 = [
  ["πΏ", "βοΈ"],
  ["βοΈ", "πΏ"],
  ["π", "βοΈ"]
];
List<List<String>> gameInput2 = [
  ["πΏ", "βοΈ"],
  ["βοΈ", "πΏ"],
  ["π", "βοΈ"],
  ["πΏ", "π"],
  ["πΏ", "π¦"],
  ["π¦", "π"],
  ["π", "π"],
  ["π", "βοΈ"],
  ["βοΈ", "π¦"],
  ["π¦", "π"],
  ["π", "πΏ"],
  ["πΏ", "πΏ"],
  ["π", "π"],
  ["βοΈ", "βοΈ"],
  ["π¦", "π¦"],
  ["π", "π"],
];

String piedraPapelTijeraLagartoSpock(List<List<String>> input) {
  int player1 = 0;
  int player2 = 0;
  String result = '';

  void addPointToWinner(List<String> play) {
    if (play.join() == "πβοΈ" || play.join() == "βοΈπ") {
      play[0] == "βοΈ" ? player1++ : player2++;
    } else if (play.join() == "πΏπ" || play.join() == "ππΏ") {
      play[0] == 'π' ? player1++ : player2++;
    } else if (play.join() == "πΏπ¦" || play.join() == "π¦πΏ") {
      play[0] == 'πΏ' ? player1++ : player2++;
    } else if (play.join() == "π¦π" || play.join() == "ππ¦") {
      play[0] == 'π¦' ? player1++ : player2++;
    } else if (play.join() == "πβοΈ" || play.join() == "βοΈπ") {
      play[0] == 'π' ? player1++ : player2++;
    } else if (play.join() == "βοΈπ¦" || play.join() == "π¦βοΈ") {
      play[0] == 'βοΈ' ? player1++ : player2++;
    } else if (play.join() == "π¦π" || play.join() == "ππ¦") {
      play[0] == 'π¦' ? player1++ : player2++;
    } else if (play.join() == "ππ" || play.join() == "ππ") {
      play[0] == 'π' ? player1++ : player2++;
    } else if (play.join() == "ππΏ" || play.join() == "πΏπ") {
      play[0] == 'π' ? player1++ : player2++;
    } else if (play.join() == "πΏβοΈ" || play.join() == "βοΈπΏ") {
      play[0] == 'πΏ' ? player1++ : player2++;
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
