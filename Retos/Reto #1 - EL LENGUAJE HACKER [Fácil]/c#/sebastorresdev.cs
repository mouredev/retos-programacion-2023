// Reto #1: EL "LENGUAJE HACKER"
// Dificultad: Fácil | Publicación: 02/01/23 | Corrección: 09/01/23

// Enunciado


/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

// recibimos un texto
using System.Text;

Dictionary<char, string> hackerLenguage = new Dictionary<char, string>()
{
    { 'a', "4"  }, { 'b', "I3"  }, { 'c', "["     }, { 'd', ")" }, { 'e', "3"  },
    { 'f', "|=" }, { 'g', "&"   }, { 'h', "#"     }, { 'i', "1" }, { 'j', ",_|"},
    { 'k', ">|" }, { 'l', "1"   }, { 'm', "^^"    }, { 'n', "^/"}, { 'o', "0"  },
    { 'p', "|*" }, { 'q', "(_,)"}, { 'r', "I2"    }, { 's', "5" }, { 't', "7"  },
    { 'u', "(_)"}, { 'v', "\\/" }, { 'w', "\\/\\/"}, { 'x', "><"}, { 'y', "j"  },
    { 'z', "2"  }, { '1', "L"   }, { '2', "R"     }, { '3', "E" }, { '4', "A"  },
    { '5', "S"  }, { '6', "b"   }, { '7', "T"     }, { '8', "B" }, { '9', "g"  },
    { '0', "o"  }
};

// obtengo el texto
string text = Console.ReadLine();
// convierto el texto a un nuevo texto hacker
string newText = ConvertToHackerLenguage(text);
// muestro en pantalla el nuevo texto
Console.WriteLine(newText);

string ConvertToHackerLenguage(string text)
{
    StringBuilder sb = new StringBuilder();
    foreach (char c in text.ToLower())
    {
        if (hackerLenguage.ContainsKey(c))
        {
            sb.Append(hackerLenguage[c]);
        }
        else
        {
            sb.Append(c);
        }
    }
    return sb.ToString();
}