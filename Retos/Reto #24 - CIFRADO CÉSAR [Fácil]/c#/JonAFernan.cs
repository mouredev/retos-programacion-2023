using System.Text.RegularExpressions;
using System.Text;

namespace Reto23;

/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */

class Program
{
    static void Main(string[] args)
    {
        int key = 17;

        string text = "Crea un programa que realize el cifrado César de un texto y lo imprima."
                      + "También debe ser capaz de descifrarlo cuando así se lo indiquemos.";
        
        System.Console.WriteLine(CaesarCipherEncrypt(text,key));
        System.Console.WriteLine(CaesarCipherDecrypt(CaesarCipherEncrypt(text,key),key));
        
    }

    static string CaesarCipherEncrypt(string text, int key)
    {
        //Remove all non-ASCII characters from text
        text = Regex.Replace(text.Normalize(NormalizationForm.FormD),"[^\x00-\x7F]+","");
        
        text = Regex.Replace(text,"[A-Z]",m=>m.ToString().ToLower());

        //Encrypt text
        return text = Regex.Replace(text,"[a-z]",new MatchEvaluator(new Cipher(key).Encrypt));
        
    }

    static string CaesarCipherDecrypt(string text, int key)
    {
       return text = Regex.Replace(text,"[a-z]",new MatchEvaluator(new Cipher(key).Decrypt));    
    }

    class Cipher
    {
        private int _key;
        private int [] alphabetArray = Enumerable.Range(97,122-97 + 1).ToArray();

        public Cipher(int key)
        {
            _key = key;
        }

        public string Encrypt(Match m)
        {
            int letter = (int)char.Parse(m.ToString());
            int index = Array.IndexOf(alphabetArray,letter);

            for(int i=0 ; i < _key; i++)
            {
               if(index+1 == alphabetArray.Length) index=-1;
               
                letter = alphabetArray[index+1];
                index++;
            }
            
            return ((char)letter).ToString();		
        }
        public string Decrypt(Match m)
        {
            int letter = (int)char.Parse(m.ToString());
            int index = Array.IndexOf(alphabetArray,letter);

            for(int i=0 ; i < _key; i++)
            {
                if(index == 0) index=alphabetArray.Length;
 
                letter = alphabetArray[index-1];
                index--;
                
            }
            
            return ((char)letter).ToString();		
        }
        
    }

}