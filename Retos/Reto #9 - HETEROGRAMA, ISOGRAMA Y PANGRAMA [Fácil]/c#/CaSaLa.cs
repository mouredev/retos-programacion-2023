// See https://aka.ms/new-console-template for more information



using System.Text.RegularExpressions;

namespace reto9;
public class reto9
{
    
    public static void Main(string[] args)
    {
        var algograma = "asdfg ";
        Console.WriteLine($"{algograma} es Isograma: {EsIsograma(algograma)}");
         algograma = "aaasdfg ";
        Console.WriteLine($"{algograma} es Isograma: {EsIsograma(algograma)}");
         algograma = "aabb e r e r ";
        Console.WriteLine($"{algograma} es Isograma: {EsIsograma(algograma)}");
        algograma = "aabb e r e r ";
        Console.WriteLine($"{algograma} es Heterograma: {EsHeterograma(algograma)}");
        algograma = "admets";
        Console.WriteLine($"{algograma} es Heterograma: {EsHeterograma(algograma)}");
        algograma = "admets";
        Console.WriteLine($"{algograma} es Heterograma: {EsHeterograma(algograma)}");

        Console.WriteLine("Escribe una frase");
        var linea = Console.ReadLine();
        Console.WriteLine($"{linea} es Isograma: {EsIsograma(linea)}");
        Console.WriteLine($"{linea} es Heterograma: {EsHeterograma(linea)}");
        Console.WriteLine($"{linea} es Pangrama: {EsPangrama(linea)}");

    }

    public static bool EsIsograma(string texto)
    {
        if (string.IsNullOrWhiteSpace(texto)) return false;                       
        var a= texto.ToLower().Where(n => Regex.IsMatch(texto,"[a-z]") && n!=' ').GroupBy(n => n).Select(n => new { n.Key, Count = n.Count() });
        if ((a?.Count() ?? 0) == 0) return false;
        return a.All(n=> n.Count == a.First().Count);
        
    }

    public static bool EsHeterograma(string texto)
    {
        if (string.IsNullOrWhiteSpace(texto)) return false;
        var a = texto.ToLower().Where(n => Regex.IsMatch(texto, "[a-z]") && n != ' ').GroupBy(n => n).Select(n => new { n.Key, Count= n.Count() });
        if ((a?.Count()??0)==0) return false;
        return a.All(n => n.Count == 1);

    }

    public static bool EsPangrama(string texto)
    {
        if (string.IsNullOrWhiteSpace(texto)) return false;
        var a = texto.ToLower().Where(n => Regex.IsMatch(texto, "[a-z]") && n != ' ').GroupBy(n => n).Select(n => new { n.Key, Count = n.Count() });
        return "abcdefghijklmnñopqrstuvwxyzüáéíóú".Except(a.Select(n=> n.Key)).Count()==0;
    }


}