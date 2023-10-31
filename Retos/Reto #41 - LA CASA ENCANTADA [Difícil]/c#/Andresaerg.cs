// See https://aka.ms/new-console-template for more information
// SoundPlayer typewriter = new();
// string solutionDir = Directory.GetParent(Environment.CurrentDirectory).Parent.Parent.FullName;
// string soundFilePath = Path.Combine(solutionDir, "sound.wav");
// typewriter.SoundLocation = soundFilePath;
// typewriter.Load();
// typewriter.PlayLooping();
// Puedes agregar sonido con el anterior codigo y la lib System.Media.
// Yo usé la siguiente: https://www.youtube.com/watch?v=wkHL5AsSzF4

using Newtonsoft.Json;


var questions = await Get_Questions();

int posX = 0, posY = 0; //Inicio
Random selector = new Random();
int exitX = 3, exitY = selector.Next(0, 3); //Salida
bool can_play = true;

string[,] house_init = new string[4, 4]{
    { "(^_^)", "⬜", "⬜", "⬜"},
    { "⬜", "⬜", "⬜", "⬜"},
    { "⬜", "⬜", "⬜", "⬜"},
    { "⬜", "⬜", "⬜", "⬜"}
};

house_init[exitX, exitY] = "⬜";

void Draw()
{
    Console.Clear();
    Console.WriteLine("===========================================================================");
    Console.WriteLine("                         Reto #41 de MoureDev                              ");
    Console.WriteLine("===========================================================================");
    for (int x = 0; x < house_init.GetLength(0); x++)
    {
        Console.Write("\t\t\t");
        for (int y = 0; y < house_init.GetLength(1); y++)
        {
            Console.Write($"{house_init[x, y]}\t");
        }
        Console.WriteLine();
    }

    string north = posX != 0 ? "Norte " : "";
    string south = posX != 3 ? "Sur " : "";
    string east = posY != 3 ? "Este " : "";
    string west = posY != 0 ? "Oeste " : "";
    string category = questions.Count() > 0 ? questions[0].category!.ToUpper() : "";
    Console.WriteLine();
    Console.WriteLine($"Presiona las flechas para desplazarte por la pista. Recibirás preguntas de: {category}");
    Console.WriteLine($"Opciones disponibles: {north}{south}{east}{west}");
    Console.WriteLine();
}

void Ask(bool ghost)
{
    bool correctAnswer = false;
    int repeat = !ghost ? 1 : 2;
    if (repeat == 2) Console.WriteLine("Vaya! Encontraste un fantasma... o el te encontro a ti ~.~");

    while ((!correctAnswer && questions!.Count > 0) || repeat > 0)
    {
        Console.WriteLine();
        int index = selector.Next(0, questions.Count);
        var question = questions[index];
        string[] options = { question.answers!.answer_a!, question.answers.answer_b!,
            question.answers.answer_c!, question.answers.answer_d! };
        string[] opt_index = new string[] { "a) ", "b) ", "c) ", "d) " };

        Console.WriteLine($"{question.question}");

        for (int i = 0; i < options.Length; i++)
        {
            if (!string.IsNullOrEmpty(options[i]))
            {
                Console.WriteLine($"{opt_index[i]}{options[i]}");
            }
        }

        Console.WriteLine();
        Console.Write("Seleccione su respuesta: ");
        string userAnswer = Console.ReadLine()!.ToLower();

        switch (userAnswer)
        {
            case "a":
                correctAnswer = question.correct_answer == "answer_a";
                break;
            case "b":
                correctAnswer = question.correct_answer == "answer_b";
                break;
            case "c":
                correctAnswer = question.correct_answer == "answer_c";
                break;
            case "d":
                correctAnswer = question.correct_answer == "answer_d";
                break;
            default:
                Console.WriteLine("Lo siento mi rey, esa no es una opción válida. Vuelve a intentarlo");
                continue;
        }

        string message = correctAnswer ? "¡Respuesta correcta!\nPuedes seguir, crack" : $"Lo siento, esa no es la respuesta correcta.\n{question.feedback}";
        Console.WriteLine(message);
        Console.WriteLine();

        questions.RemoveAt(index);
        if (questions!.Count == 0)
        {
            Console.WriteLine("Lo siento mi bro, te has quedado sin oportunidades para continuar...");
            house_init[posX, posY] = "(x_x)";
            can_play = false;
            Draw();
            return;
        }
        repeat--;
    }
}

void Movement(string direction)
{
    // Guarda la posición actual antes de moverte
    int oldPosX = posX;
    int oldPosY = posY;

    switch (direction)
    {
        case "north":
            if (posX > 0) posX--;
            break;
        case "south":
            if (posX < house_init.GetLength(0) - 1) posX++;
            break;
        case "east":
            if (posY < house_init.GetLength(1) - 1) posY++;
            break;
        case "west":
            if (posY > 0) posY--;
            break;
    }
    // Marca la posición actual como visitada
    house_init[oldPosX, oldPosY] = "⬜";

    // Comprueba si llegaste a la salida
    bool finish = (posX == exitX) && (posY == exitY); ;
    if (finish)
    {
        house_init[posX, posY] = "(^o^)";
        Draw();
        Console.WriteLine("Felicidades! Has obtenido muchos dulces y chocolates ficticios o.O \nFeliz Halloween!");
        can_play = false;
        Console.WriteLine();
        return;
    }

    // Comprueba si te has movido a una nueva posición
    bool should_ask = house_init[posX, posY] == "⬜";

    // Posicion actual
    house_init[posX, posY] = "(^_^)";

    // Hay fantasmas?
    bool ghost = false;
    int ghosts_spawn = selector.Next(0, 100);
    if (ghosts_spawn >= 0 && ghosts_spawn <= 10)
    {
        ghost = true;
        house_init[posX, posY] = "(o_o)";
    }

    Draw();

    if (should_ask)
    {
        Ask(ghost);
    }
}

Draw();

while (can_play) // Bucle infinito hasta que el usuario cierre la consola
{
    var key = Console.ReadKey(true).Key; // El argumento 'true' oculta la tecla presionada
    switch (key)
    {
        case ConsoleKey.UpArrow:
            Movement("north");
            break;
        case ConsoleKey.DownArrow:
            Movement("south");
            break;
        case ConsoleKey.RightArrow:
            Movement("east");
            break;
        case ConsoleKey.LeftArrow:
            Movement("west");
            break;
    }
}

static async Task<List<Question>> Get_Questions()
{
    HttpClient client = new HttpClient();
    Random rand = new();
    string[] categories = { "html", "css", "javascript", "php", "sql", "csharp", "java", "cpp", "python" };
    int category_index = rand.Next(0, 8);
    client.DefaultRequestHeaders.Accept.Clear();
    client.DefaultRequestHeaders.Accept.Add(
        new System.Net.Http.Headers.MediaTypeWithQualityHeaderValue("application/json"));

    var request = client.GetAsync($"https://www.preguntapi.dev/api/categories/{categories[category_index]}?level=aleatorio&limit=20");

    var response = await request;
    var json = await response.Content.ReadAsStringAsync();
    var data = JsonConvert.DeserializeObject<List<Question>>(json);

    return data!;
}

public class Question
{
    public int id { get; set; }
    public string? category { get; set; }
    public string? level { get; set; }
    public string? question { get; set; }
    public Answer? answers { get; set; }
    public string? correct_answer { get; set; }
    public string? feedback { get; set; }
}

public class Answer
{
    public string? answer_a { get; set; }
    public string? answer_b { get; set; }
    public string? answer_c { get; set; }
    public string? answer_d { get; set; }
}
