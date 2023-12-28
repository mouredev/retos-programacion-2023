/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

using System;
using System.Text;

namespace GeneradorContraseña
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Password password = new Password();
            password.Mayusculas = "no";
            password.Simbolos = "yes";
            password.Numeros = "yes";
            password.generarPass();
        }
    }

    public class Password
    {
        private string mayusculas;
        private string numeros;
        private string simbolos;
        private string letras = "0";

        public string Mayusculas { get { return mayusculas; } set { mayusculas = value == "yes" ? "1" : String.Empty; } }
        public string Numeros { get { return numeros; } set { numeros = value == "yes" ? "2" : String.Empty; } }
        public string Simbolos { get { return simbolos; } set { simbolos = value == "yes" ? "3" : String.Empty; } }

        public void generarPass()
        {
            string pass = string.Empty;

            int indice = 0;

            string config = letras + mayusculas + numeros + simbolos;

            Random random = new Random();
            int longitud = random.Next(8,16 + 1);
            StringBuilder sbLetras = new StringBuilder("abcdefghijklmnopqr");
            StringBuilder sbNumeros = new StringBuilder("0123456789");
            StringBuilder sbSignos = new StringBuilder("!#$%&/()=?¡+*{}[]-_|°¬,.;:^");
            StringBuilder sbConfig = new StringBuilder(config);
            
            for (int i = 1; i <= longitud; i++)
            {
                int indiceConfig = random.Next(sbConfig.Length);

                switch (sbConfig[indiceConfig])
                {
                    case '0':
                        indice = random.Next(sbLetras.Length);
                        pass += sbLetras[indice];
                        break;
                    case '1':
                        indice = random.Next(sbLetras.Length);
                        pass += sbLetras[indice].ToString().ToUpper();
                        break;
                    case '2':
                        indice = random.Next(sbNumeros.Length);
                        pass += sbNumeros[indice];
                        break;
                    case '3':
                        indice = random.Next(sbSignos.Length);
                        pass += sbSignos[indice];
                        break;
                }   
            }
            Console.WriteLine("La contraseña es: "+pass);
        }
    }
}
