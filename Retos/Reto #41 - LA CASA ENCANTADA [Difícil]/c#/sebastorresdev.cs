using System.Text;

namespace ConsoleApp;

internal class Program
{
    static void Main(string[] args)
    {
        Board board = new(4);
        GameBoard gameBoard = new(board);
        QuizGame game = new(gameBoard);
        game.Run();
    }
}

public class QuizGame
{
    private GameBoard _gameBoard;

    private readonly List<Quiz> _questions;
    private int _currentQuestionIndex;
    private int _live;

    public QuizGame(GameBoard gameBoard)
    {
        _questions = LoadQuestions();
        _currentQuestionIndex = 0;
        _live = 5;
        _gameBoard = gameBoard;

        Console.OutputEncoding = Encoding.UTF8;
        Console.Title = "La casa encantada";
        Instructions();
    }

    private static void Instructions()
    {
        string prompt = @"
¡Bienvenido a la Mansión Encantada!
-----------------------------------

Estás a punto de embarcarte en una aventura tenebrosa en una mansión abandonada llena de misterios y acertijos. 
Tu misión es encontrar la elusiva habitación de los dulces escondidos en esta casa embrujada.

🏰 La Mansión:
La mansión cuanta con habitacones donde habra una puerta de inicio y usted tendra que desplazarse 
hasta encontrar la habilation de duces, si cae en una habitacion de fantasma tendra que resolver dos 
acertijos para poder salir de alli. todas las habitaciones cuentan con acertijos o fantasmas.

Prepárate para adentrarte en la oscuridad y demostrar tu astucia resolviendo enigmas. 
¿Estás listo para enfrentar los desafíos de la Mansión Encantada? ¡Buena suerte!

Presiona una tecla para iniciar...
";

        Console.WriteLine(prompt);
        Console.ReadKey();
    }
    public void Run()
    {
        Console.Clear();
        Random random = new ();

        while (true)
        {
            _gameBoard.Run();
            int count = _gameBoard.GetNumberOfQuestions();
            
            while (0 < count)
            {
                _gameBoard.DisplayBoard();
                ShowLive();

                if (count == 3)
                {
                    Console.WriteLine("🎉 ¡FELICIDADES, HAS GANADO! 🎉");
                    Console.WriteLine("Presione un tacla para salir...");
                    Console.ReadKey();
                    return;
                }

                _currentQuestionIndex = random.Next(_questions.Count - 1);
                DisplayQuestion();

                var answer = Console.ReadLine().ToUpper();

                if (ValidateAnswer(answer))
                {
                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                    Console.WriteLine("🎉 Respuesta correcta! 🎉");
                    count--;
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.DarkRed;
                    Console.WriteLine("💀 Respuesta incorrecta! 💀");
                    _live--;
                    ShowAnswer();
                }
                Console.ResetColor();
                if (_live == 0)
                {
                    Console.WriteLine("❌ GAME OVER ❌");
                    Console.WriteLine("Presione un tacla para volver al menu principal...");
                    Console.ReadKey();
                    return;
                }
            }
        }
    }

    private void ShowLive()
    {
        Console.WriteLine($"Vida: {_live}");
    }

    private bool ValidateAnswer(string answer)
    {
        var quiz = _questions[_currentQuestionIndex];
        if (answer.Length == 1 && char.ToUpper(answer[0]) >= 'A' && char.ToUpper(answer[0]) < 'A' + quiz.Options.Count)
        {
            int selectOption = char.ToUpper(answer[0]) - 'A';
            return selectOption == quiz.Answer;
        }
        return false;
    }

    private void ShowAnswer()
    {
        var quiz = _questions[_currentQuestionIndex];
        Console.ForegroundColor = ConsoleColor.DarkGray;
        Console.WriteLine($"La respuesta correcta es: {quiz.Options[quiz.Answer]}");
    }

