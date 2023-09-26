namespace primofibonaccipar;
    /*
    * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
    * Ejemplos:
    * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
    * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
    */
    class Program
    {
        static void Main(string[] args)
        {

            string answer;
            int num;
            Console.WriteLine("*** Comprobador de numero primo, fibonacci y par ***");            
            Console.WriteLine("Ponga el numero positivo mayor de 2 para comprobar");
            num = Int32.Parse(Console.ReadLine());
            if (num < 1)
            {
                Console.WriteLine("Numero erroneo");
                return;
            }
            answer = comprobar(num);
            Console.WriteLine("Su numero " + num + ": " + answer);
        }

        static string comprobar(int num)
        {
            string respuesta="";
            int numcom = num;
            int j = 1, y = 1, z;
            bool fibonacci = false;
            for (int i = 2; i < numcom; i++)
            {
                if ((numcom % i) == 0)
                {
                    // No es primo 
                    respuesta = "no es primo, ";
                    i = numcom;
                }
                else
                {
                    respuesta = "es primo, ";
                    i= numcom;
                }
            }
            for (int i = 2; fibonacci==false; i = j + y)
            {
                j = y;
                y = i;
                Console.WriteLine("prueba fibonacci");
                if (numcom == i)
                {
                    // es fibonacci 
                    respuesta += "es fibonacci, ";
                    fibonacci = true;
                }
                else if ( numcom < i)
                {
                    respuesta += "no es fibonacci, ";
                    fibonacci = true;
                }
            }
            if ((numcom % 2) == 0)
            {
                // es par ;)
                respuesta += "es par.";
            }
            else
            {
                respuesta += "no es par.";
            }
            return respuesta;
        }
    }