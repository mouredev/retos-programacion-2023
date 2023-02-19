using System;
using System.Collections.Generic;

class miguelex
{
    static void Main(string[] args)
    {
        Console.Write($"¡Felicidades! Según tus respuestas, perteneces a la casa de {HogwartsHatSelector()}");
    }

    static string HogwartsHatSelector()
    {
        Console.WriteLine("Bienvenido al Test de Clasificación de Casas de Hogwarts!");
        Console.WriteLine("Responde las siguientes preguntas para saber a qué casa pertenecerías:");

        string[] preguntas = {
            "1. ¿Qué cualidad valoras más en ti mismo?",
            "2. ¿Qué criatura mágica te gustaría tener como mascota?",
            "3. ¿Cuál es tu asignatura favorita en Hogwarts?",
            "4. ¿Cuál es tu lugar favorito en el castillo de Hogwarts?",
            "5. ¿Cuál es tu hechizo favorito?"
        };

        string[][] opciones = {
            new string[] {"a. Coraje", "b. Inteligencia", "c. Lealtad", "d. Astucia"},
            new string[] {"a. Búho", "b. Gato", "c. Rata", "d. Lechuza"},
            new string[] {"a. Pociones", "b. Transformaciones", "c. Herbología", "d. Defensa contra las Artes Oscuras"},
            new string[] {"a. La Sala Común de mi casa", "b. El Gran Comedor", "c. La Biblioteca", "d. Los terrenos del castillo"},
            new string[] {"a. Expecto Patronum", "b. Wingardium Leviosa", "c. Expelliarmus", "d. Lumos"}
        };

        // Elegimos cuatro preguntas al azar
        List<int> randomQuestions = new List<int>();
        while (randomQuestions.Count < 4)
        {
            int random = new Random().Next(0, preguntas.Length);
            if (!randomQuestions.Contains(random))
            {
                randomQuestions.Add(random);
            }
        }

        List<string> respuestas = new List<string>();
        foreach (int i in randomQuestions)
        {
            Console.WriteLine(preguntas[i]);
            foreach (string opcion in opciones[i])
            {
                Console.WriteLine(opcion);
            }
            Console.Write("Elige una opción (a, b, c o d): ");
            string respuesta = Console.ReadLine() ?? "";
            respuestas.Add(respuesta);
        }

        Dictionary<string, int> puntuaciones = new Dictionary<string, int> {
            { "Gryffindor", 0 },
            { "Ravenclaw", 0 },
            { "Hufflepuff", 0 },
            { "Slytherin", 0 }
        };
        foreach (string respuesta in respuestas)
        {
            switch (respuesta)
            {
                case "a":
                    puntuaciones["Gryffindor"] = puntuaciones["Gryffindor"] + 1;
                    break;
                case "b":
                    puntuaciones["Ravenclaw"] = puntuaciones["Ravenclaw"] + 1;
                    break;
                case "c":
                    puntuaciones["Hufflepuff"] = puntuaciones["Hufflepuff"] + 1;
                    break;
                case "d":
                    puntuaciones["Slytherin"] = puntuaciones["Slytherin"] + 1;
                    break;
            }
        }

        string casa = puntuaciones.Aggregate((x, y) => x.Value > y.Value ? x : y).Key;
        return casa;
    }
}