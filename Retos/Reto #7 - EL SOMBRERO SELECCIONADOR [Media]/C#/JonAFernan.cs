namespace SombreroSeleccionador;

/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine(SortingHat());
    }

    static string SortingHat()
    {
        int gryffindorCounter = 0;
        int slytherinCounter = 0;
        int hufflepuffCounter = 0;
        int ravenclawCounter = 0;
        //used in case of tie.
        Random Dice = new Random();
        
        bool loopOut = false;

        string [] questionArray = 
        {"After I’m dead, people should remember me as:",
        "What's the worst nightmare?", 
        "If you can make a potion that is going to guarantee you one thing, what is it gonna be?", 
        "What would you never like to be called?",
        "You and your friends want to cross a bridge which is guarded by a river troll. He says that one of you fights him to cross the river. What would you do?"};
        
        string [] answerArray = 
        {"1.The Bold 2.The Great 3.The Kind 4. The Intellectual",
        "1.Everyone forgets you. 2.Being mocked by others 3.Standing at a height. 4. You are trapped in a dark room.",
        "1.Glory 2.Power 3.Love 4.Knowledge", 
        "1.Cowardly 2.Ordinary 3.Selfhis 4.Ignorant",
        "1.Volunteer for this fight 2.Have all 3 fight (without telling the troll) 3. Draw lots to see who fights 4. Confuse the troll"};


        for (int i = 0; i < questionArray.Length; i++)
        {
            do
            {
                System.Console.WriteLine(questionArray[i]);
                System.Console.WriteLine(answerArray[i]);
                string ? answer = Console.ReadLine();
                AnswerCheck(answer, ref gryffindorCounter, ref slytherinCounter, ref hufflepuffCounter, ref ravenclawCounter, ref loopOut);
                
            } while (loopOut);
            
        }

        int [] houses = {gryffindorCounter, slytherinCounter, hufflepuffCounter, ravenclawCounter};
        Array.Sort(houses);

        // In case of tie, the sorting hat will assign the house randomly between the two houses.
        if (houses[3] == houses[2])
        {
            List<string> tieList = new List<string>();
            
            if(houses[3] == gryffindorCounter) tieList.Add("Gryffindor");
            if(houses[3] == slytherinCounter) tieList.Add("Slytherin");
            if(houses[3] == hufflepuffCounter) tieList.Add("Hufflepuff");
            if(houses[3] == ravenclawCounter) tieList.Add("Ravenclaw");

            int x = Dice.Next(2);

            return $"Tu casa es {tieList[x]}";
            
        }
        
        else
        {
        
        if(houses[3] == gryffindorCounter) return $"Tu casa es Gryffindor";
        else if(houses[3] == slytherinCounter) return $"Tu casa es Slytherin";
        else if(houses[3] == hufflepuffCounter) return $"Tu casa es Hufflepuff";
        else return $"Tu casa es Ravenclaw";
        
        }

       
        
    }

    static void AnswerCheck(string userAnswer, ref int house1, ref int house2, ref int house3, ref int house4, ref bool loopOut)
    {
        switch (userAnswer)
        {
            case "1":
            house1++;
            loopOut = false;
            break;
            
            case "2":
            house2++;
            loopOut = false;
            break;

            case "3":
            house3++;
            loopOut = false;
            break;

            case "4":
            house4++;
            loopOut = false;
            break;

            default:
            System.Console.WriteLine("La respuesta no es valida. Por favor, introduzca un digito del 1 al 4.");
            loopOut = true;
            break;
        }
    }
}
