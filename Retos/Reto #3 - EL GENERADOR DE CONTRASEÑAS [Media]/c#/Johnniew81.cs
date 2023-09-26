namespace Generador_Claves
{
    /*
     * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
     * Podrás configurar generar contraseñas con los siguientes parámetros:
     * - Longitud: Entre 8 y 16.
     * - Con o sin letras mayúsculas.
     * - Con o sin números.
     * - Con o sin símbolos.
     * (Pudiendo combinar todos estos parámetros entre ellos)
     */
    class Program
    {
        static void Main(string[] args)
        {

            string answer, password;
            int length;
            bool capital, number, symbol;
            Console.WriteLine("*** Creador de contraseñas automaticas ***");
            Console.WriteLine("- Opciones");
            Console.WriteLine("1- Longitud entre 8 y 16 caracteres");
            length = Int32.Parse(Console.ReadLine());
            if (length > 8 || length < 16)
            {
                Console.WriteLine("Numero erroneo");
                return;
            }
            Console.WriteLine("2- Con o sin letras mayúsculas (s/n)");
            capital = respuestas(Console.ReadLine());
            Console.WriteLine("3- Con o sin número (s/n)");
            number = respuestas(Console.ReadLine());
            Console.WriteLine("4- Con o sin símbolos (s/n)");
            symbol = respuestas(Console.ReadLine());
            password= password_f(length, capital, number, symbol);
            Console.WriteLine("Su clave segura es: " + password);
        }
        static bool respuestas(string respuesta)
        {
            string answer = respuesta;
            bool result = false;
            answer = answer.ToLower();
            if (answer == "y" || answer == "s") { result = true; }
            return result;
        }
        static string password_f(int length, bool capital, bool number, bool symbol)
        {
            List<string> dataa = new List<string>() { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" };
            List<string> dataA = new List<string>() { "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };
            List<string> numberList = new List<string>() { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
            List<string> symbolList = new List<string>() { "!", "@", "$", "&", "=" };
            string password = "";
            Random NumRan = new Random();
            if (capital) { dataa.AddRange(dataA); }
            if (number) { dataa.AddRange(numberList);}
            if (symbol) { dataa.AddRange(symbolList);}
            for (int i = 0; i < length; i++)
            {
                password += dataa[NumRan.Next(0,dataa.Count)];
            }
            return password;
        }
    }
}