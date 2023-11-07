using System;
using System.Collections.Generic;
using System.Linq;

namespace Reto38
{
    public class Program
    {
        public static void Main()
        {
            List<int> numbers = new List<int> { 1, 5, 3, 2 };
            int target = 6;
            var combinations = FindCombinations(numbers, target);

            foreach (var combination in combinations)
            {
                Console.WriteLine(string.Join(", ", combination));
            }

            Console.ReadKey();
        }

        public static List<List<int>> FindCombinations(List<int> numbers, int target)
        {
            List<List<int>> result = new List<List<int>>();

            void Helper(List<int> currentNumbers, int currentSum, List<int> currentCombination)
            {
                if (currentSum == target)
                {
                    result.Add(new List<int>(currentCombination));
                    return;
                }

                if (!currentNumbers.Any() || currentSum > target)
                    return;

                int currentNum = currentNumbers.First();

                Helper(currentNumbers.Skip(1).ToList(), currentSum, currentCombination);

                currentCombination.Add(currentNum);
                Helper(currentNumbers.Skip(1).ToList(), currentSum + currentNum, currentCombination);
                currentCombination.RemoveAt(currentCombination.Count - 1);
            }

            Helper(numbers, 0, new List<int>());

            return result;
        }
    }
}