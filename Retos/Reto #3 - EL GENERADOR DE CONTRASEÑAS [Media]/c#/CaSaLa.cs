// See https://aka.ms/new-console-template for more information



namespace reto3;
public class Reto3
{
    public enum opcionesContrasenha
    {
        mayusculas = 1,
        numeros = 2,
        simbolos = 4
    }

    public static void Main(string[] args)
    {
        Console.WriteLine("Pulse cualquier tecla para generar nuevas contraseñas. Pulse B para salir");
        while (Console.ReadKey().Key != ConsoleKey.B)
        {
            Console.WriteLine(Contrasenha(longitud: 8, opcionesContrasenha.mayusculas));
            Console.WriteLine(Contrasenha(longitud: 10, opcionesContrasenha.mayusculas | opcionesContrasenha.simbolos));
            Console.WriteLine(Contrasenha(longitud: 10, opcionesContrasenha.mayusculas | opcionesContrasenha.simbolos | opcionesContrasenha.numeros));
        }
    }

    private static string Contrasenha(int longitud, opcionesContrasenha opciones)
    {
        if (longitud > 16 || longitud < 8) throw new ArgumentOutOfRangeException("La longitud tiene que estar compendida entre 1 y 8 caracteres");
        var minusculas = (IEnumerable<char>)"abcdefghijklmnñopqrstuvwxyz";
        var mayusculas = minusculas.Select(x => (char)x.ToString().ToUpper().First());
        var numeros = (IEnumerable<char>)"0123456789";
        var simbolos = (IEnumerable<char>)"_-:;><!·$%&/()=?¿¡";

        IEnumerable<char> CaracteresValidos = minusculas;
        var logitudCaracteresValidos = CaracteresValidos.Count();
        IEnumerable<char> contrasenha = new List<char>();
        contrasenha = contrasenha.Concat<char>(CaracteresValidos.Skip<char>(Random.Shared.Next(logitudCaracteresValidos)).Take<char>(1));

        if ((opciones & opcionesContrasenha.mayusculas) == opcionesContrasenha.mayusculas)
        {
            CaracteresValidos = CaracteresValidos.Concat<char>(mayusculas);
            logitudCaracteresValidos = CaracteresValidos.Count<char>();
            contrasenha = contrasenha.Concat<char>(CaracteresValidos.Skip<char>(Random.Shared.Next(logitudCaracteresValidos)).Take<char>(1));
        }


        if ((opciones & opcionesContrasenha.numeros) == opcionesContrasenha.numeros)
        {
            CaracteresValidos = CaracteresValidos.Concat<char>(numeros);
            logitudCaracteresValidos = CaracteresValidos.Count<char>();
            contrasenha = contrasenha.Concat<char>(CaracteresValidos.Skip<char>(Random.Shared.Next(logitudCaracteresValidos)).Take<char>(1));
        }

        if ((opciones & opcionesContrasenha.simbolos) == opcionesContrasenha.simbolos)
        {
            CaracteresValidos = CaracteresValidos.Concat<char>(simbolos);
            logitudCaracteresValidos = CaracteresValidos.Count<char>();
            contrasenha = contrasenha.Concat<char>(CaracteresValidos.Skip<char>(Random.Shared.Next(logitudCaracteresValidos)).Take<char>(1));
        }


        while (contrasenha.Count() < longitud)
        {

            contrasenha = contrasenha.Concat<char>(CaracteresValidos.Skip<char>(Random.Shared.Next(logitudCaracteresValidos)).Take<char>(1));
        }

         contrasenha
        .Select(x => (x, Random.Shared.Next()))
        .OrderBy(tuple => tuple.Item2)
        .Select(tuple => tuple.Item1)
        .ToArray();
        return string.Join(null, contrasenha);
    }
}