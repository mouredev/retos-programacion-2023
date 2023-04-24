using System.Text.RegularExpressions;
/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico 
 * del universo Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */

 public class Reto15
{
   public static void Main()
   {
      
      string spanishinput = "Trillado Fornido chocolate";
      string aurebeshInput = "¡HerfOskLethAurek MernUskNernDornOsk!";
      Console.WriteLine(AurebeshTraslator(spanishinput));   // TrillReshIskLethLethAurekDornOsk FornOskReshNernIskDornOsk CherekOskCreshOskLethAurekTrillEsk
      Console.WriteLine(AurebeshTraslator(aurebeshInput));  // ¡Hola mundo!                 
   }

   static string AurebeshTraslator(string wordToTraslate)
   {

      if(!Regex.IsMatch(Regex.Replace(wordToTraslate, "[^a-zA-Z]", ""), $"^[{String.Join("|",alphabetToAurebesh.Values)}]+$"))
      {
         return Regex.Replace(wordToTraslate.ToLower(), String.Join("|", alphabetToAurebesh.Keys), m => alphabetToAurebesh[m.Value]);
      }

      Dictionary<string, string> aurebeshToAlphabet = new Dictionary<string, string>();

      foreach (KeyValuePair<string, string> item in alphabetToAurebesh)
      {
         aurebeshToAlphabet.Add(item.Value, item.Key);
      }

      // Capitalize the first letter of the traslation to spanish ignoring special characters.
      Regex r = new Regex(@"\b[a-z]");

      return r.Replace(Regex.Replace(wordToTraslate, String.Join("|", aurebeshToAlphabet.Keys), m => aurebeshToAlphabet[m.Value]), m => m.ToString().ToUpper(), 1 , 0);
   }

   static Dictionary<string, string> alphabetToAurebesh = new Dictionary<string, string>()
   {
      {"a", "Aurek"},
      {"b", "Besh"},
      {"ch","Cherek"},
      {"c", "Cresh"},
      {"d", "Dorn"},
      {"e", "Esk"},
      {"f", "Forn"},
      {"g", "Grek"},
      {"h", "Herf"},
      {"i", "Isk"},
      {"j", "Jenth"},
      {"k", "Krill"},
      {"l", "Leth"},
      {"m", "Mern"},
      {"n", "Nern"},
      {"o", "Osk"},
      {"p", "Peth"},
      {"q", "Qek"},
      {"r", "Resh"},
      {"s", "Senth"},
      {"t", "Trill"},
      {"u", "Usk"},
      {"v", "Vev"},
      {"w", "Wesk"},
      {"x", "Xesh"},
      {"y", "Yirt"},
      {"z", "Zerek"}
   };


}