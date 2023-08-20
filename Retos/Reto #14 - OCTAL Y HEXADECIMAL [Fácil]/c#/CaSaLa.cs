// See https://aka.ms/new-console-template for more information



using System.Text.RegularExpressions;

namespace reto14;
public class reto14
{
    
    public static void Main(string[] args)
    {
        for (int i = 0; i < 1000; i++)
        {
            Console.WriteLine(ConvertirOctal(i));
        }
        
        for (int i = 0; i < 1000; i++)
        {
            Console.WriteLine(ConvertirHexadecimal(i));
        }
    }

    public static string ConvertirOctal(int numeroAConvertir)
    {
        return BaseConverter(numeroAConvertir, 8);
    }

    public static string ConvertirHexadecimal(int numeroAConvertir)
    {
        return BaseConverter(numeroAConvertir, 16);
    }

    private static string BaseConverter(int numeroAConvertir, int numBase)
    {
        if (numeroAConvertir == 0) return 0.ToString();

        var digito = "0123456789ABCDEF".ToCharArray();
        var resultado = "";

        var restoPorConvertir = numeroAConvertir;
        while (restoPorConvertir > 0)
        {
            resultado = digito[restoPorConvertir % numBase] + resultado;
            restoPorConvertir /= numBase;
        }

        return resultado;
    }
}