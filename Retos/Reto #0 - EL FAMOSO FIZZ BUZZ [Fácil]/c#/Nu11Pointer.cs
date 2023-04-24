var fizzBuzz = (int i) =>
{
    if (i % 3 == 0 && i % 5 == 0)
        return $"{i,3} -> fizzbuzz\n";

    if (i % 3 == 0)
        return $"{i,3} -> fizz\n";

    if (i % 5 == 0)
        return $"{i,3} -> buzz\n";

    return "";
};

foreach (var i in Enumerable.Range(1, 100))
    Console.Write($"{fizzBuzz(i)}");
