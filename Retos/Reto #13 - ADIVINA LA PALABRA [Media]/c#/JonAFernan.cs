namespace reto13;

/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */
class Program
{
    static void Main(string[] args)
    {
        GuessTheWord();
    }

    static void GuessTheWord()
    {
        string secretWord , wordSolution;
        List<string> missingLetters = new List<string>();
        int remainingTries = 3;
        string updateSecretWord = string.Empty;
        
        SecretWordGenerator(out secretWord , out wordSolution, ref missingLetters);
        
        do
        {
            Console.WriteLine($"You have {remainingTries} tries to discover {secretWord}");
        
            string userAnswer = Console.ReadLine().ToLower();

            if(userAnswer.Length > 1 && userAnswer == wordSolution) secretWord = userAnswer;
            else if (userAnswer.Length == 1 && missingLetters.Contains(userAnswer))
            {
                for (int i = 0; i < secretWord.Length; i++)
                {
                    if(secretWord[i] == '_' && wordSolution[i] == char.Parse(userAnswer))
                    {
                        missingLetters.Remove(userAnswer);
                        updateSecretWord += userAnswer;
                        continue;
                    }

                    updateSecretWord += secretWord[i];
                }

                secretWord = updateSecretWord;
                updateSecretWord = string.Empty;
            }
            else remainingTries -= 1;
            
        } while (remainingTries > 0 && secretWord != wordSolution);

        if(remainingTries == 0) Console.WriteLine("You lose");
        else Console.WriteLine("You win");
        
    }

    static void SecretWordGenerator(out string secretWord, out string wordSolution, ref List<string> missingLetters)
    {
        List<string> randomWords = new List<string> { "apple", "banana", "cherry", "motorbike", "elderberry", "abracadabra", "grape", "honeydew", "kiwi", "lemon" };
        Random random = new Random();

        wordSolution = randomWords[random.Next(randomWords.Count - 1)];
        char [] secretWordArray = wordSolution.ToCharArray();

        int numberOfMissingLetter = (wordSolution.Length + 1) / 2 ;
        int index;
        int [] alredyUseIndex = new int[numberOfMissingLetter];
        
        for (int i=0; i < numberOfMissingLetter; i++ )
        {
            do
            {
                index = random.Next(secretWordArray.Length);

            } while (alredyUseIndex.Contains(index));

            if(!missingLetters.Contains(secretWordArray[index].ToString())) missingLetters.Add(secretWordArray[index].ToString());
            secretWordArray[index] = '_';
            alredyUseIndex[i] = index;
            
        }

        secretWord = new String(secretWordArray);
    }
}
