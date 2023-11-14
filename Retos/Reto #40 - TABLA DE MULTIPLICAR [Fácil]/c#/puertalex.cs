using System;
class Reto40
{
    public static void Main (string[] args)
    {
        while (true)
        {
            try
            {
                int entrada;
                Console.WriteLine("Ingrese un número entero entre 1 y 10");
                entrada = Int16.Parse(Console.ReadLine());
                if (entrada >= 1 && entrada <= 10)
                {
                    Console.WriteLine(generaTabla(entrada));
                    break;            
                }
                else
                {
                    Console.WriteLine("Debe introducir un numero entero entre 1 y 10");
                }
            }
            catch
            {
                Console.WriteLine("Debe ingresar solo numeros enteros");
            }
        }
        
        string generaTabla(int numero)
        {
            string tabla = "";
            for(int i = 1; i <= 10; i++)
            {
                tabla += $"{numero} X {i} = {numero * i}\n";
            }
            return tabla;
        }
    }
}