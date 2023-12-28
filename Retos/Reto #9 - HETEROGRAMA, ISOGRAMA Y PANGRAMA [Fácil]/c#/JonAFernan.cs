namespace Reto9;

/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
class Program
{
    static void Main(string[] args)
    {   
        //All false
        //string text = "Hola Mundo";
        //heterograma y isograma
        //string text = "Murcíelago";
        //isograma
        //string text = "Dodo";
        //pangrama  
        string text = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja";
        
        TextType(text);
    }

    static void TextType(string text)
    {
        System.Console.Write("Texto a examinar: ");
        System.Console.WriteLine(text);
        string isHeterograma = Heterograma(text) ? "es" : "no es";
        string isIsograma = Isograma(text) ? "es" : "no es";
        string isPangrama = Pangrama(text) ? "es" : "no es";

        Console.WriteLine($"El texto {isHeterograma} heterograma, {isIsograma} isograma y {isPangrama} pangrama.");
    }

    static bool Heterograma(string text)
    {
        //A heterogram is a word, phrase, or sentence in which no letter of the alphabet occurs more than once.
        text = TextFormat(text);
        for (int i = 0; i < text.Length; i++)
        {
            if(text[i]==' ') continue;
            for (int j = 0; j < text.Length; j++)
            {
                if(i != j && text[i] == text[j]) return false; 
            }
            
        }
        return true;
    }

    static bool Isograma(string text)
    {
        //An isogram is a word that contains repeated letters the same number of times
        text = TextFormat(text);
        List<int> letterCounterList = new List<int>();
        for (int i = 0; i < text.Length; i++)
        {
            if(text[i]==' ') return false;
            int letterCounter = 0;
            for (int j = 0; j < text.Length; j++)
            {
                if(i != j && text[i] == text[j]) letterCounter ++;
            }

            letterCounterList.Add(letterCounter);
        }
        for (int i = 0; i < letterCounterList.Count - 1; i++)
        {
            if(i < text.Length)
            {
                if(letterCounterList[i] != letterCounterList[i+1]) return false;
            }
        }
        return true;
    }

    static bool Pangrama(string text)
    {
        // A pangram or holoalphabetic sentence is a sentence using every letter of a given alphabet at least once
        char [] alphabet = "abcdefghijklmnñopqrstuvwyxz".ToCharArray();
        text = TextFormat(text);

        foreach (var item in alphabet)
        {
            if(!text.Contains(item)) return false;
        }
        return true;

    }

    static string TextFormat(string text)
    {
        Dictionary<char,char> accentuationConverter = new Dictionary<char, char>()
        {
        {'á','a'},
        {'é','e'},
	    {'í','i'},
        {'ó','o'},
        {'ú','u'},
        };

        text = text.ToLower();
        char [] textArray = text.ToCharArray();

        for (int i = 0; i < textArray.Length; i++)
        {
            if(accentuationConverter.TryGetValue(textArray[i], out char value)) textArray[i] = value;
        }

        return text = new String(textArray);
    }
}
