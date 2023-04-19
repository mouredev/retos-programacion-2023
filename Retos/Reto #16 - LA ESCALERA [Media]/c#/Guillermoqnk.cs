/* Statement:
 * 
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */

namespace Reto16
{
    internal class Guillermoqnk
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to the stair drawer!!\n");

            Console.WriteLine("Enter the number of steps you want: ");

            var input = Console.ReadLine();

            int number = Convert.ToInt32(input);
            DrawStair(number);
        }

        private static void DrawStair(int steps)
        {
            if(steps == 0)
            {
                Console.WriteLine("__");
            }
            else
            {
                int initial = 0;
                int condition = 0;
                int increase = 0;
                int verticalPos = 5;
                bool symbol = true;
                

                if(steps > 0)
                {
                    initial = steps*2;
                    condition = 0;
                    increase = -2;
                }
                else if(steps < 0)
                {
                    initial = 0;
                    condition = steps*2;
                    increase = -2;
                }

                for(int i = initial; i != condition; i += increase)
                {
                    Console.SetCursorPosition(Math.Abs(i), verticalPos);

                    if(symbol)
                    {
                        Console.Write("_");
                        symbol = false;
                    }
                    else if(!symbol)
                    {
                        if(steps<0)
                            Console.Write("|_");
                        else
                            Console.Write("_|");
                    }

                    verticalPos +=1;
                }
                


            }
        }
    }
}