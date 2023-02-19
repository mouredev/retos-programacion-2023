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
            "5. ¿Cuál es tu hechizo favorito?",
            "6. ¿Qué objeto mágico te gustaría poseer?",
            "7. ¿Cuál es tu personaje favorito de Harry Potter?",
            "8. ¿Qué harías si te enfrentas a un troll?",
            "9. ¿Qué tipo de clima prefieres?",
            "10. ¿Cuál es tu forma preferida de transporte mágico?",
            "11. ¿Qué color te atrae más?",
            "12. ¿Qué criatura mágica te da más miedo?",
            "13. ¿Cuál es tu golosina mágica favorita?",
            "14. ¿Cuál es tu asignatura menos favorita en Hogwarts?",
            "15. ¿Qué actividad te gustaría hacer en tu tiempo libre en Hogwarts?"
        };

        string[][] opciones = {
            new string[] {"a. Coraje", "b. Inteligencia", "c. Lealtad", "d. Astucia"},
            new string[] {"a. Búho", "b. Gato", "c. Rata", "d. Lechuza"},
            new string[] {"a. Pociones", "b. Transformaciones", "c. Herbología", "d. Defensa contra las Artes Oscuras"},
            new string[] {"a. La Sala Común de mi casa", "b. El Gran Comedor", "c. La Biblioteca", "d. Los terrenos del castillo"},
            new string[] {"a. Expecto Patronum", "b. Wingardium Leviosa", "c. Expelliarmus", "d. Lumos"},
            new string[] {"a. La Capa de Invisibilidad", "b. La Varita dNeville Longbottom", "d. Draco Malfoy"},
            new string[] {"a. Huir", "b. Atacar", "c. Pedir ayuda", "d. Intentar razonar con él"},
            new string[] {"a. Sol", "b. Lluvia", "c. Nieve", "d. Viento"},
            new string[] {"a. Escoba voladora", "b. El Autobús Noctámbulo", "c. El Tren Hogwarts Express", "d. Aparición"},
            new string[] {"a. Rojo", "b. Azul", "c. Amarillo", "d. Verde"},
            new string[] {"a. Dementor", "b. El Basilisco", "c. El Hombre Lobo", "d. Las Arpías"},
            new string[] {"a. Grageas de Todos los Sabores", "b. Chocolate de la Caja de Bertie Bott", "c. Pastel de Calabaza", "d. Caramelos de Menta"},
            new string[] {"a. Historia de la Magia", "b. Adivinación", "c. Estudio de los Muggles", "d. Runas Antiguas"},
            new string[] {"a. Jugar al Quidditch", "b. Explorar el castillo", "c. Leer en la Biblioteca", "d. Pasar tiempo con amigos"}
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