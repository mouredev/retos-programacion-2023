import 'dart:io';
import 'dart:math';

void main() {
  startGame();
}

void startGame() {
  print(
      "Hola, soy el \"Sombrero Seleccionador\"\nTendrás que responder cinco preguntas para ayudarme a descubrir tu casa de Hogwarts.\n");

  hatQuestions.forEach((element) {
    print(element.question);
    element.answers.forEach((key, value) {
      print(key);
    });
    final answer = getAnswer();
    if (answer != null) {
      final String house = element.answers.values.elementAt(answer - 1);
      houses.update(house, (value) => ++value, ifAbsent: () => houses[house] = 1);
    }
  });

  List<String> selectedHouse = [];
  int maxPoints = 0;

  houses.forEach((house, points) {
    if (points > maxPoints) {
      selectedHouse = [house];
      maxPoints = points;
    } else if (points == maxPoints) {
      selectedHouse.add(house);
    }
  });

  print(selectedHouse.length == 1
      ? "Lo tengo claro... ¡${selectedHouse[0].toUpperCase()}!"
      : "Es una decisión complicada... ¡${selectedHouse[Random().nextInt(selectedHouse.length)].toUpperCase()}!");
}

class HatQuestion {
  HatQuestion({required this.question, required this.answers});

  String question;
  Map<String, String> answers;
}

int? getAnswer() {
  print("Responde 1, 2, 3 o 4: \n");
  String? answer = stdin.readLineSync();
  if (answer == "1" || answer == "2" || answer == "3" || answer == "4") {
    return int.parse(answer!);
  } else
    return null;
}

final List<HatQuestion> hatQuestions = [
  HatQuestion(question: "¿Cómo te definirías?", answers: {
    "1. Valiente": "gryffindor",
    "2. Leal": "hufflepuff",
    "3. Sabio": "ravenclaw",
    "4. Ambicioso": "slytherin",
  }),
  HatQuestion(question: "¿Cuál es tu clase favorita?", answers: {
    "1. Vuelo": "gryffindor",
    "2. Pociones": "ravenclaw",
    "3. Defensa contra las artes oscuras": "slytherin",
    "4. Animales fantásticos": "hufflepuff",
  }),
  HatQuestion(question: "¿Dónde pasarías más tiempo?", answers: {
    "1. Invernadero": "hufflepuff",
    "2. Biblioteca": "ravenclaw",
    "3. En la sala común": "slytherin",
    "4. Explorando": "gryffindor",
  }),
  HatQuestion(question: "¿Cuál es tu color favorito?", answers: {
    "1. Rojo": "gryffindor",
    "2. Verde": "ravenclaw",
    "3. Azul": "slytherin",
    "4. Amarillo": "hufflepuff",
  }),
  HatQuestion(question: "¿Cuál es tu mascota?", answers: {
    "1. Sapo": "ravenclaw",
    "2. Lechuza": "gryffindor",
    "3. Gato": "hufflepuff",
    "4. Serpiente": "slytherin",
  }),
];

final Map<String, int> houses = {};
