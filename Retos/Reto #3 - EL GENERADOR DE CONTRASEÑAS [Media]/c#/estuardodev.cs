/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
class Program
{
    static Random random = new Random();

    public static void Main(String[] args)
    {
        Console.WriteLine("------------------------------------------------------");
        Console.WriteLine("--             Generador de Contraseñas             --");
        Console.WriteLine("--              Hecho por @estuardodev              --");
        Console.WriteLine("--                   -------------                  --");
        Console.WriteLine("--        Antes debemos configurar unas cosas       --");
        Console.WriteLine("------------------------------------------------------");

        Console.Write("\nIngresa la longitud de tu contraseña (Entre 8 y 16): ");
        int longitud = Convert.ToInt32(Console.ReadLine());
        if (longitud < 8 || longitud > 16) { Console.WriteLine("Ingresa valores válidos por favor."); Environment.Exit(0); }

        int con_sin_mayusculas = pregunta("mayúsculas");

        int con_sin_numeros = pregunta("números");

        int con_sin_simbolos = pregunta("símbolos");

        Console.WriteLine("\nTu cotraseñas nueva es: " + generadorPassword(longitud, con_sin_mayusculas, con_sin_numeros, con_sin_simbolos) 
            + "\n\nNUNCA COMPARTAS TU CONTRASEÑA CON NADIE.");

    }

    public static string generadorPassword(int longitud, int _mayusculas, int _numeros, int _simbolos)
    {
        string password = "";
        string pilar;

        while (password.Length < longitud)
        {
            if(_mayusculas == 1)
            {
                pilar = Convert.ToString(abecedario(true));
                password = password + pilar;
            }
            else
            {
                pilar = Convert.ToString(abecedario(false));
                password = password + pilar;
            }
            if (_numeros == 1)
            {
                pilar = Convert.ToString(numeros());
                password = password + pilar;
            }
            if (_simbolos == 1)
            {
                pilar = Convert.ToString(caracteres());
                password = password + pilar;
            }
        }
        return password;
    }

    public static int pregunta(string palabra)
    {
        Console.Write("\n¿Deseas "+palabra+"?\n[1] - SI\n[0] - NO\nRespuesta: ");
        int dato = Convert.ToInt32(Console.ReadLine());
        if (dato < 0 || dato > 1) { Console.WriteLine("Ingresa valores válidos por favor."); Environment.Exit(0); }

        return dato;
    }

    public static char abecedario(bool mayuscula)
    {
        string ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
        string abc = "abcdefghijklmnñopqrstuvwxyz";

        if (mayuscula)
        {
            string ABCabc = ABC + abc;
            return ABCabc[random.Next(0, ABCabc.Length)];
        }
        else
        {
            return abc[random.Next(0, abc.Length)];
        }
    }

    public static char numeros()
    {
        string nums = "0123456789";
        return nums[random.Next(0, nums.Length)];
    }

    public static char caracteres()
    {
        string caracteres = "!{}+¿°!#%$%/&(&()/?¡_.,.-{+}¿/*-+.@";
        return caracteres[random.Next(0, caracteres.Length)];
    }
}