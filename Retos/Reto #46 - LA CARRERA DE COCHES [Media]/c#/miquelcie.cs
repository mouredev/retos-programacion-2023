
/*
 * Crea un programa que simule la competición de dos coches en una pista.
 * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
 * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
 * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
 * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
 *   🏁____🌲_____🚙
 *   🏁_🌲____🌲___🚗
 * 
 * El juego se desarrolla por turnos de forma automática, y cada segundo
 * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
 * uno de ellos (o los dos a la vez) llega a la meta.
 * - Acciones:
 *   - Avanzar entre 1 a 3 posiciones hacia la meta.
 *   - Si al avanzar, el coche finaliza en la posición de un árbol,
 *     se muestra 💥 y no avanza durante un turno.
 *   - Cada turno se imprimen las pistas y sus elementos.
 *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
 *   
 */

using System.Timers;
using Timer = System.Timers.Timer;

public class Program
{
    public static void Main(string[] args)
    {
 
        Carrera carrera = new Carrera();

        carrera.Initialize();
    }
}
public class Carrera
{
    private List<string> pista1;
    private List<string> pista2;
    private int carOnePosition;
    private int carTwoPosition;
    private bool turnoCarOne = true;
    private bool turnoCarTwo = true;

    private int positionTreeTemp1;
    private int positionTreeTemp2;


    internal void Initialize()
    {
        Console.Write("Introduzca longitud de la pista: ");

        string longitud = Console.ReadLine();

        int lognitudPista = 0;

        if (!int.TryParse(longitud, out lognitudPista) || lognitudPista<10)
        {
            throw new ArgumentOutOfRangeException("La longitud no es un número mayor de 10");
        }

        Console.Write("Introduzca número de árboles en la pista: ");

        string numTree = Console.ReadLine();

        int countTrees = 0;

        if (!int.TryParse(numTree, out countTrees) || countTrees < 1)
        {
            throw new ArgumentOutOfRangeException("El nº máximo de árboles debe se un numero mayor de 1");
        }

        carOnePosition = lognitudPista - 1;
        carTwoPosition = lognitudPista - 1;

        pista1 = CreatePistaRamdon(lognitudPista, countTrees);
        pista2 = CreatePistaRamdon(lognitudPista, countTrees);

        while (true)
        {
            DrawRace();

            if (IsRaceFinish()) {
                string ganador = GetWinner();
                Console.WriteLine($"El ganador es: {ganador}");
                break;
            }
            MoveCarOne();
            MoveCarTwo();
            
            Thread.Sleep(1000); 
        }
        Console.Write("Presione enter para salir");
        Console.ReadLine();

    }

    private void MoveCarOne()
    {
        if (!turnoCarOne)
        {
            turnoCarOne=true;
            return;

        }
        int movesCarOne = new Random().Next(1, 4);
        pista1[carOnePosition] = carOnePosition == positionTreeTemp1 ? "T" : "_";
        carOnePosition -= movesCarOne;
        carOnePosition = carOnePosition < 0 ? 0 : carOnePosition;
        if (pista1[carOnePosition] == "T")
        {
            positionTreeTemp1 = carOnePosition;
            pista1[carOnePosition] = pista1[carOnePosition] == "T"?"X":"C";
            turnoCarOne = false;
        }
        else
        {            
            pista1[carOnePosition] = "C";
        }
    }
    private void MoveCarTwo()
    {
        if (!turnoCarTwo)
        {
            turnoCarTwo = true;
            return;

        }
        int movesCarTwo = new Random().Next(1, 4);
        pista2[carTwoPosition] = carTwoPosition == positionTreeTemp2? "T" : "_";
        carTwoPosition -= movesCarTwo;
        carTwoPosition = carTwoPosition < 0 ? 0 : carTwoPosition;

        if (pista2[carTwoPosition] == "T")
        {
            positionTreeTemp2 = carTwoPosition;
            pista2[carTwoPosition] = pista2[carTwoPosition] == "T" ? "X" : "C";
            turnoCarTwo = false;
        }
        else
        {
            pista2[carTwoPosition] = "C";
        }

    }

    private void DrawRace()
    {
        string pista1String = string.Join("", pista1);
        string pista2String = string.Join("", pista2);
        Console.WriteLine($"{pista1String}\n{pista2String}");
    }

    private string GetWinner()
    {
        if (pista1[0] == "C"  && pista2[0] == "C")
            return "Empate";

        if (pista1[0] == "C")
            return "Coche 1";

        if (pista2[0] == "C")
            return "Coche 2";
        return string.Empty;
    }

    private bool IsRaceFinish()
    {
        return pista1[0]=="C" || pista2[0]=="C";
    }

    private List<string> CreatePistaRamdon(int longotidPista, int maxTrees) {

        List<string> pista = new List<string>() { "M" };
        string[] rango = Enumerable.Repeat("_", longotidPista-2).ToArray();

        int countTrees = new Random().Next(1, maxTrees+1);
        int countCurrentTrees = 0;
        while (countCurrentTrees < countTrees)
        {
            int positionTree = new Random().Next(1, longotidPista - 2);
            if (rango[positionTree] != "T")
            {
                rango[positionTree] = "T";
                countCurrentTrees++;
            }
            
        }

        pista.AddRange(rango);
        pista.Add("C");
        return pista;
    }
}