namespace reto21;

/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */
class Program
{
    static void Main(string[] args)
    {
        PrimoPar(14);
        // (3, 5), (5, 7), (11, 13)
        PrimoPar(100);
        // (3,5), (5,7), (11,13), (17,19), (29,31), (41,43), (59,61), (71,73)
    }

    static void PrimoPar(int number)
    {
        List<int> listPrimos = new List<int>();
        bool firstComma = true;
        
        for (int i = 2; i <= number; i++)
        {
            bool isPrimo = true;
         
            for (int j = 2 ; j < i ; j++)
                
                {
                    if(i%j == 0) 
                    {
                        isPrimo = false;
                        break;
                    }
                }  

            if(isPrimo == true) 
                {
                    listPrimos.Add(i);
                    
                    if(i != 2 && listPrimos[listPrimos.Count-1] - listPrimos[listPrimos.Count-2] == 2)
                    {
                        System.Console.Write(firstComma ? "" : ", ");
                        System.Console.Write($"({listPrimos[listPrimos.Count-2]},{listPrimos[listPrimos.Count-1]})");
                        firstComma = false;
                    }
                }

        }
    }
}
