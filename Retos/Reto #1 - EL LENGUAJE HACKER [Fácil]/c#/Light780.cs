namespace Reto1_LenguajeHacker
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Inicio:
            Console.WriteLine("Escriba una palabra: ");
            var cadena = Console.ReadLine();
            
            if(cadena == null)            
                goto Inicio;

            Console.WriteLine(string.Join("", cadena.Select(c => leetAbc[char.ToUpper(c)])));
        }

        static Dictionary<char, string> leetAbc = new()
        {
            {'A', @"1"}, {'B', @"I3"}, {'C', @"["},
            {'D', @")"}, {'E', @"3"},
            {'F', @"|="},
            {'G', @"&"},
            {'H', @"#"},
            {'I', @"1"},
            {'J', @",_|"},
            {'K', @">|"},
            {'L', @"1"},
            {'M', @"/\\/\\"},
            {'N', @"^/"},
            {'O', @"0"},
            {'P', @"|*"},
            {'Q', @"(_,)"},
            {'R', @"I2"},
            {'S', @"5"},
            {'T', @"7"},
            {'U', @"(_)"},
            {'V', @"\\/"},
            {'W', @"\/\/"},
            {'X', @"><"},
            {'Y', @"j"},
            {'Z', @"2"},
            {'1', @"L"},
            {'2', @"R"},
            {'3', @"E"},
            {'4', @"A"},
            {'5', @"S"},
            {'6', @"b"},
            {'7', @"T"},
            {'8', @"B"},
            {'9', @"g"},
            {'0', @"o"},
            {' '," "}
        };
    }
}