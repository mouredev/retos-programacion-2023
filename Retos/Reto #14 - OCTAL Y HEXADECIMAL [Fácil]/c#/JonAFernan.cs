using System.Text;

/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

namespace reto14;
class Program
{
    static void Main(string[] args)
    {
        DecimalToOctalAndHex(268434155);
        DecimalToOctalAndHex(1235);
        DecimalToOctalAndHex(897785);
        DecimalToOctalAndHex(328);
    }

    static void DecimalToOctalAndHex(int numberDecimal)
    {        
        Console.WriteLine($"The octal and the hex number for {numberDecimal} are {DecimalToOctal(numberDecimal)} and {DecimalToHex(numberDecimal)}");
    }

    static string DecimalToOctal(int numberDecimal)
  {
    
    bool loop = true;
    List<int> remainderList = new List<int>();
    StringBuilder octal = new StringBuilder();
    
    do
    {
      if(numberDecimal <= 8)
      {
        remainderList.Add(numberDecimal);
        loop = false;
      }
      else
      {
        remainderList.Add(numberDecimal % 8);  
        numberDecimal = numberDecimal / 8;
      }

    } while (loop);

    remainderList.Reverse();

    foreach (int item in remainderList)
    {
      octal.Append(item);
    }

    return octal.ToString();
    
  }

   static string DecimalToHex(int numberDecimal)
  {
    Dictionary<int, string> hexDict = new Dictionary<int, string>
    {
        {10,"A"},
        {11,"B"},
        {12,"C"},
        {13,"D"},
        {14,"E"},
        {15,"F"}

    };
    
    bool loop = true;
    List<int> remainderList = new List<int>();
    StringBuilder hex = new StringBuilder();
    
    do
    {
      if(numberDecimal <= 16)
      {
        remainderList.Add(numberDecimal);
        loop = false;
      }
      else
      {
        remainderList.Add(numberDecimal % 16);  
        numberDecimal = numberDecimal / 16;
      }

    } while (loop);

    remainderList.Reverse();

    foreach (int item in remainderList)
    {
        if(hexDict.ContainsKey(item)) hex.Append(hexDict[item]);
        else hex.Append(item);
    }

    return hex.ToString();
  }
}
