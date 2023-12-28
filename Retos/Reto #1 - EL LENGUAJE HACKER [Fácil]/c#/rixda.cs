/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

namespace traductor{
    class leet{
       #region diccionario   
       Dictionary<string, string> leet = new Dictionary<string, string>();
        leet.Add("a", "4");
        leet.Add("b", "I3");
        leet.Add("c", "[");
        leet.Add("d", ")");
        leet.Add("e", "3");
        leet.Add("f", "|=");
        leet.Add("g", "&");
        leet.Add("h", "#");
        leet.Add("i", "1");
        leet.Add("j", ",_|");
        leet.Add("k", ">|");
        leet.Add("l", "1");
        leet.Add("m", @"/\/\ ");   // el @ es para que no tome la contrabarra como una secuencia de escape
        leet.Add("n", "^/");
        leet.Add("o", "0");
        leet.Add("p", "|*");
        leet.Add("q", "(_,)");
        leet.Add("r", "I2");
        leet.Add("s", "5");
        leet.Add("t", "7");
        leet.Add("u", "(_)");
        leet.Add("v", @"\/");     // el @ es para que no tome la contrabarra como una secuencia de escape
        leet.Add("w", @"\/\/");   // el @ es para que no tome la contrabarra como una secuencia de escape
        leet.Add("x", "><");
        leet.Add("y", "j");
        leet.Add("z", "2");
        leet.Add("1", "L");
        leet.Add("2", "R");
        leet.Add("3", "E");
        leet.Add("4", "A");
        leet.Add("5", "S");
        leet.Add("6", "b");
        leet.Add("7", "T");
        leet.Add("8", "B");
        leet.Add("9", "g");
        leet.Add("0", "o");
        leet.Add(" ", " ");
        #endregion

        public string Leet(string imputText){
        imputText.ToLower();
        string outText = "";
        string temp;

        foreach (char item in imputText)
        {
            leet.TryGetValue(item.ToString(),out temp );
            outText += temp;
        }

        return outText;
        }


    }
}