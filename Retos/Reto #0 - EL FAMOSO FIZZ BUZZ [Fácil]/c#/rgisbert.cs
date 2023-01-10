string fizzBuzz(int n)
{
    bool isMultipleOf3 = n % 3 == 0;
    bool isMultipleOf5 = n % 5 == 0;

    if (isMultipleOf3 && isMultipleOf5) return "fizzbuzz";
    if (isMultipleOf3) return "fizz";
    if (isMultipleOf5) return "buzz";
    return n.ToString();
}

for(int i = 1; i <= 100; i++)
{
    Console.WriteLine( fizzBuzz(i) );
}