    private static List<Quiz> LoadQuestions()
    {
        // Tambien se puede extraer de una fuente externa
        return new()
        {
            new Quiz()
            {
                Question = " ¿Qué es lo que tiene ojos pero no puede ver?",
                Answer = 0,
                Options = new List<string>{ "Un libro.", "Un teléfono.", "Un pez.", "Un árbol." }
            },  // 1
            new Quiz()
            {
                Question = "¿Qué palabra se escribe incorrectamente en todos los diccionarios?",
                Answer = 0,
                Options = new List<string>{ "Incorrectamente.", "Palabra.", "Diccionarios.", "Todos." }
            },  // 2
            new Quiz()
            {
                Question = "Si tienes tres manzanas y tomas dos, ¿cuántas manzanas te quedan?",
                Answer = 3,
                Options = new List<string>{ "Ninguna.", "Una.", "Dos.", "Tres." }
            },  // 3
            new Quiz()
            {
                Question = "Si un avión se estrella justo en la frontera entre Estados Unidos y Canadá, ¿dónde entierras a los sobrevivientes?",
                Answer = 2,
                Options = new List<string>{ "En Estados Unidos.", "En Canadá.", "No los entierras.", "En la frontera." }
            },  // 4
            new Quiz()
            {
                Question = "Si tienes un cubo de hielo en un vaso y el hielo se derrite, ¿qué le sucede al nivel del agua?",
                Answer = 2,
                Options = new List<string>{ "Aumenta.", "Disminuye.", "Permanece igual.", "Depende del clima." }
            },  // 5
            new Quiz()
            {
                Question = "¿Cuál es la próxima letra en esta serie: A, E, I, M, ___?",
                Answer = 1,
                Options = new List<string>{ "O.", "U.", "R.", "L." }
            },  // 6
            new Quiz()
            {
                Question = "Cuanto más lo quites, más grande se vuelve. ¿Qué es?",
                Answer = 0,
                Options = new List<string>{ "Un agujero.", "Un árbol.", "Un libro.", "Un coche." }
            },  // 7
            new Quiz()
            {
                Question = "¿Cuántos meses tienen 28 días?",
                Answer = 2,
                Options = new List<string>{ "Uno.", "Seis.", "Todos.", "Doce." }
            },  // 8
            new Quiz()
            {
                Question = "¿Cuál es el animal que camina por la mañana con cuatro patas, por la tarde con dos patas y por la noche con tres patas?",
                Answer = 2,
                Options = new List<string>{ "Perro.", "Gato.", "Hombre.", "Elefante." }
            },  // 9
            new Quiz()
            {
                Question = "Tengo llaves pero no puedo abrir ninguna puerta. ¿Qué soy?",
                Answer = 3,
                Options = new List<string>{ "Una computadora.", "Una escuela.", "Un músico.", "Un libro." }
            },  // 10
            new Quiz()
            {
                Question = "¿Qué es lo que puede viajar alrededor del mundo sin moverse?",
                Answer = 0,
                Options = new List<string>{ "Una carta.", "Un teléfono.", "Un avión.", "El viento." }
            },  // 11
            new Quiz()
            {
                Question = "¿Qué es lo que es mío y sin embargo, lo usas más que yo?",
                Answer = 0,
                Options = new List<string>{ "Mi nombre.", "Mis zapatos.", "Mi casa.", "Mi teléfono." }
            },  // 12
            new Quiz()
            {
                Question = "Si lanzas una moneda al aire, ¿cuáles son las posibilidades de que caiga de canto?",
                Answer = 1,
                Options = new List<string>{ "50%.", "0%.", "25%.", "75%." }
            },  // 13
            new Quiz()
            {
                Question = "¿Qué palabra se deletrea incorrectamente en todos los diccionarios?",
                Answer = 1,
                Options = new List<string>{ "Incorrectamente.", "Deletrea.", "Diccionarios.", "Todos." }
            },  // 14
            new Quiz()
            {
                Question = "¿Qué es lo que tiene dientes pero no puede masticar?",
                Answer = 1,
                Options = new List<string>{ "Un león.", "Un engranaje.", "Un tren.", "Un piano." }
            },  // 15
            new Quiz()
            {
                Question = "Cuando intento comer, estoy roto. Cuando bebo, estoy bien. ¿Qué soy?",
                Answer = 0,
                Options = new List<string>{ "Un vaso.", "Un plato.", "Un tenedor.", "Un cuchillo." }
            },  // 16
            new Quiz()
            {
                Question = "¿Qué elemento químico es representado por el símbolo 'Fe' en la tabla periódica?",
                Answer = 2,
                Options = new List<string> { "Hidrógeno", "Oxígeno", "Hierro", "Plata" }
            },  // 17
            new Quiz()
            {
                Question = "¿Cuál es el planeta más cercano al Sol en nuestro sistema solar?",
                Answer = 2,
                Options = new List<string> { "Venus", "Marte", "Mercurio", "Júpiter" }
            }, // 18
            new Quiz()
            {
                Question = "¿Cuál es el proceso por el cual las plantas convierten la luz solar en energía química?",
                Answer = 0,
                Options = new List<string> { "Fotosíntesis", "Respiración", "Evaporación", "Descomposición" }
            }, // 19
            new Quiz()
            {
                Question = "¿Cuál es la unidad básica de la herencia genética?",
                Answer = 2,
                Options = new List<string> { "Proteína", "Ácido ribonucleico (ARN)", "Gen", "Célula" }
            }, // 20
            new Quiz()
            {
                Question = "¿Cuál es la fórmula química del agua?",
                Answer = 0,
                Options = new List<string> { "H2O", "CO2", "CH4", "NaCl" }
            }, // 21
            new Quiz()
            {
                Question = "¿Cuál es el proceso por el cual la sangre circula por el cuerpo humano?",
                Answer = 2,
                Options = new List<string> { "Respiración", "Digestión", "Circulación", "Excreción" }
            }, // 22
            new Quiz()
            {
                Question = "¿Qué famoso científico formuló la teoría de la relatividad?",
                Answer = 2,
                Options = new List<string> { "Isaac Newton", "Charles Darwin", "Albert Einstein", "Galileo Galilei" }
            }, // 23
            new Quiz()
            {
                Question = "¿Cuál es la capa exterior sólida de la Tierra?",
                Answer = 2,
                Options = new List<string> { "Núcleo", "Manto", "Corteza", "Magma" }
            }, // 24
            new Quiz()
            {
                Question = "¿Qué gas es esencial para la fotosíntesis y es liberado por los seres humanos al exhalar?",
                Answer = 1,
                Options = new List<string> { "Oxígeno", "Dióxido de carbono", "Nitrógeno", "Hidrógeno" }
            }, // 25
            new Quiz()
            {
                Question = "¿Cuál es la fuerza que atrae dos objetos con masa entre sí?",
                Answer = 2,
                Options = new List<string> { "Fuerza electromagnética", "Fuerza nuclear fuerte", "Fuerza gravitatoria", "Fuerza de fricción" }
            } // 26
        };
    }

