using System;

namespace AleatoryNumber
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int result = GetAleatoryByMillisecond();
            Console.WriteLine($"Result: {result}");
            Console.WriteLine($"Result: {GetAleatoryByDate()}");
            Console.ReadLine();
        }

        /// <summary>
        /// get aleatory by current millisecond
        /// </summary>
        /// <returns></returns>
        public static int GetAleatoryByMillisecond()
        {
            return DateTime.UtcNow.Millisecond / 10;
        }

        /// <summary>
        ///  Get aleatory by currendt datetime
        /// </summary>
        /// <returns></returns>
        public static int GetAleatoryByDate()
        {
            var x = DateTime.Now;
            var result = x.Year + x.Month + x.Day + x.Hour + x.Minute + x.Second + x.Millisecond;
            return result / 100;
        }
    }
}
