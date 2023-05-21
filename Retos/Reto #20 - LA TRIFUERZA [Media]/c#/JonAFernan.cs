namespace Reto20;

/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
 */


class Program
{
    static void Main(string[] args)
    {
        TriforceDraw(5);
    }


    static void TriforceDraw (int n)
    {
        List<int> pyramidStepsNum = new List<int>();

        char asterisk = '*';
        char blankSpace = ' ';
        int counter = 0;

        while (n!= 0)
        {   
            pyramidStepsNum.Add(n*2-1);
            n= n- 1;
        }

        pyramidStepsNum.Reverse();


        for ( int i = 0; i< pyramidStepsNum.Count * 2 ; i++)
        {
            string f;

            if( i < pyramidStepsNum.Count)
            {
                f = new String(blankSpace,pyramidStepsNum[(pyramidStepsNum.Count - 1)] -i) + new String(asterisk,pyramidStepsNum[i]);
            }

            else
            {
                f = new String(blankSpace, pyramidStepsNum[(pyramidStepsNum.Count - 1)]-i) + new String(asterisk,pyramidStepsNum[counter]) 
                + new String(blankSpace,pyramidStepsNum[(pyramidStepsNum.Count - 1)-counter]) + new String(asterisk,pyramidStepsNum[counter]); 
                
                counter ++;
            }

            Console.WriteLine(f);
        }

    }
}
