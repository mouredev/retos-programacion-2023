using System;

namespace GeneradorDePassword
{
    class Program
    {
        static void Main(string[] args)
        {
            string minusculas = "abcdefghijklmnopqrstuvwxyz";
            string mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            string numeros = "0123456789";
            string especiales = "#$%&/()=?";
            string todas = mayusculas + minusculas + numeros + especiales;
            string opciones = minusculas;
            string password = "";
            Random aleatorio = new Random();

            Console.WriteLine("Elige la longitud de tu password entre 8 y 16 carácteres");
            string cant = Console.ReadLine();

            int cantidad = int.Parse(cant);

            Console.WriteLine("¿Quieres que tenga letras minúsculas, mayúsculas, números y carácteres especiales? S/N");
            string r0 = Console.ReadLine();

            if (r0 == "S")
            {
                opciones = todas;
            }
            else
            {
                Console.WriteLine("¿Quieres que tenga letras mayúsculas? S/N");
                string r1 = Console.ReadLine();

                if (r1 == "S")
                {
                    opciones = minusculas + mayusculas;
                }

                Console.WriteLine("¿Quieres que tenga números? S/N");
                string r2 = Console.ReadLine();

                if (r2 == "S")
                {
                    opciones = opciones + numeros;
                }

                Console.WriteLine("¿Quieres que tenga carácteres especiales? S/N");
                string r3 = Console.ReadLine();

                if (r3 == "S")
                {
                    opciones = opciones + especiales;
                }

            }
            // generar un password
            for (int i = 0; i < cantidad; i++)
            {
                int x = aleatorio.Next(opciones.Length);
                password = password + opciones[x];
            }

            Console.WriteLine("El password es: " + password);
            Console.Read();   
        }
    }
}