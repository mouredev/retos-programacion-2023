/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

using System;
using static Soluciones.Reto_07;

namespace Soluciones
{
    class Reto_07
    {
        static List<Questions> questions;
        static List<Answers> answer;
        private enum Casas { Gryffindor, Slytherin, Hufflepuff , Ravenclaw }
        
        

        public class Questions
        {
            public int Id { get; set; }
            public string Question { get; set; }
        }

        public class Answers
        { 
            public int Id { get; set; } 
            public string Answer { get; set;}
            public int Option { get; set; }
            public int QuestionId { get; set; }
        }

        static public void Main()
        {
            int Gryffindor = 0, Slytherin = 0, Hufflepuff = 0, Ravenclaw = 0;
            Init();
            List<Answers> Answer;
            foreach (var _question in questions)
            {
                Console.WriteLine(_question.Question);
                Answer = answer.Where(x => x.QuestionId == _question.Id).ToList();
                
                foreach (var _answer in Answer)
                {
                    Console.WriteLine(string.Concat(" ", _answer.Option, " - ", _answer.Answer));
                }

                int n;
                while (!int.TryParse(Console.ReadLine(), out n) || n > 4)
                {
                    Console.WriteLine("You entered an invalid number");
                }

                switch (n)
                {
                    case 1:
                        Gryffindor++;
                        break;
                    case 2:
                        Slytherin++;
                        break;
                    case 3:
                        Hufflepuff++;
                        break;
                    case 4:
                        Ravenclaw++;
                        break;
                    default:
                        break;
                }
            }
            Console.Clear();

            Console.WriteLine("El sombrero seleccionador a elejido......");
            if (Gryffindor > Slytherin && Gryffindor > Hufflepuff && Gryffindor > Ravenclaw)
            {
                Console.WriteLine(string.Concat(Casas.Gryffindor, "!!!!"));
            }
            else if (Slytherin > Gryffindor && Slytherin > Hufflepuff && Slytherin > Ravenclaw)
            {
                Console.WriteLine(string.Concat(Casas.Slytherin,"!!!!"));
            }
            else if (Hufflepuff > Slytherin && Hufflepuff > Gryffindor && Hufflepuff > Ravenclaw)
            {
                Console.WriteLine(string.Concat(Casas.Hufflepuff, "!!!!"));
            }
            else
            {
                Console.WriteLine(string.Concat(Casas.Ravenclaw, "!!!!"));
            }
        }

        private static void Init() 
        {
            questions = new List<Questions>();
            questions.Add(new Questions { Id = 1, Question = "¿A qué clase te gustaría asistir más?" });
            questions.Add(new Questions { Id = 2, Question = "¿Qué animal llevarías al colegio?" });
            questions.Add(new Questions { Id = 3, Question = "Si hablamos de aspectos positivos de tu personalidad ¿Cuál de estas opciones te define más?" });
            questions.Add(new Questions { Id = 4, Question = "¿¿Que te gusta más?" });
            questions.Add(new Questions { Id = 5, Question = "¿En dónde pasarías tu tiempo libre en Hogwarts?" });

            answer = new List<Answers>();
            answer.Add(new Answers { Id = 1,  Option = 1 , Answer = "D.C.A.O.", QuestionId = 1 });
            answer.Add(new Answers { Id = 2,  Option = 2 , Answer = "Adivinación.", QuestionId = 1 });
            answer.Add(new Answers { Id = 3,  Option = 3 , Answer = "Pociones.", QuestionId = 1 });
            answer.Add(new Answers { Id = 4,  Option = 4 , Answer = "Cuidado de Criaturas Mágicas", QuestionId = 1 });
                                              
            answer.Add(new Answers { Id = 5,  Option = 1 , Answer = "Sapo.", QuestionId = 2 });
            answer.Add(new Answers { Id = 6,  Option = 2 , Answer = "Gato.", QuestionId = 2 });
            answer.Add(new Answers { Id = 7,  Option = 3 , Answer = "Lechuza.", QuestionId = 2 });
            answer.Add(new Answers { Id = 8,  Option = 4, Answer = "No llevaría ninguna.", QuestionId = 2 });
                                              
            answer.Add(new Answers { Id = 9,  Option = 1 , Answer = "Generoso y perseverante.", QuestionId = 3 });
            answer.Add(new Answers { Id = 10, Option = 2 ,  Answer = "Leal y determinado.", QuestionId = 3 });
            answer.Add(new Answers { Id = 11, Option = 3 ,  Answer = "Distinguido y diplomático.", QuestionId = 3 });
            answer.Add(new Answers { Id = 12, Option = 4,  Answer = "Creativo e intelectual.", QuestionId = 3 });
                                              
            answer.Add(new Answers { Id = 13, Option = 1 ,  Answer = "Viento.", QuestionId = 4 });
            answer.Add(new Answers { Id = 14, Option = 2 ,  Answer = "Prado.", QuestionId = 4 });
            answer.Add(new Answers { Id = 15, Option = 3 ,  Answer = "Fogata", QuestionId = 4 });
            answer.Add(new Answers { Id = 16, Option = 4,  Answer = "Laguna", QuestionId = 4 });
                                              
            answer.Add(new Answers { Id = 17, Option = 1 ,  Answer = "En los terrenos.", QuestionId = 5 });
            answer.Add(new Answers { Id = 18, Option = 2 ,  Answer = "En los invernaderos.", QuestionId = 5 });
            answer.Add(new Answers { Id = 19, Option = 3 ,  Answer = "En la biblioteca.", QuestionId = 5 });
            answer.Add(new Answers { Id = 20, Option = 4,  Answer = "En la Sala común.", QuestionId = 5 });

        }

    }
}


