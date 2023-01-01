int[] listOfNumbers = Enumerable.Range(1, 100).ToArray();

foreach (int valueNumber in listOfNumbers)
{
  string valueString = "";

  if (valueNumber % 3 == 0)
    valueString += "Fizz";

  if (valueNumber % 5 == 0)
    valueString += "Buzz";

  Console.WriteLine(
    valueString == string.Empty
      ? valueNumber
      : valueString
  );
}

