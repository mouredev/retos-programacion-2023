namespace Reto22;

/*
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
 */
class Program
{
    static void Main(string[] args)
    {
        DrawSpiral(12);
        /*
            ═══════════╗
            ╔═════════╗║
            ║╔═══════╗║║
            ║║╔═════╗║║║
            ║║║╔═══╗║║║║
            ║║║║╔═╗║║║║║
            ║║║║║╚╝║║║║║
            ║║║║╚══╝║║║║
            ║║║╚════╝║║║
            ║║╚══════╝║║
            ║╚════════╝║
            ╚══════════╝
        */ 
        
    }


    static void DrawSpiral(int size)
    {
        bool horizontal = true;
        int spiralLength = size-1;

        if(size <=2) System.Console.WriteLine("Insert a value greater than two");

        else
        {

            for(int i = 0 ; i < size ; i++)
            {
                //System.Console.Write(i + " ");
                for (int j = 0; j < size; j++)
                {
                    if( i<=spiralLength/2 && j==spiralLength-i)
                    {
                        System.Console.Write('\u2557'); //╗ 
                        horizontal = false;
                    } 
                    else if (i>spiralLength/2 && j== i) 
                    {
                        System.Console.Write('\u255D'); // ╝
                        horizontal = false;
                    }
                    else if (i<=spiralLength/2 && i !=0 && j==i-1) 
                    {
                        System.Console.Write('\u2554'); //╔
                        horizontal=true;
                    }
                    else if (i>spiralLength/2 && j==spiralLength-i)
                    {
                        System.Console.Write('\u255A'); //╚
                        horizontal = true; 
                    }
                    else if(horizontal) Console.Write('\u2550'); //═
                    else Console.Write('\u2551'); // ║
                }

                System.Console.WriteLine();
            }
        }
    }
}
