import 'dart:io';
import 'dart:math' as math;

typedef Position = Map<String, int>;
typedef Board = List<List<ItemsEnum>>;
typedef Question = Map<String, String>;

enum Moves {
  north("norte"),
  south("sur"),
  east("este"),
  west("oeste");

  const Moves(this.value);
  final String value;
}

enum ItemsEnum {
  start("🚪"),
  phantom("👻"),
  candy("🍭"),
  empty("⬜️"),
  current("📍");

  const ItemsEnum(this.value);
  final String value;
}

final List<Map<String, String>> questions = [
  {
    "question": "¿Cuál es la capital de Francia?",
    "answer": "París",
  },
  {
    "question": "¿Cuál es el planeta más grande del sistema solar?",
    "answer": "Júpiter",
  },
  {
    "question": "¿Cuál es el río más largo del mundo?",
    "answer": "El río Amazonas",
  },
  {
    "question": "¿Quién escribió 'Don Quijote de la Mancha'?",
    "answer": "Miguel de Cervantes",
  },
  {
    "question": "¿En qué año comenzó la Primera Guerra Mundial?",
    "answer": "1914",
  },
  {
    "question": "¿Cuál es el símbolo químico del oro?",
    "answer": "Au",
  },
  {
    "question": "¿Cuál es la montaña más alta del mundo?",
    "answer": "El Monte Everest",
  },
  {
    "question": "¿Quién pintó la 'Mona Lisa'?",
    "answer": "Leonardo da Vinci",
  },
  {
    "question": "¿Cuál es el océano más grande del mundo?",
    "answer": "El océano Pacífico",
  },
  {
    "question": "¿En qué año se fundó Google?",
    "answer": "1998",
  },
  {
    "question": "¿Quién escribió 'Romeo y Julieta'?",
    "answer": "William Shakespeare",
  },
  {
    "question": "¿Cuál es el símbolo químico del hidrógeno?",
    "answer": "H",
  },
  {
    "question": "¿Cuál es el elemento más abundante en la Tierra?",
    "answer": "El oxígeno",
  },
  {
    "question": "¿Cuál es el quinto planeta en el sistema solar?",
    "answer": "Júpiter",
  },
  {
    "question": "¿Cuál es la capital de Japón?",
    "answer": "Tokio",
  },
  {
    "question":
        "¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?",
    "answer": "1776",
  },
  {
    "question": "¿Quién fue el primer presidente de Estados Unidos?",
    "answer": "George Washington",
  },
  {
    "question": "¿Cuál es la fórmula química del agua?",
    "answer": "H2O",
  },
  {
    "question": "¿Quién fue el primer ser humano en orbitar la Tierra?",
    "answer": "Yuri Gagarin",
  },
  {
    "question": "¿Cuál es el metal más abundante en la corteza terrestre?",
    "answer": "El aluminio",
  },
  {
    "question": "¿Cuál es la capital de Australia?",
    "answer": "Camberra",
  },
  {
    "question": "¿Quién escribió '1984'?",
    "answer": "George Orwell",
  },
  {
    "question": "¿Cuál es el símbolo químico del carbono?",
    "answer": "C",
  },
  {
    "question": "¿En qué año se cayó el Muro de Berlín?",
    "answer": "1989",
  },
  {
    "question": "¿Quién fue el primer hombre en la Luna?",
    "answer": "Neil Armstrong",
  },
  {
    "question": "¿Cuál es la capital de China?",
    "answer": "Pekín",
  },
  {
    "question": "¿En qué año se descubrió la penicilina?",
    "answer": "1928",
  },
  {
    "question": "¿Cuál es el océano más pequeño del mundo?",
    "answer": "El océano Ártico",
  },
  {
    "question": "¿Quién escribió 'Cien años de soledad'?",
    "answer": "Gabriel García Márquez",
  },
  {
    "question": "¿Cuál es la moneda de Japón?",
    "answer": "El yen",
  },
  {
    "question": "¿En qué año se fundó Microsoft?",
    "answer": "1975",
  },
];

final Map<ItemsEnum, Position> positions = {};

final Set<ItemsEnum> uniqueItems = {ItemsEnum.start, ItemsEnum.candy};

final List<ItemsEnum> items = ItemsEnum.values;

void main(List<String> arguments) {
  final board = generateMansion();

  runGame(board);
}

