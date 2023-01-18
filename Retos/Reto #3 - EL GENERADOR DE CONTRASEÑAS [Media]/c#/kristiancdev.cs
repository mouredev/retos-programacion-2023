string UpperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
string LowerLetters = "abcdefghijklmnopqrstuvwxyz";
string Numbers = "0123456789";
string SpecialCharacters = "!@#$%^&*()?";

List<string> YesChoices = new List<string> { "SI", "S", "YES", "Y" };
List<string> NoChoices = new List<string> { "NO", "N" };

int Length = ValidateLength("Introduzca la longitud de la contraseña:");
bool ValidLength = ValidateYesNo("Validar la longitud Si/No: ");
bool IncludeCapitals = ValidateYesNo("Incluir mayúsculas Si/No: ");
bool IncludeLowercase = ValidateYesNo("Incluir minúsculas Si/No: ");
bool IncludeNumbers = ValidateYesNo("Incluir números Si/No: ");

string GeneratedPassword = GeneratePassword(Length, ValidLength, IncludeCapitals, IncludeLowercase, IncludeNumbers);
Console.WriteLine($"La contraseña generada es: {GeneratedPassword}");

int ValidateLength(string Question)
{
  while (true) {
    int length = 0;

    try
    {
      Console.WriteLine(Question);
      length = int.Parse(Console.ReadLine());
    }
    catch (Exception)
    {
      Console.WriteLine("Debes escribir un número.");
      continue;
    }

    if (length < 0) {
      Console.WriteLine("Debes escribir un número positivo.");
      continue;
    } else {
      return length;
    }
  }
}

bool ValidateYesNo(string Question)
{
  while (true)
  {
    Console.WriteLine(Question);
    string answer = Console.ReadLine();

    if (YesChoices.Contains(answer.ToUpper())) {
      return true;
    } else if (NoChoices.Contains(answer.ToUpper())) {
      return false;
    } else {
      Console.WriteLine("Debes escribir Si o No.");
      continue;
    }
  }
}

string GeneratePassword(int Size, bool ValidSize, bool Capital, bool Lower, bool Number)
{
  if (ValidSize)
  {
    if (!(Size > 8 && Size <= 16))
    {
      Console.WriteLine("La longitud no cumple el parámetro de longitud recomendada.");
      return "";
    }
  }

  var rand = new Random();

  string Password = "";
  string Characters = "";

  Characters += SpecialCharacters;
  Characters += Capital ? UpperLetters : "";
  Characters += Lower ? LowerLetters : "";
  Characters += Number ? Numbers : "";

  for (int i = 0; i <= Size; i++)
  {
    string randomCharacter = Characters.Substring(rand.Next(1, Characters.Count()), 1);
    Password += randomCharacter;
  }
  
  return Password;
}