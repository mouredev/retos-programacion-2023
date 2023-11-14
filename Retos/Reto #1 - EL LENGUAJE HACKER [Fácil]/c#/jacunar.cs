/*
# Reto #1: EL "LENGUAJE HACKER"
# Dificultad: Fácil

## Enunciado

 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

static void LenguajeHacker(string texto) {
    Dictionary<string, string> ClaveLeet = new Dictionary<string, string>() {
        { "a", "4" }, { "b", "|3" }, { "c", "[" }, { "d", ")" },
        { "e", "3" }, { "f", "|=" }, { "g", "&" }, { "h", "#" },
        { "i", "1" }, { "j", ",_|" }, { "k", ">|" }, { "l", "1" },
        { "m", @"/\/\" }, { "n", "^/" }, { "o", "0" }, { "p", "|*" },
        { "q", "(-,)" }, { "r", "|2" }, { "s", "5" }, { "t", "7" },
        { "u", "(_)" }, { "v", @"\/" }, { "w", @"\/\/" }, { "x", "><" },
        { "y", "j" }, { "z", "2" }, { "1", "L" }, { "2", "R" },
        { "3", "E" },  { "4", "A" }, { "5", "S" }, { "6", "b" },
        { "7", "T" }, { "8", "B" }, { "9", "g" }, { "0", "o" }
    };

    Console.WriteLine("Cadena entrada: " + texto);
    texto = texto.ToLower();
    char[] textoseparado = texto.ToCharArray();
    string nuevacadena = "";
    foreach (var item in textoseparado) {
        string valor = "";
        bool result = ClaveLeet.TryGetValue(item.ToString(), out valor);
        if (result)
            nuevacadena+= valor;
    }
    Console.WriteLine("Resultado: " + nuevacadena);
}

public class Program {
    static void Main(string[] args) {
        Reto01.LenguajeHacker("josue");
        Reto01.LenguajeHacker("jacunar103");
        Console.Read();
    }
}