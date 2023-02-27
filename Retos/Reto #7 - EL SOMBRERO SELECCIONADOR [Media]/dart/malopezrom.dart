/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

import 'dart:io';

/**
 * Llamada a la función principal
 */
void main(){
  quizGame();
}


/**
 * Interface que pregunta una respuesta y sus respuestas
 */
class Question{
  String question;
  List<Answer> answers;

  Question(this.question, this.answers);

  Answer ask(){
    print(question);
    int i=1;
    answers.forEach((element) {
      print("${i+1}. ${element.answer}");
      i++;

    });
    int answer = int.parse(stdin.readLineSync()!);
    return answers[answer-1];
  }


}

/**
 * Interface que representa una respuesta y sus puntos
 */
class Answer{
 String answer;
 List<Point> points;
    Answer(this.answer, this.points);
 int getPoints(Team team) {
   return points.firstWhere((p) => p.name == team, orElse: () => Point(team, 0)).points;
 }
}

/**
 * Interface que representa los puntos de cada equipo
 */
class Point{
  Team name;
  int points;
  Point(this.name, this.points);
}
/**
 * Enumerado que representa los equipos
 */
enum Team {
  Celtic,
  Farsa,
  GranadaCF,
  RMadrid
}
/**
 * Extension del enumerado Team para obtener el nombre del equipo
 */
extension TeamInfo on Team {
  String get name {
    switch (this) {
      case Team.Celtic:
        return "Celtic de Pulianas";
      case Team.Farsa:
        return "Farsa el equipo de los culerdos";
      case Team.GranadaCF:
        return "Vamos mi grana";
      case Team.RMadrid:
        return "Central Lechera";

    }
  }
}

/**
 * Array de preguntas y respuestas y sus puntos correspondientes a cada equipo
 */
