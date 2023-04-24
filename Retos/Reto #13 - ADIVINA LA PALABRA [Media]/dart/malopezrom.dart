/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */




import 'dart:convert';
import 'dart:io';
import 'dart:math';
import 'package:http/http.dart' as http;

/**
 * Funcion de extension para obtener todos los indices de una ocurrrencia de un string
 */
extension StringExtension on String {
  List<int> indexAllOf(String search) {
    final indexes = <int>[];
    int i=-1;
    while((i=this.indexOf(search, i+1)) != -1) {
      indexes.add(i);
    }
    return indexes;
  }
}

/**
 * Interfaz para representar una letra y su posicion dentro de una palabra
 */
class Letter {
  String letter;
  int position;

  Letter({required this.letter, required this.position});
}
/**
 * Clase para manejar la logica de las palabras
 */
class GuessWord {
  late String _originalWord;
  late String _secretWord;
  List<String> _lettersUsed = [];
  List<Letter> _letters = [];
  static const API_WORDS = "https://clientes.api.greenborn.com.ar/public-random-word?c=9&l=8";
  /**
   * Constructor de la clase
   * @param word Palabra original a adivinar
   * @param handicap Porcentaje de letras a ocultar
   */
  GuessWord(String word, double handicap) {
    _originalWord = word;
    final numChars = (_originalWord.length * handicap).floor();
    var offuscated = _originalWord;
    for (var i = 0; i < numChars; i++) {
      final position = Random().nextInt(_originalWord.length);
      offuscated = offuscated.replaceRange(position, position + 1, '_');
    }
    _letters = offuscated.split('').asMap().entries.fold<List<Letter>>([], (acc, entry) {
      final index = entry.key;
      final letter = entry.value;
      return letter == '_' ? acc : [...acc, Letter(letter: letter, position: index)];
    });
    _secretWord = _offuscate();
  }
  /**
   * Metodo estatico para obtener una palabra aleatoria de la API
   */
  static Future<String> getWord() async {
    final response = await http.get(Uri.parse(API_WORDS));
    final data = jsonDecode(response.body) as List<dynamic>;
    return data[0] as String;
  }

  /**
   * Metodo para ocultar las letras de la palabra
   * @private
   */
  String _offuscate() {
    return _originalWord.split('').asMap().entries.map((entry) {
      final index = entry.key;
      final c = entry.value;
      return _letters.any((l) => l.position == index) ? c : '_';
    }).join('');
  }
  /**
   * Metodo para agregar una letra usada a la lista de letras que ya se han usado y no estan en la palabra
   * @param letter
   */
  void addUsedLetter(String letter) {
    if (!_lettersUsed.contains(letter)) {
      _lettersUsed.add(letter);
    }
  }
  /**
   * Metodo para obtener las letras usadas que no estan en la palabra
   */
  String lettersUsed() {
    return _lettersUsed.join(',');
  }
  /**
   * Metodo para agregar una letra que si esta en la palabra
   * @param letter
   */
  bool addLetter(Letter letter) {
    if (_letters.any((l) => l.position == letter.position && l.letter == '_')) {
      return false;
    } else {
      _letters.add(letter);
      _secretWord = _offuscate();
      return true;
    }
  }
  /**
   * Devuelve la palabra ofuscada
   */
  String get secretWord {
    return _secretWord;
  }
}
/**
 * Clase para manejar la logica del juego
 */
class HangedGame {
  late int attempts;
  late String word;
  late int maxAttempts;
  late bool isFinish;
  late GuessWord guessWordClass;
  UserInterface userInterface = new UserInterface();
  /**
   * Constructor de la clase
   * @param word Palabra a adivinar
   */
  HangedGame(String word) {
    this.word = word;
    attempts = 1;
    maxAttempts = 5;
    isFinish = false;
    maxAttempts = UserInterface.HandgedInput.length;
    guessWordClass = GuessWord(word, 0.6);
  }
  /**
   * Metodo que devuelve la palabra que se debe adivinar ofuscada
   */
  String guessWord() => guessWordClass.secretWord;

  /**
   * Metodo para adivinar una letra de la palabra
   * Si es una sola letra se agrega a la lista de letras usadas
   * Si es mas de una letra se intenta adivinar la palabra
   * @param letter Letra a adivinar o palabra a adivinar
   */
  void guessLetter(String letter) {
    if (letter.length > 1) {
      if (letter == word) {
        print("Has acertado la palabra $word");
        isFinish = true;
      } else {
        attempts++;
        print("Error! La palabra no es $letter");
        if (attempts > maxAttempts) {
          print("Has perdido.La palabra que buscamos es $word");
          isFinish = true;
        }
      }
    } else {
      if (word.contains(letter)) {
        word.indexAllOf(letter).forEach((element) {
          if (this.guessWordClass.addLetter(
              Letter(letter: letter, position: element))) {
            if (this.guessWordClass.secretWord == word) {
              print("Has acertado la palabra $word");
              isFinish = true;

            }

          }
        });
      }else{
        attempts++;
        this.guessWordClass.addUsedLetter(letter);
        print("Error! La palabra no contiene la letra $letter");
        if (attempts > maxAttempts) {
            print("Has perdido.La palabra que buscamos es $word");
            isFinish = true;
        }

      }


    }
  }

  /**
   * Metodo asincrono para iniciar el juego
   */
  Future<void> play() async {

    print("Bienvenido al juego del ahorcado");
    print("================================");
    while(!this.isFinish){
      print(UserInterface.HandgedInput[attempts-1]);
      print("Palabra a adivinar: ${this.guessWord()}");
      print("Intentos restantes: ${maxAttempts-attempts}");
      print("Letras usadas: ${this.guessWordClass.lettersUsed()}");
      final letter = await userInterface.prompt("Introduce una letra o palabra: ");
      if(letter != null){
        this.guessLetter(letter);
      }
    }

  }
}
/**
 * Clase para manejar la interfaz de usuario
 *
 */
class UserInterface{
  static const List<String> HandgedInput= [''''
         +---+
         |   |
         O   |
         |   |
             |
             |
     =========''','''
         +---+
         |   |
         O   |
        /|   |
             |
             |
     =========''','''
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
     =========''','''
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
     =========''','''
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
     ========='''



  ];
  /**
   * Metodo para leer una entrada de texto
   * @param message Mensaje a mostrar al usuario
   */
  Future<String?> prompt(String message) async {
    final input = stdin.readLineSync();
    return input;
  }

}
/**
 * Inicio del juego
 */

Future<void> main() async {
  final word = await GuessWord.getWord();
  HangedGame game = new HangedGame(word);
  game.play();

}