using System.Text.RegularExpressions;

namespace reto19;

/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */
class Program
{
    static void Main(string[] args)
    {
        string textToAnalyze = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " + 
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. " +
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. " +
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
        
        TextAnalyzer(textToAnalyze);
        /*
        The text has 69 words.
        The average word length is 5.
        Has 4 sentences.
        The longuest word is: reprehenderit.
        */

    }

    static void TextAnalyzer(string text)
    {
        string longuestWord = "";
        int totalChars = 0 ;
        // get all the words of the text.
        MatchCollection words = Regex.Matches(text,@"\w+");
        
        //get the sentences of the text using the point as reference.
        MatchCollection sentences = Regex.Matches(text,@"\.");

        foreach (Match item in words)
        { 
            int wordLength = item.Value.Length;
            if(wordLength > longuestWord.Length) longuestWord = item.Value;
            totalChars += wordLength;
        }


        System.Console.WriteLine($"The text has {words.Count} words.");
        System.Console.WriteLine($"The average word length is {totalChars/words.Count}.");
        System.Console.WriteLine($"Has {sentences.Count} sentences.");
        System.Console.WriteLine($"The longuest word is: {longuestWord}.");
    }
}
