using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Reto7
{
    internal class Program
    {
        public class Questions
        {
            public string quest { get; set; } 
            public List<Answers> answersList { get; set; }
        }
        public class Answers
        {
            public string answer { get; set; }
            public List<AnswerProperty> propertyList { get; set; }            
        }
        public class AnswerProperty
        {
            public Property property { get; set; }
            public int propertyValue { get; set; }

        }
        public enum Property 
        {
            Coraje,
            Trabajo,
            Sabiduría,
            Ambicion

        }

        public class Valors
        {
            public Property property{get; set;}
            public int value{get; set;}
}
        public class Gamer
        {
            public string name { get; set; }
            public int questionAnswered { get; set; }
            public List<Valors> ValorsList { get; set; }
        }



        public static Gamer _jugador = new Gamer();
        public static bool validateAnswer = false;
        public static int answervalue;
        static void Main(string[] args)
        {
            var questions = GetQuestions();
            
            _jugador.ValorsList = new List<Valors>();
            MakeQuestion(questions);
            Result();
            Console.ReadLine();
        }

        /// <summary>
        /// Process to show questions and get answer
        /// </summary>
        /// <param name="questionList"></param>
        public static void MakeQuestion(List<Questions> questionList)
        {
            Console.WriteLine("****************************");
            Console.WriteLine("¿Cual es tu nombre?");
            _jugador.name = Console.ReadLine();
            Console.WriteLine($"Hola {_jugador.name}. Empiezan las preguntas, responde marcando el numero correcto, 0 para salir o terminar");

            int questionCounter = 0;
            Console.WriteLine("****************************");
            foreach (var questions in questionList)
            {
                questionCounter++;
                Console.ForegroundColor= ConsoleColor.Blue;
                Console.WriteLine();
                Console.WriteLine($"{questionCounter} - {questions.quest}");
                Console.ForegroundColor = ConsoleColor.Green;
                int answercounter = 0;
                foreach (var answer in questions.answersList)
                {
                    answercounter++;
                    Console.WriteLine($"{answercounter} - {answer.answer}");
                }
                double number;
                while (!validateAnswer)
                {
                    
                    if (double.TryParse(Console.ReadLine(), out number) && number >= 0 && number <= 4)
                    {
                        validateAnswer = true;
                        answervalue = Convert.ToInt32(number);
                        if (answervalue == 0)
                            break;

                        _jugador.questionAnswered++;
                        Valors aux = new Valors();
                        ProcessAnswer(questions.answersList);
                    }
                    else
                    {
                        Console.WriteLine("El número ingresado no es válido. entre 0 y 4 por favor");
                    }
                }
                if (answervalue == 0)
                    break;
                validateAnswer = false;
            }           
        }
        


        /// <summary>
        /// whow result
        /// </summary>
        public static void Result()
        {
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine();
            Console.WriteLine("****************************************************");
            Console.WriteLine($"{_jugador.name} has contestado {_jugador.questionAnswered} preguntas");
            _jugador.ValorsList = _jugador.ValorsList.OrderByDescending(s=>s.value).ToList();
            foreach (var valores in _jugador.ValorsList)
            {
                Console.WriteLine($"{valores.property} - {valores.value}");
            }
            var k = _jugador.ValorsList.First();
            if (k.property == Property.Coraje)
                Console.WriteLine($"Tu casa correcta sería: Gryffindor");
            if (k.property == Property.Trabajo)
                Console.WriteLine($"Tu casa correcta sería: Hufflepuff");
            if (k.property == Property.Sabiduría)
                Console.WriteLine($"Tu casa correcta sería: Ravenclaw");
            if (k.property == Property.Ambicion)
                Console.WriteLine($"Tu casa correcta sería: Slytherin");
        }


        /// <summary>
        /// Process answer
        /// </summary>
        /// <param name="anwers"></param>
        public static void ProcessAnswer(List<Answers> anwers) 
        {
            int result = answervalue;


            foreach (var propertyy in anwers[result -1].propertyList)
            {
                var x = _jugador.ValorsList.Select(s => s.property == propertyy.property).FirstOrDefault();
                if (!x)
                {
                    Valors aux = new Valors()
                    {
                        property = propertyy.property,
                        value = propertyy.propertyValue
                    };
                    _jugador.ValorsList.Add(aux);
                }
                else
                {
                    var s = _jugador.ValorsList.Where(d => d.property == propertyy.property).FirstOrDefault();
                    s.value = propertyy.propertyValue;
                    _jugador.ValorsList.Remove(s);
                    _jugador.ValorsList.Add(s);
                }
            }
        }






        public static List<Questions> GetQuestions()
        { 
            List<Questions> returnvalue = new List<Questions>();
            returnvalue.Add(new Questions()
            { 
                quest = "¿Qué harías si te encontraras con un obstáculo importante en tu camino hacia una meta?",
                answersList = new List<Answers>()
                {
                    new Answers()
                    { 
                        answer = "Renunciaría y buscaría otra cosa que hacer.",
                        propertyList = new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 1
                            },
                            new AnswerProperty() 
                            {
                                property = Property.Trabajo,
                                propertyValue = 1
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 2
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 1
                            }
                        }
                    },
                    new Answers()
                    {
                        answer = "Trataría de encontrar una manera de superarlo, pero si no funciona, me daría por vencido.",
                        propertyList = new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 2
                            },
                            new AnswerProperty()
                            {
                                property = Property.Trabajo,
                                propertyValue = 3
                            }
                            ,
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 3
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 2
                            }
                        }
                    },
                    new Answers()
                    {
                        answer = "Intentaría superar el obstáculo, aunque me lleve tiempo y esfuerzo extra.",
                        propertyList = new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 4
                            },
                            new AnswerProperty()
                            {
                                property = Property.Trabajo,
                                propertyValue = 5
                            }
                            ,
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 4
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 3
                            }
                        }
                    },
                                        new Answers()
                    {
                        answer = "Me tomaría un tiempo para reflexionar sobre cómo superar el obstáculo y buscaría la ayuda de otras personas si es necesario.",
                        propertyList = new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 5
                            },
                            new AnswerProperty()
                            {
                                property = Property.Trabajo,
                                propertyValue = 4
                            }
                            ,
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 5
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 5
                            }
                        }
                    }
                } 
            });

            returnvalue.Add(new Questions()
            {
                quest = "¿Qué tan dispuesto estás a tomar riesgos en tu vida?",
                answersList= new List<Answers>() 
                {
                    new Answers()
                    {
                        answer = "No estoy dispuesto a correr riesgos. Prefiero la estabilidad y la seguridad.",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            { 
                                property = Property.Coraje,
                                propertyValue = 1
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 2
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 3
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 4
                            }
                        }
                    },
                   new Answers()
                    {
                        answer="Tomo riesgos solo si estoy seguro de que puedo manejar las consecuencias.",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 2
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 3
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 4
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 3
                            }
                        }
                    },
                    new Answers()
                    {
                        answer="c) Estoy dispuesto a correr riesgos si creo que la recompensa vale la pena.",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 4
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 4
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 3
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 4
                            }
                        }
                    },
                                      new Answers()
                    {
                        answer="Estoy dispuesto a correr riesgos si creo que tengo la oportunidad de aprender algo nuevo o experimentar algo emocionante.",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 5
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 5
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 2
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 5
                            }
                        }
                    }
                }
            });

            returnvalue.Add(new Questions()
            {
                quest = "¿Cómo manejas las críticas y los errores?",
                answersList = new List<Answers>()
                {
                    new Answers()
                    {
                        answer = "Me desanimo fácilmente y me siento mal por mucho tiempo. ",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 1
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 1
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 2
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 1
                            }
                        }
                    },
                   new Answers()
                    {
                        answer="Las críticas y los errores me molestan, pero trato de aprender de ellos.",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 2
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 3
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 4
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 2
                            }
                        }
                    },
                                       new Answers()
                    {
                        answer = "Las críticas y los errores son una oportunidad para mejorar y crecer.",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 4
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 4
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 5
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 4
                            }
                        }
                    },
                    new Answers()
                    {
                        answer = "Las críticas y los errores son solo parte del camino hacia el éxito.",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 5
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 5
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 4
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 5
                            }
                        }
                    }
                }
            });
            returnvalue.Add(new Questions()
            {
                quest = "¿Cómo te enfrentas a los desafíos?",
                answersList = new List<Answers>()
                {
                    new Answers()
                    {
                        answer = "Me rindo facilmente",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 1
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 1
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 2
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 1
                            }
                        }
                    },
                   new Answers()
                    {
                        answer="Busco ayuda inmediatamente",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 2
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 2
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 3
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 2
                            }
                        }
                    },
                    new Answers()
                    {
                        answer="Trato de encontrar una solución por mi cuenta.",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 3
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 3
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 4
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 3
                            }
                        }
                    },
                    new Answers()
                    {
                        answer="Me enfrento al desafío directamente sin temor.",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 5
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 5
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 3
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 4
                            }
                        }
                    }
                }
            });

            returnvalue.Add(new Questions()
            {
                quest = "¿Cómo buscas aprender cosas nuevas?",
                answersList = new List<Answers>()
                {
                    new Answers()
                    {
                        answer = "No me interesa aprender cosas nuevas.",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 1
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 2
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 2
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 1
                            }
                        }
                    },
                   new Answers()
                    {
                        answer="Prefiero que me enseñen directamente.",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 2
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 1
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 4
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 3
                            }
                        }
                    },
                    new Answers()
                    {
                        answer = "Leo libros o veo tutoriales en línea.",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 4
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 5
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 3
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 3
                            }
                        }
                    },
                    new Answers()
                    {
                        answer = "xperimento y pruebo cosas nuevas por mi cuenta.",
                        propertyList= new List<AnswerProperty>()
                        {
                            new AnswerProperty()
                            {
                                property = Property.Coraje,
                                propertyValue = 3
                            },
                            new AnswerProperty()
                            {
                                property= Property.Trabajo,
                                propertyValue = 5
                            },
                            new AnswerProperty()
                            {
                                property = Property.Sabiduría,
                                propertyValue = 4
                            },
                            new AnswerProperty()
                            {
                                property = Property.Ambicion,
                                propertyValue = 5
                            }
                        }
                    }
                }
            });
            return returnvalue;
        }
    }
}