Board generateMansion() {
  final Board board = [];

  final Set<ItemsEnum> addedItems = {};

  for (var y = 0; y < 4; y++) {
    board.insert(y, []);
    for (var x = 0; x < 4; x++) {
      final ItemsEnum randomItem = getRandomItem(addedItems);

      addedItems.add(randomItem);

      if (randomItem == ItemsEnum.start) {
        positions.addAll({
          ItemsEnum.start: {'x': x, 'y': y}
        });
      }

      if (randomItem == ItemsEnum.candy) {
        positions.addAll({
          ItemsEnum.candy: {'x': x, 'y': y}
        });
      }

      board[y].insert(x, randomItem);
    }
  }

  return board;
}

ItemsEnum getRandomItem(Set<ItemsEnum> addedItems) {
  ItemsEnum item;

  do {
    final randomItem = math.Random().nextInt((items.length - 1)).floor();
    item = items[randomItem];
  } while (uniqueItems.contains(item) && addedItems.contains(item));

  return item;
}

void showCurrentPosition(Board board) {
  print("Actualmente estás aquí");

  final Position currentPosition = positions[ItemsEnum.start]!;

  for (var y = 0; y < board.length; y++) {
    final List<String> rows = board[y]
        .asMap()
        .map((int x, ItemsEnum item) {
          if (x == currentPosition['x'] && y == currentPosition['y']) {
            return MapEntry(x, ItemsEnum.current.value);
          }

          if (item != ItemsEnum.start) {
            return MapEntry(x, ItemsEnum.empty.value);
          }

          return MapEntry(x, item.value);
        })
        .values
        .toList();

    print(rows);
  }
}

String? getMove() {
  final Set<Moves> possibleMoves = {...Moves.values};
  final Position currentPosition = positions[ItemsEnum.start]!;

  if (currentPosition['y'] == 0) {
    possibleMoves.remove(Moves.north);
  } else if (currentPosition['y'] == 3) {
    possibleMoves.remove(Moves.south);
  }

  if (currentPosition['x'] == 0) {
    possibleMoves.remove(Moves.west);
  } else if (currentPosition['x'] == 3) {
    possibleMoves.remove(Moves.east);
  }

  String? response = "";
  final List<String> moves = possibleMoves.map((move) => move.value).toList();

  while (!moves.contains(response?.toLowerCase() ?? "")) {
    print('A donde quieres desplazarte? (${moves.join("/")})');
    response = stdin.readLineSync()!;
  }

  return response;
}

Position getNewPosition(String move) {
  final Position position = positions[ItemsEnum.start]!;

  if (move == Moves.north.value) {
    return {"x": position['x']!, "y": position['y']! - 1};
  }
  if (move == Moves.south.value) {
    return {"x": position['x']!, "y": position['y']! + 1};
  }
  if (move == Moves.east.value) {
    return {"x": position['x']! + 1, "y": position['y']!};
  }
  return {"x": position['x']! - 1, "y": position['y']!};
}

updatePosition(Position position) {
  positions.addAll({ItemsEnum.start: position});
}

bool handleAskQuestion(bool containPhantom) {
  int counter = containPhantom ? 2 : 1;

  while (counter > 0) {
    if (containPhantom) print("Apareció un fantasma, respondes 2 preguntas!");

    final int numRandomQuestion =
        math.Random().nextInt(questions.length).floor();

    final Map<String, String> test = questions[numRandomQuestion];

    print(test['question']);

    final String response = stdin.readLineSync() ?? '';

    final correctAnswer =
        response.toLowerCase() == test['answer']?.toLowerCase();

    if (correctAnswer) {
      counter--;
      questions.removeAt(numRandomQuestion);
    } else {
      print("Respuesta incorrecta!");
    }
  }

  return counter == 0;
}

bool validateFinishGame(Board board, String move) {
  final Map<String, int> newPosition = getNewPosition(move);
  final Position position = positions[ItemsEnum.candy]!;

  if (newPosition['x'] == position['x'] && newPosition['y'] == position['y']) {
    updatePosition(newPosition);
    return true;
  }

  if (handleAskQuestion(
      board[newPosition['y']!][newPosition['x']!] == ItemsEnum.phantom)) {
    updatePosition(newPosition);
  }

  return false;
}

void runGame(Board board) {
  bool finishGame = false;

  while (!finishGame) {
    showCurrentPosition(board);
    final String? move = getMove();
    finishGame = validateFinishGame(board, move!);
  }

  print("Felicidades, haz completado el juego 🎉🎉!");
}
