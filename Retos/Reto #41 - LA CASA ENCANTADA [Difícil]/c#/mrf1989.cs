// Author: mrf1989/mruano89

bool firstMovement = true;
string userPrompt = "";
const int GAMEBOARD_ROWS = 4;
const int GAMEBOARD_COLS = 4;
const int GHOST_PROBABILITY = 10;

GameConfiguration configuration = new(
    GAMEBOARD_ROWS,
    GAMEBOARD_COLS,
    GHOST_PROBABILITY);

BoxRoom[,] gameboard = CreateGameboard(configuration);
var quizzes = GenerateQuizzes(20);

Console.WriteLine("Welcome to the Haunted House! Muahahaha!".ToUpper());
Console.WriteLine("Do you know what you need to know to find the hidden sweets?");
Console.WriteLine("Type 'exit' to finish the game.");
Console.WriteLine();

do
{
    configuration.playerCoords = UpdatePlayerCoords(configuration.playerCoords,
        userPrompt);
    
    var movements = GetAvailableMovesFrom(
        configuration.playerCoords[0],
        configuration.playerCoords[1]);

    var playerCoords = configuration.playerCoords;

    PrintGameboard(gameboard, configuration);
    
    Console.WriteLine($"Your current position is: " +
        $"({playerCoords[0]}, {playerCoords[1]})");

    if (!firstMovement)
    {
        var room = gameboard[playerCoords[0], playerCoords[1]];
        if (room.Equals(BoxRoom.Sweets))
        {
            Console.WriteLine("You have found the Haunted House sweets!!");
            break;
        }
        AnswerQuizz(quizzes, room);
    }
    else
    {
        firstMovement = false;
    }

    Console.Write("Where do you want to move in the Haunted Mansion? (Type: ");
    foreach (var movement in movements)
    {
        Console.Write($"'{movement}', ");
    }
    Console.Write("\b\b)\n");
    
    userPrompt = PlayerMovement(movements);
    
    Console.Clear();

} while (userPrompt != "exit");

string GetPlayerMovement(List<Movement> availableMoves)
{
    var playerMovement = Console.ReadLine().Trim();

    _ = Enum.TryParse(playerMovement, out Movement selectedMovement);
    var checkValidMovement = availableMoves
        .Exists(movement => movement == selectedMovement);

    if (!checkValidMovement && playerMovement != "exit")
    {
        throw new Exception("The movement is not valid. Try again!");
    }

    return playerMovement;
}

string PlayerMovement(List<Movement> availableMoves)
{
    string playerMovement = "";
    
    do
    {
        try
        {
            playerMovement = GetPlayerMovement(availableMoves);
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
            //PlayerMovement(availableMoves);
        }
    } while (playerMovement.Length == 0);
    
    return playerMovement;
}

// Methods

Tuple<string, int>[] GenerateQuizzes(int quizzSize)
{
    Tuple<string, int>[] quizzes = new Tuple<string, int>[quizzSize];

    for (int i = 0; i < quizzSize; i++)
    {
        int factorA = new Random().Next(0, 10);
        int factorB = new Random().Next(0, 10);

        quizzes[i] = new($"{factorA} x {factorB}", factorA * factorB);
    }

    return quizzes;
}

void AnswerQuizz(Tuple<string, int>[] quizzes, BoxRoom room)
{
    int successfulQuizzes = 0;
    int numberOfQuizzes = 1;
    if (room.Equals(BoxRoom.Ghost))
    {
        numberOfQuizzes = 2;
        Console.WriteLine("A terrible ghost appeared!!\n" +
            "You will have to pass two tests to escape...");
    }

    do
    {
        var quizz = GetQuizz(quizzes);
        Console.WriteLine($"Product of {quizz.Item1}:");

        try
        {
            int quizzResponse = Convert.ToInt32(Console.ReadLine());
            if (quizzResponse == quizz.Item2)
            {
                successfulQuizzes++;
                Console.WriteLine("Good!");
            }
            else
            {
                Console.WriteLine("You are wrong. Try again!");
            }
        }
        catch
        {
            Console.WriteLine("You are wrong. You must entry a number!");
        }

    } while (successfulQuizzes != numberOfQuizzes);
    Console.WriteLine("Nice! Keep looking for the sweets!");
}

