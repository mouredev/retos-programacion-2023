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

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Reto__07
{
    internal class Program
    {
        public int estudios()
        {
            while (true)
            {
                Console.WriteLine("Que te gustaria ser de mayor?(Rico,Astronauta,Profesor o medico)");
                string resestudios = Console.ReadLine();

                if (resestudios.ToUpper() == "RICO")
                {
                    return 0;
                }
                else if (resestudios.ToUpper() == "ASTRONAUTA")
                {
                    return 20;
                }
                else if (resestudios.ToUpper() == "PROFESOR")
                {
                    return 40;
                }else if(resestudios.ToUpper() == "MEDICO")
                {
                    return 60;
                }
            }
        }
        
        public int idolo()
        {

            while (true)
            {

                Console.WriteLine("¿Quien es tu idolo?(Musk, Gates, Einstein  o Gandhi)");
                string resestudios = Console.ReadLine();

                if (resestudios.ToUpper() == "MUSK")
                {
                    return 0;
                }
                else if (resestudios.ToUpper() == "GATES")
                {
                    return 20;
                }
                else if (resestudios.ToUpper() == "EINSTEIN")
                {
                    return 40;
                }
                else if (resestudios.ToUpper() == "GANDHI")
                {
                    return 60;
                }
            }
        }
        public int vivir()
        {

            while (true)
            {
                Console.WriteLine("¿¿Donde vivirias?(Rascacielos, Urbanizacion, Pueblo o Bosque)");
                string resestudios = Console.ReadLine();

                if (resestudios.ToUpper() == "RASCACIELOS")
                {
                    return 0;
                }
                else if (resestudios.ToUpper() == "URBANIZACION")
                {
                    return 20;
                }
                else if (resestudios.ToUpper() == "PUEBLO")
                {
                    return 40;
                }
                else if (resestudios.ToUpper() == "BOSQUE")
                {
                    return 60;
                }
            }
        }
        static void Main()
        {
            Program programa = new Program();
            int resultado = programa.estudios() + programa.idolo() + programa.vivir();
            string casa = "";

            if (resultado > 135)
            {
                casa = "GRYFFINDOR";
            }else if (resultado > 90 &&  resultado <= 135)
            {
                casa = "RAVENCLOW";
            }else if(resultado > 45 && resultado <= 90)
            {
                casa = "HUFFLEPUFF";
            }
            else
            {
                casa = "SLYTHERIN";
            }
                
            Console.WriteLine($"HAS SIDO SELECCIONADO PARA LA CASA {casa}");
            Console.ReadKey();


        }
    }
}