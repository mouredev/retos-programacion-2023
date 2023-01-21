namespace Reto3_2023;

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
class Program
{
    static void Main(string[] args)
    {
    Console.WriteLine(PasswordGenerator(true,true,true));   
    }

    static string PasswordGenerator( bool mayus, bool numbers, bool symbols, int pswLong = 8)
    {
        // verificar que la longitud de la contraseña es la correcta
        if (pswLong > 16 || pswLong < 8)
            {
                pswLong= 8;
                System.Console.WriteLine("La longitud de la contraseña ha de ser entre 8 y 16 caracteres");
                System.Console.WriteLine("Se establece la configuración por defecto de 8 caracteres");
            }

        string passWord = "";
        char [] passWordCharArray = new char[pswLong];
        List<char> passWordCharList = new List<char>();
        var random = new Random();
        char[] alphabetArray = "abcdefghijklmnopqestuvwxyz".ToCharArray();
        char[] alphabetArrayMayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray();
        char[] numbersArray = "0123456789".ToCharArray();
        char[] symbolsArray = "!@#|$%&_-<>?¿*+()[]:;,/º".ToCharArray();
        int counterChars = 0;
        int numberOfLowers;

        if(mayus)
            {
                for (int i = 0; i < random.Next(2,pswLong/4); i++)
                {
                    passWordCharList.Add(alphabetArrayMayus[random.Next(alphabetArrayMayus.Length)]);
                    counterChars ++ ;
                }
                
            }
        if(numbers)
            {   for (int i = 0; i < random.Next(2,pswLong/4); i++)
                {
                passWordCharList.Add(numbersArray[random.Next(numbersArray.Length)]);
                counterChars ++ ;
                }
            }
        if(symbols)
            {
                for (int i = 0; i < random.Next(2,pswLong/4); i++)
                {
                passWordCharList.Add(symbolsArray[random.Next(symbolsArray.Length)]);
                counterChars ++ ;
                }
            }
        numberOfLowers =pswLong-counterChars;
        for (int i = 0; i < numberOfLowers; i++)
        {
            passWordCharList.Add(alphabetArray[random.Next(alphabetArray.Length)]);
            counterChars++;
        }
        
        // Colocamos los carecteres en posiciones aleatorias
        for (int i = 0; i < passWordCharArray.Length ; i++)
        {
            int indexList = random.Next(passWordCharList.Count);
            passWordCharArray[i] = passWordCharList[indexList];
            passWordCharList.RemoveAt(indexList);
        }
        
            
        passWord = new string(passWordCharArray);
        return passWord;
    }
}