List<Question> quizz = [

   Question(
      "Se acerca la fecha del próximo partido de tu equipo, ¿cómo te sientes?",
      [
          Answer("Nervioso/a, todos los partidos de mi equipo los siento con pasión.", [Point(Team.Celtic, 10), Point(Team.Farsa, 0), Point(Team.GranadaCF, 9), Point(Team.RMadrid, 2)]),
          Answer("No es relevante, cuando llegue la hora ya me sentaré a verlo tranquilamente.",[Point(Team.Celtic, 0), Point(Team.Farsa, 7), Point(Team.GranadaCF,2), Point(Team.RMadrid, 7)]),
          Answer("Los vecinos hablan sobre el partido los días previos, se nota el ambiente en la calle.",[Point(Team.Celtic, 4), Point(Team.Farsa, 10), Point(Team.GranadaCF,1), Point(Team.RMadrid, 9)]),
          Answer("No como ni duermo los días previos de los nervios. Da igual que sean dieciseisavos de Copa o la última jornada de Liga, lo vivo.",[Point(Team.Celtic, 8), Point(Team.Farsa, 1), Point(Team.GranadaCF,10), Point(Team.RMadrid, 0)])
      ]),

  new Question(
      "Estás en un bar y te das cuenta de que nadie es del mismo equipo que tú, ¿qué piensas?",
      [
          Answer("Joder, mira que es raro.", [Point(Team.Celtic, 10), Point(Team.Farsa, 0), Point(Team.GranadaCF, 3), Point(Team.RMadrid, 2)]),
          Answer("Ya está esto lleno de borregos, míralos, todos viendo el Chirincirco.",[Point(Team.Celtic, 1), Point(Team.Farsa, 7), Point(Team.GranadaCF,4), Point(Team.RMadrid, 9)]),
          Answer("Normal, si somos 4 gatos. Eh, pero con orgullo, coño.",[Point(Team.Celtic, 2), Point(Team.Farsa, 10), Point(Team.GranadaCF,1), Point(Team.RMadrid, 2)]),
          Answer("Ups, igual tenía que haber ido al de dos calles más abajo...",[Point(Team.Celtic, 10), Point(Team.Farsa, 1), Point(Team.GranadaCF,4), Point(Team.RMadrid, 1)])
      ]),
  Question(
      "Penalti a favor del Madrid/Barcelona. En la repetición se ve que no era. ¿Cómo reaccionas?",
      [
          Answer("Ya están robando estos perros.", [Point(Team.Celtic, 10), Point(Team.Farsa, 0), Point(Team.GranadaCF, 9), Point(Team.RMadrid, 2)]),
          Answer("Esto es una puta vergüenza! Soy el entrenador y los saco del campo, que se rían de su madre.",[Point(Team.Celtic, 3), Point(Team.Farsa, 10), Point(Team.GranadaCF,3), Point(Team.RMadrid, 9)]),
          Answer("Ya la tenemos liada, ahora a aguantar a la prensa toda la semana...",[Point(Team.Celtic, 4), Point(Team.Farsa, 0), Point(Team.GranadaCF,9), Point(Team.RMadrid, 2)]),
          Answer("Ya estamos con la prensa mamadora del movimiento",[Point(Team.Celtic, 10), Point(Team.Farsa, 0), Point(Team.GranadaCF,9), Point(Team.RMadrid, 2)])
      ]),
  Question(
      "Caso contrario: última jornada de liga y una victoria de tu equipo hace que supere el objetivo marcado al principio del año.",
      [
          Answer("Coño, coño, coño, coño, coño, coño. Como les dé por ganar me desnudo en la fuente del pueblo.", [Point(Team.Celtic, 10), Point(Team.Farsa, 0), Point(Team.GranadaCF, 9), Point(Team.RMadrid, 2)]),
          Answer("Yaya, enséñame unos rezos de esos, que es para una cosa del finde.",[Point(Team.Celtic, 1), Point(Team.Farsa, 9), Point(Team.GranadaCF,2), Point(Team.RMadrid, 6)]),
          Answer("Pase lo que pase ha sido un temporadón, ¡qué orgullo de equipo!",[Point(Team.Celtic, 6), Point(Team.Farsa, 5), Point(Team.GranadaCF,4), Point(Team.RMadrid, 4)]),
          Answer("Con lo bien que vivía yo cuando éramos mediocres, qué ganas de matarnos con los nervios.",[Point(Team.Celtic, 10), Point(Team.Farsa, 1), Point(Team.GranadaCF,9), Point(Team.RMadrid, 4)])
      ]),
  Question(
      "Final de la temporada, tu equipo desciende a Segunda División. Vaya veranito te vas a pegar...",
      [
          Answer("JAJAJAJAJAJAJAJAJA EN SEGUNDA DICE, ¡QUE SOY DEL MADRID/BARÇA, TOLAI!", [Point(Team.Celtic, 0), Point(Team.Farsa, 10), Point(Team.GranadaCF, 0), Point(Team.RMadrid, 10)]),
          Answer("Lloro, me enfado, durante las primeras semanas va a ser una auténtica pesadilla. No puede pasarnos a nosotros...",[Point(Team.Celtic, 5), Point(Team.Farsa, 7), Point(Team.GranadaCF,3), Point(Team.RMadrid, 4)]),
          Answer("No pudo ser, nos vino grande la categoría. Volveremos con más fuerza, ¡seguro!",[Point(Team.Celtic, 7), Point(Team.Farsa, 2), Point(Team.GranadaCF,9), Point(Team.RMadrid, 2)]),
          Answer("Otra vez al hoyo. El año que viene mi abono se lo pueden meter por el...",[Point(Team.Celtic, 4), Point(Team.Farsa, 0), Point(Team.GranadaCF,9), Point(Team.RMadrid, 0)])
      ])
];


/**
 * Función que calcula el equipo al que perteneces
 */
void yourTeamsIs(Map<Team, int> points) {
  var teamWithMaxPoints = points.entries.reduce((a, b) => a.value > b.value ? a : b).key;
  print('Tu equipo es: ${teamWithMaxPoints.name}');
}


/**
 * Función principal que llama a la función que muestra las preguntas
 */
void quizGame() {
  var points = <Team, int>{};
  points[Team.Celtic] = 0;
  points[Team.Farsa] = 0;
  points[Team.GranadaCF] = 0;
  points[Team.RMadrid] = 0;

  print("Bienvenido al test de fútbol. Responde a las siguientes preguntas y averigua qué equipo eres:\n");

  quizz.forEach((question) {
    var answer = question.ask();
    answer.points.forEach((point) {
      points[point.name] = (answer.getPoints(point.name) + (points[point.name] ?? 0));
    });
  });

  yourTeamsIs(points);
}




