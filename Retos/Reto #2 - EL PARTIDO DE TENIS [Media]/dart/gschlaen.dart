import 'dart:io';

void main() {
  print('Ingresa la secuencia de puntos con el formato P1, P2, etc');
  String? text = stdin.readLineSync();
  if (text != null) {
    printGame(text);
  }
}

printGame(text) {
  final P1 = "P1";
  final P2 = "P2";
  final sec = getWords(text, P1, P2);

  final scores = ["love", "15", "30", "40"];

  var p1 = 0;
  var p2 = 0;
  var game = [];

  if (sec.length == 0) {
    print("La secuencia no es valida");
  } else {
    loop:
    for (int i = 0; i < sec.length; i++) {
      sec[i] == "P1" ? p1 += 1 : p2 += 1;

      if (p1 < 3 && p2 < 3 || p1 == 3 && p2 < 3 || p1 < 3 && p2 == 3) {
        game.add("${scores[p1]} - ${scores[p2]}");
      } else {
        switch (p1 - p2) {
          case 0:
            {
              game.add("Deuce");
            }
            break;

          case 1:
            {
              game.add("Ventaja P1");
            }
            break;

          case -1:
            {
              game.add("Ventaja P2");
            }
            break;

          case 2:
            {
              game.add("Ha ganado el P1");
            }
            break;

          case -2:
            {
              game.add("Ha ganado el P2");
            }
            break;

          default:
            {
              game = ["La partida ingresada no es válida"];
              break loop;
            }
        }
      }
    }
    game.map((e) => print(e)).toList();
  }
}

List<String> getWords(String text, String word1, String word2) {
  var words = <String>[];
  var regex = RegExp("$word1|$word2");
  var match = regex.allMatches(text);

  for (var m in match) {
    words.add(m.group(0)!);
  }

  return words;
}
