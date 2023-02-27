using System;

class miguelex
{
    public static long seed = DateTime.Now.Ticks / TimeSpan.TicksPerMillisecond;

    static void Main(string[] args)
    {
        long a = DateTime.Now.Ticks / TimeSpan.TicksPerMillisecond;
        long m = (DateTime.Now.Ticks / TimeSpan.TicksPerMillisecond) * 1000;

        Console.WriteLine("¿Cuantos numeros quieres generar?: ");
        int contador = Convert.ToInt32(Console.ReadLine());

        for (int i = 0; i < contador; i++)
        {
            Console.WriteLine("Numero {0}: {1}", i + 1, RandomNumber(a, m));
            System.Threading.Thread.Sleep(3000);
        }

    }

    private static int RandomNumber(long a, long m)
    {
        long q = a / m;
        long r = a % m;

        seed = a * (seed % q) - r * (seed / q);


        if (seed <= 0)
        {
            seed += m;
        }

        return Convert.ToInt32(Math.Abs(seed) % 100);
    }

}