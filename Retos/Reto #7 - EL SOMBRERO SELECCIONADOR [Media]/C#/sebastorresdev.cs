//# Reto #7: El sombrero seleccionador
//#### Dificultad: Media | Publicación: 13/02/23 | Corrección: 20/02/23

//## Enunciado

/*
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

//    Gryffindor -> 1
//    Slytherin  -> 2
//    Hufflepuff -> 3
//    Ravenclaw  -> 4

string prompt = @"                                         _ __
        ___                             | '  \
   ___  \ /  ___         ,'\_           | .-. \        /|
   \ /  | |,'__ \  ,'\_  |   \          | | | |      ,' |_   /|
 _ | |  | |\/  \ \ |   \ | |\_|    _    | |_| |   _ '-. .-',' |_   _
// | |  | |____| | | |\_|| |__    //    |     | ,'_`. | | '-. .-',' `. ,'\_
\\_| |_,' .-, _  | | |   | |\ \  //    .| |\_/ | / \ || |   | | / |\  \|   \
 `-. .-'| |/ / | | | |   | | \ \//     |  |    | | | || |   | | | |_\ || |\_|
   | |  | || \_| | | |   /_\  \ /      | |`    | | | || |   | | | .---'| |
   | |  | |\___,_\ /_\ _      //       | |     | \_/ || |   | | | |  /\| |
   /_\  | |           //_____//       .||`      `._,' | |   | | \ `-' /| |
        /_\           `------'        \ |   AND        `.\  | |  `._,' /_\
                                       \|       THE          `.\
                                            _  _  _  _  __ _  __ _ /_
                                           (_`/ \|_)/ '|_ |_)|_ |_)(_
                                           ._)\_/| \\_,|__| \|__| \ _)
                                                           _ ___ _      _
                                                          (_` | / \|\ ||__
                                                          ._) | \_/| \||___
";

var houseHogwarts = new Dictionary<string, int>
{
    { "Gryffindor", 0},
    { "Slytherin", 0},
    { "Hufflepuff", 0},
    { "Ravenclaw", 0}

};

var questions = new List<Tuple<string, List<string>>>
{
    new Tuple<string, List<string>>("¿Qué cualidad valoras más?", new List<string>
    {
        "1) Valentía",
        "2) Ambición",
        "3) Lealtad",
        "4) Inteligencia"
    }),
    new Tuple<string, List<string>>("¿Cuál es tu animal mágico favorito?", new List<string>
    {
        "1) León",
        "2) Serpiente",
        "3) Tejón",
        "4) Águila"
    }),
    new Tuple<string, List<string>>("Elige una asignatura mágica:", new List<string>
    {
        "1) Defensa contra las artes oscuras",
        "2) Pociones",
        "3) Cuidado de criaturas mágicas",
        "4) Adivinación"
    }),
    new Tuple<string, List<string>>("¿Qué cualidad te define mejor?", new List<string>
    {
        "1) Coraje",
        "2) Astucia",
        "3) Paciencia",
        "4) Sabiduría"
    }),
    new Tuple<string, List<string>>("¿Cuál sería tu lugar preferido en Hogwarts?", new List<string>
    {
        "1) El Gran Comedor",
        "2) Mazmorras",
        "3) Jardines",
        "4) Biblioteca"
    })
};
int answer;
bool isCorrect;

Console.ForegroundColor = ConsoleColor.Yellow;
Console.WriteLine(prompt);

Console.ForegroundColor = ConsoleColor.Green;
Console.WriteLine(@"Bienvenido a Hogwarts!,Soy el sombrero seleccionador, te realizare 5 preguntas 
que me ayudaran a determinar a que casa pertenceras (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)

Listo para empezar ?

Presione Enter para continuar..."
);
Console.ReadKey();
Console.ResetColor();

DetermineTheHogwartsHouse();



void DetermineTheHogwartsHouse()
{
    foreach (var question in questions)
    {
        Console.WriteLine(question.Item1);
        for (int i = 0; i < question.Item2.Count; i++)
        {
            Console.WriteLine(question.Item2[i]);
        }

        do
        {
            Console.Write("Resp: ");
            isCorrect = int.TryParse(Console.ReadLine(), out answer);
        } while (!isCorrect || answer < 1 || answer > 4);


        switch (answer)
        {
            case 1:
                houseHogwarts["Gryffindor"]++;break;
            case 2:
                houseHogwarts["Slytherin"]++; break;
            case 3:
                houseHogwarts["Hufflepuff"]++; break;
            case 4:
                houseHogwarts["Ravenclaw"]++; break;
            default:
                break;
        }
    }

    string selectedHouse = "Gryffindor";

    foreach (var house in houseHogwarts)
    {
        if (house.Value > houseHogwarts[selectedHouse])
            selectedHouse = house.Key;
    }
    Console.WriteLine($"Usted pertence a la casa {selectedHouse}");
}