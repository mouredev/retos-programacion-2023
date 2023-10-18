/* Reto #5: HOLA MUNDO
 * 
 * Enunciado:
 * 
 *  Escribe un !Hola Mundo! en todos los lenguajes de programación que puedas
 *   
 */

using System.Linq;
using System;

Console.Write("\nReto #5: HOLA MUNDO");
Console.Write("\n-------------------------------\n\n");

Console.Write(HelloWorldExotico() + "\n"); // Salida -> "hello world!"

string HelloWorldExotico()
{
    string lorem = "Lorem ipsum dolor sit amet, consectetur | adipiscing elit. Donec tempus dui mi, viverra vulputate | dolor hendrerit ac. Curabitur porttitor enim | nec turpis porttitor, eget egestas | ligula mattis. Nullam nec augue purus. | Morbi maximus et libero at posuere. Nunc sodales nisi | non diam ultrices, sed facilisis enim | aliquam. Sed et nisl sed arcu accumsan volutpat eu |  quis sem. Vestibulum consectetur tempor quam, | id commodo risus | aliquam in. || Nulla rhoncus risus vitae tortor hendrerit, vel | bibendum nibh facilisis. Sed aliquet, nisl eu | euismod tincidunt, purus arcu elementum massa, | vel ullamcorper ex | ipsum a lectus. Quisque id magna vel | ipsum sollicitudin | vulputate vitae vel ante. Suspendisse nulla | dolor, condimentum ut rutrum vel, pulvinar non odio. Duis | scelerisque nibh quis diam maximus rhoncus. | Lorem ipsum dolor sit | amet, consectetur | adipiscing.";

    return new string(
      String.Concat(
        String.Concat(
          lorem
            .Split('|')
            .Select(x => x.Trim())
            .Select(x => x.Length > 0 ? x.Split().Count() : 0)
            .Select(x => x == 3 ? "f" : x == 9 ? "c" : x.ToString()))
        .Chunk(2)
        .Select(x => $@"\u00{String.Concat(x)}"))
      .Split(new[] { @"\u" }, StringSplitOptions.RemoveEmptyEntries)
      .Select(c => (char)Convert.ToInt32(c, 16))
      .ToArray());
}