    private void DisplayQuestion()
    {
        var quiz = _questions[_currentQuestionIndex];

        Console.ForegroundColor = ConsoleColor.DarkMagenta;
        Console.WriteLine($"Acertijo: {quiz.Question}");
        char option = 'A';

        Console.ForegroundColor = ConsoleColor.Gray;
        foreach (var choice in quiz.Options)
        {
            Console.WriteLine($"Opción {option}: {choice}");
            option++;
        }

        Console.ForegroundColor = ConsoleColor.DarkGreen;
        Console.Write("Tu respuesta: ");
    }
}

public class Quiz
{
    public int Answer { get; set; }
    public string Question { get; set; } = string.Empty;
    public List<string> Options { get; set; } = new();
}

public class Room
{
    public bool IsActive { get; set; }
    public string Content { get; set; }
    public Room(string content, bool isActive = false)
    {
        IsActive = isActive;
        Content = content;
    }
    public override string ToString()
    {
        return IsActive ? Content : "🔲";
    }
}

public class Board
{
    public int Side { get; set; }
    public Room[] Matrix { get; set; }

    public Board(int side)
    {
        Side = side;
        Matrix = new Room[Side * Side];
        InitializeBoard();
    }

    private void InitializeBoard()
    {
        for (int i = 0; i < Side * Side; i++)
        {
            var room = new Room("❓");
            Matrix[i] = room;
        }
    }
}

