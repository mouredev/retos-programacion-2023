using System;
using System.Collections.Generic;
using System.Linq;

namespace Reto39
{
    public class Program
    {
        public static void Main()
        {
            int maxNumber = 10;
            var triples = FindPythagoreanTriples(maxNumber);

            foreach (var triple in triples)
            {
                Console.WriteLine($"({triple.Item1}, {triple.Item2}, {triple.Item3})");
            }

            Console.ReadKey();
        }

        public static List<Tuple<int, int, int>> FindPythagoreanTriples(int maxNumber) =>
            (from a in Enumerable.Range(1, maxNumber)
                from b in Enumerable.Range(a, maxNumber - a + 1)
                let c = Math.Sqrt(a * a + b * b)
                where c <= maxNumber && c% 1 == 0
                select Tuple.Create(a, b, (int)c)).ToList();
    }

}