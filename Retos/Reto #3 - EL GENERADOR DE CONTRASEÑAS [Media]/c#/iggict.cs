
using System;

Console.Write("\nGENERADOR ALEATORIO DE CONTRASEÑAS");
Console.Write("\n----------------------------------\n");

Console.Write("\nParametros de entrada:\n");

Console.Write("\n* Número de caracteres (8-16)");
Console.Write("\n* Permitir mayusculas (s/n)");
Console.Write("\n* Permitir dígitos (s/n)");
Console.Write("\n* Permitir símbolos (s/n)\n");

Console.Write("\nEjemplos:\n");

Console.Write("\nEj01 => 8,s,s,n");
Console.Write("\nEj02 => 9,n,s,n\n");

do
{
    PasswordGenerator pwGenerator;

    Console.Write("\nIntroduce los parámetros separados por comas: ");

    string paramString = Console.ReadLine() ?? "";

    var paramArray = paramString.Split(',');

    try
    {
        pwGenerator = new PasswordGenerator(
            length: (paramArray.Length >= 1 ? Int32.Parse(paramArray[0]) : 8),
            isCaseAllowed: paramArray.Length >= 2 && paramArray[1].Equals("s", StringComparison.OrdinalIgnoreCase),
            isDigitAllowed: paramArray.Length >= 3 && paramArray[2].Equals("s", StringComparison.OrdinalIgnoreCase),
            isSpecialCharAllowed: paramArray.Length >= 4 && paramArray[3].Equals("s", StringComparison.OrdinalIgnoreCase)
        );
    }
    catch (Exception)
    {
        Console.WriteLine($"\nERROR: Los parámetros de entrada no son válidos");
        continue;
    }

    Console.WriteLine($"\nPASSWORD: {pwGenerator.CreatePassword()}");

} while (true);

public class PasswordGenerator
{

    const int MIN_LENGTH = 8;
    const int MAX_LENGTH = 16;

    private readonly int length;
    private readonly bool isCaseAllowed;
    private readonly bool isDigitAllowed;
    private readonly bool isSpecialCharAllowed;

    public PasswordGenerator(int length, bool isCaseAllowed = false, bool isDigitAllowed = false, bool isSpecialCharAllowed = false)
    {

        if (length < MIN_LENGTH)
            this.length = MIN_LENGTH;
        else if (length > MAX_LENGTH)
            this.length = MAX_LENGTH;
        else
            this.length = length;

        this.isCaseAllowed = isCaseAllowed;
        this.isDigitAllowed = isDigitAllowed;
        this.isSpecialCharAllowed = isSpecialCharAllowed;

        Console.WriteLine($"\nLongitud={this.length}, Mayúsculas={this.isCaseAllowed}, Números={this.isDigitAllowed}, Símbolos={this.isSpecialCharAllowed} ");
    }

    public string CreatePassword()
    {
        const string CHARS = "abcdefghijklmnopqrstuvwxyz";
        const string DIGITS = "1234567890";
        const string SPECIAL_CHARS = "!@#$%&*+-?()<>";

        string allowedChars = CHARS
            + (this.isCaseAllowed ? CHARS.ToUpper() : "")
            + (this.isDigitAllowed ? DIGITS : "")
            + (this.isSpecialCharAllowed ? SPECIAL_CHARS : "");

        string pw = string.Empty;

        Random random = new();

        for (int i = 0; i < this.length; i++)
        {
            int idx = random.Next(0, allowedChars.Length);
            pw += allowedChars[idx];
        }

        return pw;
    }

}

