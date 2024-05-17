namespace RetosProgramacion
{
    internal class Program
    {

        private static Dictionary<string, string> dictionary = new Dictionary<string, string>()
        {
            {"A", "4"},
            {"B", "I3"},
            {"C", "["},
            {"D", ")"},
            {"E", "3"},
            {"F", "|="},
            {"G", "&"},
            {"H", "#"},
            {"I", "1"},
            {"J", ",_|"},
            {"K", ">|"},
            {"L", "1"},
            {"M", @"/\/\"},
            {"N", "^/"},
            {"O", "0"},
            {"P", "|*"},
            {"Q", "(_,)"},
            {"R", "I2"},
            {"S", "5"},
            {"T", "7"},
            {"U", "(_)"},
            {"V", @"\/"},
            {"W", @"\/\/"},
            {"X", "><"},
            {"Y", "j"},
            {"Z", "2"}
        };
        static void Main(string[] args)
        { 

            Console.WriteLine("Ingrese un texto para transformarlo a lenguaje Hacker: ");
            string texto = Console.ReadLine();

            Console.WriteLine(TransformarTexto(texto));
           
        }

        private static string TransformarTexto(string texto)
        {
            foreach (var caracter in dictionary)
            {
                texto = texto.Replace(caracter.Key, caracter.Value).ToUpper().ToString();
            }
            return texto;
        }
    }
}
