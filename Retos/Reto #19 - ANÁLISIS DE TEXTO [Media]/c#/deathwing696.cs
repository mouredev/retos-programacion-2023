/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

using System;

namespace deathwing696
{
    public class Deathwing696
    {
        static void Main(string[] args)
        {
            string texto1 = "Lorem ipsum dolor sit amet. ";
            string texto2 = $"\r\n\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut eros ipsum. Proin tincidunt venenatis augue, tempus scelerisque nunc. Etiam in suscipit sapien, laoreet facilisis diam. Duis in scelerisque dui, sed sodales arcu. Vivamus tempor faucibus augue eu fringilla. Pellentesque tincidunt nec leo at molestie. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Praesent vulputate neque nec dui placerat rutrum accumsan id nulla. Donec a luctus urna. Suspendisse sodales erat nisi, sed fermentum erat porta id. Nullam tristique id augue vitae porta. Curabitur eu mauris finibus, dictum risus fringilla, pharetra felis. Integer orci neque, mollis ac eleifend non, imperdiet eu felis. Sed dictum quam quis nulla faucibus rutrum. Donec egestas enim est, in feugiat magna pellentesque nec. Curabitur tincidunt, velit nec eleifend malesuada, odio lorem pharetra quam, vitae laoreet libero orci at dui.\r\n\r\nAenean mattis mauris ut sollicitudin feugiat. Quisque id finibus elit, vel blandit nulla. Curabitur ullamcorper, enim at lobortis pharetra, nisi nisi sagittis turpis, vitae lacinia risus nibh ut nisl. Nunc porttitor tellus metus, et pharetra neque pharetra sit amet. Fusce ornare laoreet felis, vel dapibus purus auctor ut. Proin quis porta nunc. Mauris ac semper nulla. Sed rhoncus sapien ipsum, eget blandit mi pharetra sit amet.\r\n\r\nPellentesque malesuada sapien vitae tellus cursus condimentum. Ut eget tellus elementum, imperdiet nibh quis, malesuada dolor. Nunc molestie fringilla placerat. Suspendisse volutpat porttitor sapien vel ullamcorper. Nunc euismod vehicula felis a finibus. Duis quis hendrerit lacus. Donec euismod magna purus, sed hendrerit neque molestie at. Ut vitae dolor elit. Donec vel porttitor ex. Ut condimentum scelerisque tortor, sed accumsan nisi tempus nec. Donec id lacinia ipsum. Praesent molestie vulputate finibus. Praesent ultrices aliquam elementum. Proin convallis, ex sit amet tempor mollis, dui diam laoreet arcu, vel bibendum elit turpis ut arcu. Donec porttitor, nulla sit amet dictum eleifend, nisi lacus feugiat nunc, eu varius orci mi eu enim.\r\n\r\nIn interdum tellus eros, sit amet euismod neque ornare eu. Ut mattis aliquam lacus sed lobortis. Nam pulvinar lectus a fringilla efficitur. Donec sed mauris id mi maximus auctor. Pellentesque quis rhoncus nunc, id facilisis mauris. Vivamus porta ut nisl nec pharetra. Proin sapien tortor, pretium non tempor sed, vehicula at magna.\r\n\r\nDonec feugiat, arcu a lacinia tempus, nisl felis imperdiet risus, eu ultrices leo augue id nisi. Pellentesque pellentesque lacus id quam laoreet tempor. Praesent vel tincidunt tellus. Mauris blandit eros quam, laoreet rutrum libero congue at. Vestibulum eget porta neque, in ultrices neque. Suspendisse pretium tempor velit eu posuere. Cras pellentesque sem urna, vel iaculis mauris interdum quis. Integer cursus ultricies dolor. In consectetur nulla tristique tellus ullamcorper laoreet vel ac augue. Vestibulum porttitor tristique libero in tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. ";

            int total_letras = 0, total_palabras = 0, num_oraciones = 0, total_longitudes_palabras = 0;
            string palabra_mas_larga = "", palabra = "";

            foreach (char caracter in texto2)
            {
                if (char.IsLetterOrDigit(caracter))
                {
                    total_letras++;
                    palabra += caracter;
                }
                else if (caracter == ' '  || caracter == '\t' || caracter == '\n' || caracter == '\r' || Es_simbolo_puntuacion(caracter))
                {
                    Add_palabra_y_comprueba_palabra_mas_larga(ref total_letras, ref total_palabras, ref total_longitudes_palabras, ref palabra_mas_larga, ref palabra);
                }
                else if (caracter == '.')
                {
                    num_oraciones++;
                    Add_palabra_y_comprueba_palabra_mas_larga(ref total_letras, ref total_palabras, ref total_longitudes_palabras, ref palabra_mas_larga, ref palabra);
                }
            }

            Add_palabra_y_comprueba_palabra_mas_larga(ref total_letras, ref total_palabras, ref total_longitudes_palabras, ref palabra_mas_larga, ref palabra);

            double longitud_media = (double)total_longitudes_palabras / total_palabras;

            Console.WriteLine($"El número total de palabras es {total_palabras}");
            Console.WriteLine($"La longitud media de las palabras es {longitud_media}");
            Console.WriteLine($"El número de oraciones en el texto es {num_oraciones}");
            Console.WriteLine($"La palabra más larga es \"{palabra_mas_larga}\"");

            Console.ReadKey();
        }

        private static void Add_palabra_y_comprueba_palabra_mas_larga(ref int total_letras, ref int total_palabras, ref int total_longitudes_palabras,
                                                                      ref string palabra_mas_larga, ref string palabra)
        {
            if (total_letras > 0)
            {
                total_palabras++;
                total_longitudes_palabras += total_letras;

                if (total_letras > palabra_mas_larga.Length)
                {
                    palabra_mas_larga = palabra;
                }

                total_letras = 0;
                palabra = "";
            }
        }

        private static bool Es_simbolo_puntuacion(char caracter)
        {
            return caracter == ',' || caracter == ':' || caracter == ';' || caracter == '?' || caracter == ')' || caracter == '!';
        }
    }
}