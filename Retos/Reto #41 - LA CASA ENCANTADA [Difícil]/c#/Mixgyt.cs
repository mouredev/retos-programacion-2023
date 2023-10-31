using System;

class Program
{
    private static string[,] mansion = new string[4,4]; 
    static string room = "⬜️";
    static string exit = "✅";
    static string candy = "🍭";
    static string entry = "🚪";
    static string bonus = "❓";
    static string ghost = "👻";
    static string viewed = "❎";

    static Dictionary<string,string> questions = new Dictionary<string, string>() {
        {"¿El agua moja?","si"},
        {"Plata no es ¿dime que es?","platano"},
        {"Si un objeto imparable choca con un objeto inamovible que pasa", "nada"},
        {"Si tengo 3 peces y se ahoga 1 cuantos tengo","3"},
        {"Napoleon tenia un caballo blanco, de que color era el caballo de Napoleon","blanco"},
        {"Siempre paso helada y prima es la hielera","nevera"},
        {"¿Que le paso a la gallina cuando cruzo la calle?","llego al otro lado"},
        {"Sostengo muchas perlas blancas unas arriba unas abajo", "dentadura"}
    };

    static void Main()
    {
        Random random = new Random();

        for(int i = 0; i < mansion.GetLength(1); i++)
        {
            for(int j = 0; j < mansion.GetLength(0); j++)
            {
                mansion[j,i] = room;
            }
        }

        void placeObject(string obj, int prob = 0) //la probabilidad la tomo del 1 al 10 (1 siendo el 10% de 10)
        {
            int x = random.Next(0,mansion.GetLength(0));
            int y = random.Next(0,mansion.GetLength(1));
            int i = random.Next(1,11);

            if(i >= prob)
            {
                if(mansion[x,y] == room)
                {
                    mansion[x,y] = obj;
                }
                else
                {
                    placeObject(obj);
                }
            }
        }

        void findObject(string obj, out int x, out int y)
        {
            x = 0;
            y = 0;
            for(int j = 0; j < mansion.GetLength(1); j++)
            {
                for(int i = 0; i < mansion.GetLength(0); i++)
                {
                    if(mansion[i,j] == obj)
                    {
                        x = i;
                        y = j;
                    }
                }
            }
        }

        Player instance()
        {
            for(int y = 0; y < mansion.GetLength(1); y++)
            {
                for(int x = 0; x < mansion.GetLength(0); x++)
                {
                    if(mansion[x,y] == entry)
                    {
                        return new Player(x,y);
                    }
                }
            }
            return new Player(0,0);
        }
        
        placeObject(entry);
        placeObject(exit);
        placeObject(bonus,10);
        placeObject(bonus,10);
        Player player = instance();  

        Console.WriteLine("¡¡Boo...!! estas atrapado en una casa encantada \nPara salir necesitas encontrar el salon con dulces");
        while(!candyFound())
        {
            print(mansion, player);
            string controls = "";
            if(player.y > 0)
            {
                controls += "W(Arriba) ";
            }
            if(player.y < mansion.GetLength(1)-1)
            {
                controls += "S(Abajo) ";
            }
            if(player.x > 0)
            {
                controls += "A(Izquierda) ";
            }
            if(player.x < mansion.GetLength(0)-1)
            {
                controls += "D(Derecha)";
            }
            Console.WriteLine($"Muevete usando {controls} (Q darse por vencido)");
            if(getText(out string text, "wasd"))
            {
                switch(text)
                {
                    case "w":
                        if(player.y - 1 >= 0)
                        --player.y;
                        else
                        continue;
                        break;
                    case "s":
                        if(player.y + 1 < mansion.GetLength(1))
                        ++player.y;
                        else
                        continue;
                        break;
                    case "a":
                        if(player.x - 1 >= 0)
                        --player.x;
                        else
                        continue;
                        break;
                    case "d":
                        if(player.x + 1 < mansion.GetLength(0))
                        ++player.x;
                        else
                        continue;
                        break;
                }
            }
            else
            {
                if(text == "q")
                {
                    Console.WriteLine("Te das por vencido y el programa termina... ");
                    Environment.Exit(0);
                }
                Console.WriteLine("No has escrito W, A, S o D\nVuelve a intentarlo");
                continue;
            }

            findObject(bonus,out int x, out int y);
            if(player.x == x && player.y == y)
            {
                Console.WriteLine("Encuentras un fantasma 👻 Booo... y te hace una pregunta");
                showQuestion();
                Console.WriteLine("Ahora puedes seguir con la pregunta siguiente Booo... 👻");
                mansion[x,y] = ghost;
            }

            if(!candyFound())
            {
                Console.WriteLine("Acerta la pregunta para poder cambiar de habitación");
                showQuestion();
            }
        }
        player.icon = candy;
        print(mansion,player);
        Console.WriteLine("¡¡Felicidades!! has logrado encontrar los dulces y la salida de la mansion 🥳🥳");
        
        void showQuestion()
        {
            int q = random.Next(0,questions.Count);
            KeyValuePair<string,string> question = questions.ElementAt(q);
            Console.WriteLine($"Preguta: {question.Key}");
            Console.Write("Respuesta: ");
            string awser = Console.ReadLine().Trim().ToLower();
            Console.WriteLine("");

            if(awser == question.Value)
            {
                Console.WriteLine("¡Respuesta correcta!");
                mansion[player.x,player.y] = viewed;
            }
            else
            {
                Console.WriteLine("Incorrecto \nLo siento 👻 no te puedes ir sin responder bien una pregunta");
                showQuestion();
            }
        }

        bool candyFound()
        {
            if(mansion[player.x,player.y] == exit)
            {
                return true;
            }
            return false;
        }
    }

    static void print(string[,] ma, Player player)
    {
        for(int y = 0; y < ma.GetLength(1); y++)
        {
            for(int x = 0; x < ma.GetLength(0); x++)
            {
                if(player.icon != null && player.x == x && player.y == y)
                {
                    Console.Write(player.icon);
                    continue;
                }
                else if(ma[x,y] != room && ma[x,y] != entry && ma[x,y] != viewed)
                {
                    Console.Write(room);
                    continue;
                }
                Console.Write(ma[x,y]);
            }
            Console.WriteLine("");
        }
    }

    static bool getText(out string text, string chars = "")
    {
        text = Console.ReadLine().Trim().ToLower();
        if(text.Length > 1)
        {
            Console.WriteLine($"Valor no valido solo se permite 1 caracter de estos '{chars}'");
        }
        else if(chars.Intersect(text).Count() > 0)
        {
            return true;
        }

        return false;
    }
}

struct Player
{
    public string icon = "👦";
    public int x;
    public int y;

    public Player(int x, int y)
    {
        this.x = x;
        this.y = y;
    }
}
