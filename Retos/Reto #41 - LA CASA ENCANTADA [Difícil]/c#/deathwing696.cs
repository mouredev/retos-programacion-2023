/*
 * Este es un reto especial por Halloween.
 * Te encuentras explorando una mansión abandonada llena de habitaciones.
 * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 * Tu misión es encontrar la habitación de los dulces.
 *
 * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 * (Tienes total libertad para ser creativo con los textos)
 *
 * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 *   Esta podría ser una representación:
 *   🚪⬜️⬜️⬜️
 *   ⬜️👻⬜️⬜️
 *   ⬜️⬜️⬜️👻
 *   ⬜️⬜️🍭⬜️
 * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 *   Si no lo aciertas no podrás desplazarte.
 * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 *   tengas que responder dos preguntas para salir de ella.
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;

namespace reto41
{
    public class Reto41
    {
        private static Dictionary<string, string> _enigmas = new Dictionary<string, string>();
        private static Dictionary<string, string> _preguntas = new Dictionary<string, string>();

        static void Main(string[] args)
        {
            Inicializa_enigmas();
            Inicializa_preguntas();

            string[,] mansion = {
            {"🚪", "⬜", "⬜", "⬜"},
            {"⬜", "👻", "⬜", "⬜"},
            {"⬜", "⬜", "⬜", "👻"},
            {"⬜", "⬜", "🍭", "⬜"}
            };

            int fila_actual = 0;
            int columna_actual = 0;

            Console.WriteLine("¡Bienvenido a la mansión abandonada! Conseguirás hallar la habitación de los dulces?");            

            while (true)
            {
                string  habitacion_actual = mansion[fila_actual, columna_actual];

                Imprime_tablero(mansion, fila_actual, columna_actual);

                if (habitacion_actual == "🍭")
                {
                    Console.WriteLine("¡Enhorabuena! ¡Has encontrado la habitación de los dulces!");
                    break;
                }

                if (habitacion_actual == "👻")
                {
                    Console.WriteLine("¡Oh no! Un fantasma te ha atrapado. Debes responder dos preguntas para salir.");

                    if (!ResponderPregunta() || !ResponderPregunta())
                    {
                        Console.WriteLine("El fantasma no está satisfecho. Has perdido.");
                        break;
                    }
                }
                else
                {
                    Console.WriteLine($"Estás en una habitación. Resuelve el enigma para avanzar.");
                    if (!ResolverEnigma())
                    {
                        Console.WriteLine("Respuesta incorrecta. No puedes avanzar.");
                        continue;
                    }
                }

                Console.Write("¿Hacia dónde quieres desplazarte? (norte/sur/este/oeste): ");
                string direccion = Console.ReadLine().ToLower();

                // Mover según la dirección
                switch (direccion)
                {
                    case "norte":
                        if (fila_actual > 0) fila_actual--;
                        break;
                    case "sur":
                        if (fila_actual < mansion.GetLength(0) - 1) fila_actual++;
                        break;
                    case "este":
                        if (columna_actual < mansion.GetLength(1) - 1) columna_actual++;
                        break;
                    case "oeste":
                        if (columna_actual > 0) columna_actual--;
                        break;
                    default:
                        Console.WriteLine("Dirección no válida. Las direcciones que puedes usar son: norte, sur, este u oeste");
                        break;
                }
            }

            Console.ReadKey();
        }

        static void Imprime_tablero(string[,] tablero, int fila_actual, int columna_actual)
        {
            string simbolo = tablero[fila_actual, columna_actual];

            tablero[fila_actual, columna_actual] = "👤";

            for (int i = 0; i < tablero.GetLength(0); i++)
            {
                for (int j = 0; j < tablero.GetLength(1); j++)
                {
                    Console.Write($"{tablero[i, j]} ");
                }

                Console.WriteLine();
            }

            tablero[fila_actual, columna_actual] = simbolo;
        }

        static void Inicializa_enigmas()
        {
            _enigmas.Add("aguja", "Enigma: ¿Qué tiene ojos y no puede ver?");
            _enigmas.Add("vela", "Enigma: Soy alto cuando joven y corto cuando viejo. ¿Qué soy?");
            _enigmas.Add("secreto", "Enigma: Todos me quieren, todos me buscan. Cuando me tienen, me quieren compartir. ¿Qué soy?");
            _enigmas.Add("oscuridad", "Enigma: Cuanto más lo miras, menos lo ves. ¿Qué es?");
            _enigmas.Add("agua", "Enigma: Siempre estoy corriendo, pero nunca me canso. ¿Qué soy?");
            _enigmas.Add("corazón", "Enigma: Si me rompes, no dejas de llorar. Si me tocas, algo moriría. ¿Qué soy?");
            _enigmas.Add("nube", "Enigma: Sin alas, voy a lugares altos. Sin piernas, me muevo rápido. ¿Qué soy?");
            _enigmas.Add("pizza", "Soy redonda como una pelota, pero todo el mundo me quiere llevar a casa. ¿Qué soy?");
            _enigmas.Add("viento", "Enigma: Puedo estar en todas partes, pero nunca puedes verme. ¿Qué soy?");
            _enigmas.Add("teclado", "Enigma: Tengo llaves pero no abro cerraduras. Tengo espacio pero no tengo habitación. ¿Qué soy?");
            _enigmas.Add("espejo", "Enigma: Aunque siempre hablo la verdad, nunca digo una palabra. ¿Qué soy?");
            _enigmas.Add("aliento", "Enigma: Puedo ser tan ligero como una pluma, pero incluso el hombre más fuerte no puede sostenerme durante mucho tiempo. ¿Qué soy?");
            _enigmas.Add("libro", "Enigma: Puedo ser leído, pero no por todos. Todos tienen uno, pero algunos prefieren usar el de otros. ¿Qué soy?");
            _enigmas.Add("futuro", "Enigma: Siempre estoy delante de ti, pero nunca puedes verme. ¿Qué soy?");
            _enigmas.Add("reloj", "Enigma: Tengo agujas pero no coso. Tengo números pero no cuento. ¿Qué soy?");
            _enigmas.Add("cebolla", "Enigma: Aunque no tengo ojos, lloro cuando cortas. ¿Qué soy?");
            _enigmas.Add("sombra", "Enigma: Puedes verme en el agua, pero nunca me mojaré. ¿Qué soy?");
        }

        static void Inicializa_preguntas()
        {
            _preguntas.Add("mapa", "Pregunta: Tengo ciudades, pero no casas. Tengo montañas, pero no árboles. Tengo agua, pero no peces. ¿Qué soy?");
            _preguntas.Add("café", "Pregunta: Soy tomado de la vaca, pero no soy leche. Tengo cuernos y me bebes caliente. ¿Qué soy?");
            _preguntas.Add("agujero", "Pregunta: Cuando más lo quitas, más grande se vuelve. ¿Qué es?");
            _preguntas.Add("nube", "Pregunta: Puedo volar sin tener alas. Puedo llorar sin tener ojos. ¿Qué soy?");
            _preguntas.Add("Incorrectamente", "Pregunta: ¿Qué palabra siempre está escrita incorrectamente?");
            _preguntas.Add("toalla", "Pregunta: Cuanto más seca, más mojada se vuelve. ¿Qué es?");
            _preguntas.Add("teléfono", "Pregunta: Hablo sin boca y oigo sin oídos. No tengo cuerpo, pero vengo de un cerdo. ¿Qué soy?");
            _preguntas.Add("copo de nieve", "Pregunta: Entra uno, el sol lo toca, y ya no está. ¿Qué es?");
        }

        static bool ResolverEnigma()
        {
            Extrae_de_diccionario(false, out string pregunta, out string solucion);

            Console.WriteLine(pregunta);
            string respuesta = Console.ReadLine().ToLower();

            return respuesta == solucion;
        }

        static bool ResponderPregunta()
        {
            Extrae_de_diccionario(true, out string pregunta, out string solucion);

            Console.WriteLine(pregunta);
            string respuesta = Console.ReadLine().ToLower();

            return respuesta == solucion;
        }

        static void Extrae_de_diccionario(bool es_pregunta, out string pregunta, out string solucion)
        {
            Random random = new Random();

            if (es_pregunta)
            {
                int numero_aleatorio = random.Next(0, _preguntas.Count);

                solucion = _preguntas.Keys.ElementAt(numero_aleatorio);
                pregunta = _preguntas[solucion];
            }
            else
            {
                int numero_aleatorio = random.Next(0, _enigmas.Count);

                solucion = _enigmas.Keys.ElementAt(numero_aleatorio);
                pregunta = _enigmas[solucion];
            }
        }
    }
}