// See https://aka.ms/new-console-template for more information



namespace reto1;
public class Reto1
{

    public static void Main(string[] args)
    {
        Console.WriteLine("Escribe la frase que quieras ver traducida a 1337 speak");
        var frase = Console.ReadLine();
        Console.WriteLine(ToLeetSpeak(frase));
    }

    private static string ToLeetSpeak(string? frase)
    {
        if (string.IsNullOrWhiteSpace(frase)) return frase;
        var dictionary = new Dictionary<char, string> 
        {
            {'a',"4" },
            {'b',"I3" },
            {'c',"[" },
            {'d',")" },
            {'e',"3" },
            {'f',"|=" },
            {'g',"&" },
            {'h',"#" },
            {'i',"1" },
            {'j',",_|" },
            {'k',">|" },
            {'l',"1" },
            {'m',"/\\/\\" },
            {'n',"^/" },
            {'o',"0" },
            {'p',"|*" },
            {'q',"(_,)" },
            {'r',"I2" },
            {'s',"5" },
            {'t',"7" },
            {'u',"(_)" },
            {'v',"\\/" },
            {'w',"\\/\\/" },
            {'x',"><" },
            {'y',"j" },
            {'z',"o" },
            {'0',"L" },
            {'1',"L" },
            {'2',"R" },
            {'3',"E" },
            {'4',"A" },
            {'5',"S" },
            {'6',"b" },
            {'7',"T" },
            {'8',"B" },
            {'9',"g" }

        };
        return string.Join (null,frase.ToLower().Select(c => dictionary.TryGetValue(c, out string leetChar) ? leetChar : c.ToString()));
    }
}