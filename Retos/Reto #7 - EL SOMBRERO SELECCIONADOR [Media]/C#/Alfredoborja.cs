using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Security.Cryptography.X509Certificates;

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


namespace SOMBREROSELECCIONADOR
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Cual es tu nombre?");
            string name = Console.ReadLine();

            Sombrero sombrero = new Sombrero(name);
            sombrero.makeQuestions(false);

            if (sombrero.isTie()) 
            {
                sombrero.makeQuestions(true);
                var houseWinner = sombrero.hitsByHouse().OrderByDescending(x => x.Aciertos).FirstOrDefault();
                Console.WriteLine("\nSeras parte de la casas "+ houseWinner.Nombre);
            }
            else
            {
                var houseWinner = sombrero.hitsByHouse().OrderByDescending(x => x.Aciertos).FirstOrDefault();
                Console.WriteLine("\nSeras parte de la casa de "+ houseWinner.Nombre+"!");
            }
        }
    }

    public class Sombrero 
    {
        public string Name { get; set; }
        public Sombrero(string name)
        {
            Preguntas = new List<Pregunta>();
            PosiblesRespuestas = new List<Respuesta>(); 
            generarPreguntas();
            generarRespuestas();
            generarCasas();
            Name = name;
        }

        List<string> RespuestasContestadas = new List<string>();
        public List<Pregunta> Preguntas { get; set; }
        public void generarPreguntas()
        {
            Preguntas.Add(new Pregunta { Id = 1, Interrogante = "Cual es tu color favorito ? ", IsTieBreaker = false });
            Preguntas.Add(new Pregunta { Id = 2, Interrogante = "Cual animal te gusta mas ? ", IsTieBreaker = false});
            Preguntas.Add(new Pregunta { Id = 3, Interrogante = "Cual es tu Personaje favorito ? ", IsTieBreaker = false });
            Preguntas.Add(new Pregunta { Id = 4, Interrogante = "Con cual valor te identificas mas ? ", IsTieBreaker = false });
            Preguntas.Add(new Pregunta { Id = 5, Interrogante = "Cual profesor favorito ? ",IsTieBreaker = false });
            Preguntas.Add(new Pregunta { Id = 6, Interrogante = "Cual es tu hechizo favorito? ", IsTieBreaker = true });
        }
        public List<Respuesta> PosiblesRespuestas { get; set; }
        public void generarRespuestas()
        {
            PosiblesRespuestas.Add(new Respuesta { Id = 1, TipoRespuesta = "Gryffindor", IdPregunta = 1, Contestacion = "Rojo" });
            PosiblesRespuestas.Add(new Respuesta { Id = 2, TipoRespuesta = "Slytherin", IdPregunta = 1, Contestacion = "Verde" });
            PosiblesRespuestas.Add(new Respuesta { Id = 3, TipoRespuesta = "Hafflepuff", IdPregunta = 1, Contestacion = "Naranja" });
            PosiblesRespuestas.Add(new Respuesta { Id = 4, TipoRespuesta = "Ravenclaw", IdPregunta = 1, Contestacion = "Azul" });

            PosiblesRespuestas.Add(new Respuesta { Id = 5, TipoRespuesta = "Gryffindor", IdPregunta = 2, Contestacion = "Leon" });
            PosiblesRespuestas.Add(new Respuesta { Id = 6, TipoRespuesta = "Slytherin", IdPregunta = 2, Contestacion = "Serpiente" });
            PosiblesRespuestas.Add(new Respuesta { Id = 7, TipoRespuesta = "Hafflepuff", IdPregunta = 2, Contestacion = "Cuervo" });
            PosiblesRespuestas.Add(new Respuesta { Id = 8, TipoRespuesta = "Ravenclaw", IdPregunta = 2, Contestacion = "Tejon" });

            PosiblesRespuestas.Add(new Respuesta { Id = 9, TipoRespuesta = "Gryffindor", IdPregunta = 3, Contestacion = "Neville" });
            PosiblesRespuestas.Add(new Respuesta { Id = 10, TipoRespuesta = "Slytherin", IdPregunta = 3, Contestacion = "Bulstrode" });
            PosiblesRespuestas.Add(new Respuesta { Id = 11, TipoRespuesta = "Hafflepuff", IdPregunta = 3, Contestacion = "Scamander" });
            PosiblesRespuestas.Add(new Respuesta { Id = 12, TipoRespuesta = "Ravenclaw", IdPregunta = 3, Contestacion = "Luna" });

            PosiblesRespuestas.Add(new Respuesta { Id = 13, TipoRespuesta = "Gryffindor", IdPregunta = 4, Contestacion = "Valiente" });
            PosiblesRespuestas.Add(new Respuesta { Id = 14, TipoRespuesta = "Slytherin", IdPregunta = 4, Contestacion = "Astuto" });
            PosiblesRespuestas.Add(new Respuesta { Id = 15, TipoRespuesta = "Hafflepuff", IdPregunta = 4, Contestacion = "Leal" });
            PosiblesRespuestas.Add(new Respuesta { Id = 16, TipoRespuesta = "Ravenclaw", IdPregunta = 4, Contestacion = "Intelectual" });

            PosiblesRespuestas.Add(new Respuesta { Id = 17, TipoRespuesta = "Gryffindor", IdPregunta = 5, Contestacion = "McGonagall" });
            PosiblesRespuestas.Add(new Respuesta { Id = 18, TipoRespuesta = "Slytherin", IdPregunta = 5, Contestacion = "Snape" });
            PosiblesRespuestas.Add(new Respuesta { Id = 19, TipoRespuesta = "Hafflepuff", IdPregunta = 5, Contestacion = "Sprout" });
            PosiblesRespuestas.Add(new Respuesta { Id = 20, TipoRespuesta = "Ravenclaw", IdPregunta = 5, Contestacion = "Flitwick" });

            PosiblesRespuestas.Add(new Respuesta { Id = 21, TipoRespuesta = "Gryffindor", IdPregunta = 6, Contestacion = "EXPECTO PATRONUM" });
            PosiblesRespuestas.Add(new Respuesta { Id = 22, TipoRespuesta = "Slytherin", IdPregunta = 6, Contestacion = "FINITE INCANTATEM" }); 
            PosiblesRespuestas.Add(new Respuesta { Id = 23, TipoRespuesta = "Hafflepuff", IdPregunta = 6, Contestacion = "HERBIVICUS" });
            PosiblesRespuestas.Add(new Respuesta { Id = 24, TipoRespuesta = "Ravenclaw", IdPregunta = 6, Contestacion = "LUMOS SOLEM" });
        }
        List<Casa> casas = new List<Casa>();
        public void generarCasas()
        {
            casas.Add(new Casa { Nombre = "Gryffindor", Aciertos = 0 });
            casas.Add(new Casa { Nombre = "Slytherin", Aciertos = 0 });
            casas.Add(new Casa { Nombre = "Hafflepuff", Aciertos = 0 });
            casas.Add(new Casa { Nombre = "Ravenclaw", Aciertos = 0 });
        }
        public bool isTie()
        {
            return searchRepeatedTopHouses().Count > 1 ? true : false;
        }
        public void makeQuestions(bool IsReplay) 
        {
            foreach (var pregunta in Preguntas.Where(x => x.IsTieBreaker == IsReplay))
            {
                Console.WriteLine(pregunta.Interrogante);
                List<Respuesta> respuestas = new List<Respuesta>();

                if (IsReplay)
                {
                    Console.WriteLine("Una ultima pregunta... ");
                    var repeatedHouses = searchRepeatedTopHouses();
                    foreach (var r in repeatedHouses)
                    {
                        respuestas.Add(PosiblesRespuestas.Where(x => x.TipoRespuesta == r.Nombre && x.IdPregunta == pregunta.Id).FirstOrDefault());
                    }
                }
                else
                {
                    respuestas = PosiblesRespuestas.Where(x => x.IdPregunta == pregunta.Id).ToList();
                }
                getResponse(respuestas);
            }
            hitsByHouse();
            cleanAnswers();
        }

        private void getResponse(List<Respuesta> respuestas)
        {
            bool invalidAnswer = true;
            do
            {
                Console.ForegroundColor = ConsoleColor.Red;
                foreach (var respuesta in respuestas)
                {
                    Console.WriteLine(respuesta.Contestacion);
                }
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("Escribe tu respuesta >> \n");
                string response = Console.ReadLine().Trim().ToLower();
                var isValidResponse = respuestas.Find(x => x.Contestacion.ToLower() == response);
                if (isValidResponse != null)
                {
                    saveAnswer(response);
                    invalidAnswer = false;
                }
                if (invalidAnswer == true) Console.WriteLine("Respuesta incorrecta, favor de contestar correctamente: \n");
            } while (invalidAnswer);
        }

        public List<Casa> searchRepeatedTopHouses()
        {
            var houseMaxScore = casas.OrderByDescending(x => x.Aciertos).FirstOrDefault();
            return casas.Where(x => x.Aciertos == houseMaxScore.Aciertos).ToList();
        }
        public void saveAnswer(string respuesta)
        {
            RespuestasContestadas.Add(respuesta);
        }
        public void cleanAnswers()
        {
            RespuestasContestadas.Clear();
        }
        public List<Casa> hitsByHouse()
        {
            foreach (var respuesta in RespuestasContestadas)
            {
                string current_casa = findTypeByResponse(respuesta.ToLower().ToString());
                if (current_casa == "Gryffindor") casas.Where(x => x.Nombre == current_casa).ToList().ForEach(x => x.Aciertos++);
                if (current_casa == "Slytherin") casas.Where(x => x.Nombre == current_casa).ToList().ForEach(x => x.Aciertos++);
                if (current_casa == "Hafflepuff") casas.Where(x => x.Nombre == current_casa).ToList().ForEach(x => x.Aciertos++);
                if (current_casa == "Ravenclaw") casas.Where(x => x.Nombre == current_casa).ToList().ForEach(x => x.Aciertos++);
            }
            return casas.OrderByDescending(x => x.Aciertos).ToList();
        }
        public string findTypeByResponse(string respuesta)
        {
            return PosiblesRespuestas.Where(x => x.Contestacion.ToLower().ToString() == respuesta).Select(x => x.TipoRespuesta).FirstOrDefault();
        }
    }

    public struct Pregunta
    {
        public int Id { get; set; }
        public string Interrogante { get; set; }
        public bool IsTieBreaker { get; set; }
    }

    public class Respuesta
    {
        public int Id { get; set; }
        public string Contestacion { get; set; }
        public int IdPregunta { get; set; }
        public string TipoRespuesta { get; set; }
    }

    public class Casa
    {
        public string Nombre { get; set; }
        public int Aciertos { get; set; }
    }
}