#region Tablero de juego
public class GameBoard
{
    private Board _board;
    private int _currentPosition;
    private int _side;

    public int CurrentPosition { get => _currentPosition; set => _currentPosition = value; }

    public GameBoard(Board board)
    {
        _board = board;
        _side = board.Side;
        _currentPosition = InitializeInitialDoor();
        AssignRoom();
    }

    private void AssignRoom()
    {
        Random random = new();
        int index = random.Next(_side * _side);

        // asginamos el dulce
        while (_board.Matrix[index].Content != "❓")
        {
            index = random.Next(_side * _side);
        }
        _board.Matrix[index] = new Room("🍭");

        // Obtenemos la cantidad de fantasma que apareceran
        // considerandose que minimanete haya 2 fantasmas
        int countGhost = random.Next(2, _side * _side - 4); 

        // Asignamos los fantasmas
        index = random.Next(_side * _side);
        for (int i = 0; i < countGhost; i++)
        {
            while (_board.Matrix[index].Content != "❓")
            {
                index = random.Next(_side * _side);
            }
            _board.Matrix[index] = new Room("👻");
        }
    }
    private int InitializeInitialDoor()
    {
        Random random = new();
        int index = random.Next(_side * _side);

        // Asigna solo a los extremos
        while (!(index <= _side || index >= (_side * (_side - 1)) || index % _side == 0 || (index + 1) % _side == 0))
        {
            index = random.Next(_side * _side);
        }

        _board.Matrix[index] = new Room("🚪", true);
        return index;
    }
    
    public void Run()
    {
        DisplayBoard();
        string input = Input.ReadInput(GetMessage());
        while (!ValidateMove(input))
        {
            Console.WriteLine("Moviemiento no valido");
            input = Input.ReadInput(GetMessage());
        }
        MovePlayer(input);
    }

    public int GetNumberOfQuestions()
    {
        if (_board.Matrix[_currentPosition].Content == "❓") return 1;
        if (_board.Matrix[_currentPosition].Content == "👻") return 2;
        if (_board.Matrix[_currentPosition].Content == "🍭") return 3;
        return 0;
    }
    private string GetMessage()
    {
        string ms = string.Empty;
        ms += ValidateMove("N") ? "N ↑ - " : "";
        ms += ValidateMove("S") ? "S ↓ - " : "";
        ms += ValidateMove("E") ? "E → - " : "";
        ms += ValidateMove("W") ? "W ← - " : "";
        return ms;
    }
    private bool ValidateMove(string move)
    {
        if (move == "E" && (_currentPosition + 1) % _side == 0)     return false;
        if (move == "W" && _currentPosition % _side == 0)           return false;
        if (move == "N" &&  _currentPosition < _side)               return false;
        if (move == "S" && _currentPosition >= _side * (_side - 1)) return false;

        return true;
    }
    private void MovePlayer(string move)
    {
        _currentPosition += move == "E" ? 1 : 0;
        _currentPosition -= move == "W" ? 1 : 0;
        _currentPosition -= move == "N" ? _side : 0;
        _currentPosition += move == "S" ? _side : 0;
        _board.Matrix[_currentPosition].IsActive = true;
    }
    public void DisplayBoard()
    {
        int index, side = _board.Side;
        for (int i = 0; i < side; i++)
        {
            for (int j = 0; j < side; j++)
            {
                index = side * i + j;
                if (index == _currentPosition) Console.Write("🧛");
                else Console.Write("  ");
                
                if (index == _currentPosition) Console.Write(_board.Matrix[index]);
                else Console.Write(_board.Matrix[index]);
            }
            Console.WriteLine();
        }
    }
}
#endregion

public static class Input
{
    public static string ReadInput(string ms)
    {
        string inputKey;
        Console.WriteLine($"Donde quieres desplazarte {ms}\b\b  ");
        inputKey = Console.ReadLine().ToUpper();

        while (inputKey != "N" && inputKey != "S" && inputKey != "E" && inputKey != "W")
        {
            Console.WriteLine("Opcion Invalida");
            inputKey = Console.ReadLine().ToUpper();
        }
        return inputKey;
    }
}