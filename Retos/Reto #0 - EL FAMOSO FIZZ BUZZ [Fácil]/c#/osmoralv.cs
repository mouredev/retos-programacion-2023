bool divisibleByThree;
bool divisibleByFive;

string output;

for (int i = 1; i <= 100; i++)
{
    divisibleByThree = (i % 3) == 0;
    divisibleByFive = (i % 5) == 0;

    if (divisibleByThree && divisibleByFive)
    {
        output = "FizzBuzz";

    } else if (divisibleByThree)
    {
        output = "Fizz";

    } else if (divisibleByFive)
    {
        output = "Buzz";

    } else
    {
        output = i.ToString();

    }

    Console.WriteLine($"{i} - {output}");

}