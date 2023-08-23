namespace Reto_30
{
    internal class Program
    {
        static Dictionary<string, string> t9 = new Dictionary<string, string>()
        {
            {"1", "@"},
            {"2", "a"},
            {"22", "b"},
            {"222", "c"},
            {"3", "d"},
            {"33", "e"},
            {"333", "f"},
            {"4", "g"},
            {"44", "h"},
            {"444", "i"},
            {"5", "j"},
            {"55", "k"},
            {"555", "l"},
            {"6", "m"},
            {"66", "n"},
            {"666", "o"},
            {"7", "p"},
            {"77", "q"},
            {"777", "r"},
            {"7777", "s"},
            {"8", "t"},
            {"88", "u"},
            {"888", "v"},
            {"9", "w"},
            {"99", "x"},
            {"999", "y"},
            {"9999", "z"},
            {"0", " "},
            {"-", ""}
        };

        static void Main(string[] args)
        {
            string start = "";
            Console.WriteLine("Pulse ENTER para empezar, o cualquier otra letra para cerrar.");

            while (start == "") 
            {
                Console.WriteLine("Bienvenido al teclado T9.");
                Console.WriteLine("Pulsa ENTER para continuar...");
                string enter = Console.ReadLine();

                while (enter != "")
                {
                    Console.WriteLine("¡Uepa! Debes de pulsar ENTER.");
                    enter = Console.ReadLine();
                }

                keyboardT9();
                Console.WriteLine("Pulse ENTER para escribir otro mensaje o cualquier otra letra para cerrar.");
                start = Console.ReadLine();
            }
        }

        static void keyboardT9()
        {
            Console.WriteLine("Escriba texto usando el teclado númerico (0-9). Si escribes solo un carácter, debes de finalizar con guón.");
            Console.WriteLine("Ejemplos: \n4- = g \n44-666-555-2 = hola");
            Console.WriteLine("Esciba los números a traducir a continuación:");
            string input = Console.ReadLine();

            while (t9.TryGetValue(input, out string numberKey)) //Si escribimos algo que no es un número o una "-" sola, da error y volvemos a pedir la entrada.
            {
                Console.WriteLine("¡Uepa! Debes de escibir un número como en el sistema T9.");
                input = Console.ReadLine();
            }

            string[] message = input.Split("-"); //Transformamos el input en un arreglo de cadenas. Con el método Split(); las separamos mediante "-".
            
            string output = "";

            for (int i=0; i<message.Length; i++) // Recorremos cada letra del input y buscamos su correspondiente traducción.
            {
                if (t9.ContainsKey(message[i].ToString()))
                {
                    output = output + t9[message[i].ToString()];
                }
            }
            Console.WriteLine(output);
        }
    }
}
