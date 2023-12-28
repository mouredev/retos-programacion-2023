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


/**
 * Funcion main con los casos de ejemplo.
 */
main() {

  var game = Game([["🗿", "✂️"],
  ["✂️", "🗿"],
  ["🦎", "✂️"],
  ["🗿", "📄"],
  ["📄", "🗿"],
  ["🗿", "🗿"],
  ["🖖", "🦎"],
  ["🖖", "✂️"]],"Player 1","Player 2");
  print("El resultado es : ${evaluateGame(game)}");

  var game2 = Game([["🗿", "✂️"],
      ["🦎", "✂️"],
      ["🖖", "🗿"],
      ["🖖", "🖖"],

      ],"Player 1","Player 2");
  print("El resultado es : ${evaluateGame(game2)}");


  var game3 = Game(
      [
        ["🖖", "🦎"],
        ["🦎", "🖖"],
        ["🖖", "🖖"],

      ], "Player 1", "Player 2");
  print("El resultado es : ${evaluateGame(game3)}");

}



/*
Objeto que representa las opciones de juego.
*/
var options = ["🗿","📄","✂️","🦎","🖖"];
/**
 * Enumerado que representa un resultado de una jugada.
 */
enum Result {Tie,Player1, Player2}

/**
 * Combinaciones de jugadas.
 */
Map<String,Map<String,Result>> combinations =
{ //Piedra
  "🗿": {"🗿": Result.Tie, "📄": Result.Player2, "✂️": Result.Player1, "🦎": Result.Player1, "🖖": Result.Player2},
  //Papel
  "📄": {"🗿": Result.Player1, "📄": Result.Tie, "✂️": Result.Player2, "🦎": Result.Player2, "🖖": Result.Player1},
  //Tijera
  "✂️": {"🗿": Result.Player2, "📄": Result.Player1, "✂️": Result.Tie, "🦎": Result.Player1, "🖖": Result.Player2},
  //Lagarto
  "🦎": {"🗿": Result.Player2, "📄": Result.Player1, "✂️": Result.Player2, "🦎": Result.Tie, "🖖": Result.Player1},
  //Spock
  "🖖": {"🗿": Result.Player1, "📄": Result.Player2, "✂️": Result.Player1, "🦎": Result.Player2, "🖖": Result.Tie}
};


/**
 * Clase que representa una jugada
 */
class Game{
  String player1;
  String player2;
  List<List<String>> game;
  Game(this.game,this.player1, this.player2);

}

/**
 * Funcion que busca el ganador si lo hay de una lista de jugadas
 * @param listOfGame Listado de jugadas
 * @return Resultado de la jugada
 * @see Result
 */
Result foundWinner(List<Result> game){
  var player1= game.where((element) => element==Result.Player1).length;
  var player2= game.where((element) => element==Result.Player2).length;

  if(player1>player2){
    return Result.Player1;
  }
  else if(player2>player1){
    return Result.Player2;
  }
  else{
    return Result.Tie;
  }
}


/**
 * Funcion que evalua una partida de piedra, papel, tijera , lagarto o spock
 * @param game objeto que representa un juego con los jugadores y las jugadas de cada uno
 * @return String con el nombre del jugador o empate en el que no hay ningun ganador
 */

String evaluateGame(Game game) {
  List<Result> results = [];
  for (var e in game.game) {
    if (combinations.containsKey(e[0]) && combinations.containsKey(e[1])) {
      if (combinations[e[0]]![e[1]] == Result.Player1) {
        results.add(Result.Player1);
      } else if (combinations[e[0]]![e[1]] == Result.Player2) {
        results.add(Result.Player2);
      }
    }
  }

  switch(foundWinner(results)){
    case Result.Player1:
      return game.player1;
    case Result.Player2:
      return game.player2;
    case Result.Tie:
      return "empate";
  }




}