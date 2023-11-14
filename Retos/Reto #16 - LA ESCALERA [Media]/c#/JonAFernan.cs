using System.Text;
namespace Reto16;

/*
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

class Program
{
    static void Main(string[] args)
    {
        DrawLadder(0); 
        DrawLadder(-4);
        DrawLadder(4);
    }

    static void DrawLadder(int numberOfSteps)
    {
        StringBuilder steps = new StringBuilder("_");

        if(numberOfSteps == 0) System.Console.WriteLine(steps.Insert(0,"_"));
        
        else if(numberOfSteps > 0)
        {
            
            for (int i = 0; i < numberOfSteps * 2; i++)
            {
                steps.Insert(i,' ');
            }

            System.Console.WriteLine(steps);
            steps.Insert(steps.Length,'|');

            while (steps.Length > 1)
            {
                if(steps[1] != '_') steps.Remove(0,2);
                else steps.Remove(0,1);
                System.Console.WriteLine(steps);
            }
        }

        else if(numberOfSteps < 0)
        {
            System.Console.WriteLine(steps);
            steps.Insert(0," |");
            System.Console.WriteLine(steps);

            if(numberOfSteps == -1) return;    
                
            else
            {
                while (steps.Length < numberOfSteps * -2 )
                {
                    
                    steps.Insert(0," ", 2);
                    System.Console.WriteLine(steps);
                }
            }
        }
    }
}