Tuple<string, int> GetQuizz(Tuple<string, int>[] quizzes)
{
    int quizzRandomPosition = new Random().Next(0, quizzes.Length);
    return quizzes[quizzRandomPosition];
}

BoxRoom[,] CreateGameboard(GameConfiguration config)
{
    BoxRoom[,] gameboard = new BoxRoom[config.rows, config.cols];

    for (int i = 0; i < config.rows; i++)
    {
        for (int j = 0; j < config.cols; j++)
        {
            int randomInteger = new Random().Next(0, 100);

            if (randomInteger <= config.ghostProbability)
            {
                gameboard[i, j] = BoxRoom.Ghost;
            }
            else
            {
                gameboard[i, j] = BoxRoom.Empty;
            }
        }
    }

    gameboard[config.doorCoords[0], config.doorCoords[1]] = BoxRoom.Door;
    gameboard[config.sweetsCoords[0], config.sweetsCoords[1]] = BoxRoom.Sweets;

    return gameboard;
}

List<Movement> GetAvailableMovesFrom(int row, int col)
{
    List<Movement> movements = new();

    if (row - 1 >= 0)
    {
        movements.Add(Movement.North);
    }

    if (row + 1 < GAMEBOARD_ROWS)
    {
        movements.Add(Movement.South);
    }

    if (col + 1 < GAMEBOARD_COLS)
    {
        movements.Add(Movement.East);
    }

    if (col - 1 >= 0)
    {
        movements.Add(Movement.West);
    }

    return movements;
}

void PrintGameboard(BoxRoom[,] gameboard, GameConfiguration config)
{
    int[] coords = config.playerCoords;
    for (int i = 0; i < config.rows; i++)
    {
        for (int j = 0; j < config.cols; j++)
        {
            bool playerInCurrentRoom = coords[0] == i && coords[1] == j;
            switch (gameboard[i, j])
            {
                case BoxRoom.Door:
                    Console.Write("🚪");
                    break;
                case BoxRoom.Ghost:
                    if (playerInCurrentRoom)
                    {
                        Console.Write("👻");
                    }
                    else
                    {
                        Console.Write("⬜️");
                    }
                    break;
                case BoxRoom.Sweets:
                    if (playerInCurrentRoom)
                    {
                        Console.Write("🍭");
                    }
                    else
                    {
                        Console.Write("⬜️");
                    }
                    break;
                case BoxRoom.Empty:
                    if (playerInCurrentRoom)
                    {
                        Console.Write("❓");
                    }
                    else
                    {
                        Console.Write("⬜️");
                    }
                    break;
            }
        }
        Console.Write("\n");
    }
}

int[] UpdatePlayerCoords(int[] playerCoords, string? userPrompt)
{
    int[] newCoords = playerCoords;

    switch (userPrompt.Trim().ToLower())
    {
        case "north":
            newCoords[0]--;
            break;
        case "south":
            newCoords[0]++;
            break;
        case "east":
            newCoords[1]++;
            break;
        case "west":
            newCoords[1]--;
            break;
        default:
            break;
    }

    return newCoords;
}

// Objects

enum BoxRoom
{
    Door,
    Empty,
    Ghost,
    Sweets
}

enum Movement
{
    North,
    South,
    East,
    West
}

public struct GameConfiguration
{
    public GameConfiguration(int rows, int cols, int ghostProbability)
    {
        this.rows = rows;
        this.cols = cols;
        this.ghostProbability = ghostProbability;
        this.doorCoords = GenerateDoorCoords();
        sweetsCoords = GenerateSweetsCoords();
        playerCoords = doorCoords;
    }

    private int[] GenerateDoorCoords()
    {
        int[] coords = new int[] {
            new Random().Next(0, rows - 1),
            new Random().Next(0, cols - 1)
        };

        return coords;
    }

    private int[] GenerateSweetsCoords()
    {
        int[] coords;

        do
        {
            coords = new int[] {
                new Random().Next(0, rows - 1),
                new Random().Next(0, cols - 1)
            };
        } while (doorCoords[0] == coords[0] && doorCoords[1] == coords[1]);
        
        return coords;
    }

    public int rows { get; init; }
    public int cols { get; init; }
    public int ghostProbability { get; init; }
    public int[] doorCoords { get; init; }
    public int[] sweetsCoords { get; init; }
    public int[] playerCoords { get; set; }
}