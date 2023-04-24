namespace Reto2_PartidoTenis
{
    internal class Program
    {
        static void Main(string[] args)
        {
            StartMatch(new string[]{"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"});
        }

        static void StartMatch(string[] sequency)
        {
            //Validaciones
            var set = new HashSet<string>(sequency);
            
            if (set.Count() != 2) return;
            if (!set.Contains("P1") && !set.Contains("P2")) return;

            int[] scores = new int[2] { 0, 0 };
            string[] points = new string[] { "Love", "15", "30", "40"};
            
            //Iteracion
            var enumerator = sequency.GetEnumerator();
            while (enumerator.MoveNext())
            {
                var player = Convert.ToString(enumerator.Current);
                if(player is null) continue;

                int currentIndex = player == "P1" ? 0 : 1;
                scores[currentIndex]++;

                if (scores[0] == 3 && scores[1] == 3)
                    Console.WriteLine("Deuce");

                else if ((scores[0] == 4 && scores[0] > scores[1]) || (scores[1] == 4 && scores[1] > scores[0]))
                    Console.WriteLine($"Ventaja P{currentIndex+1}");

                else if ((scores[0] == 5 && scores[0] - scores[1] == 2) || (scores[1] == 5 && scores[1] - scores[0] == 2))
                    Console.WriteLine($"Ha ganado el P{currentIndex + 1}");

                else
                    Console.WriteLine(points[scores[0]] + " - " + points[scores[1]]);
            }
        }
    }
}