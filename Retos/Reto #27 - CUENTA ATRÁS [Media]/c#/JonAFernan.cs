namespace reto27;

/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */
class Program
{
    static void Main(string[] args)
    {
        CountdownAsync(15,1);
        CountdownAsync(4,2);

        Console.ReadKey();
    }

    static async void CountdownAsync(int countNum, int seconds)
    {
        
        if (countNum <=0) 
        {
            System.Console.WriteLine("Error. Insert a non-negative number that is greater than zero");
            return;
        }
        if (seconds < 0) 
        {
            System.Console.WriteLine("Error. Insert a non-negative number");
            return;
        }
        for (int i = countNum ; i >= 0; i--)
        {
            await Task.Delay(seconds * 1000);
            System.Console.WriteLine(i);
        }
    }
}
