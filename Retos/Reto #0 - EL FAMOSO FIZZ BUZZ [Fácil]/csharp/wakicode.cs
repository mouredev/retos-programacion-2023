
Console.WriteLine(
    string
    .Join('\n', Enumerable
    .Range(1, 100)
    .Select(x =>
    x % 15 == 0 ? "fizzbuzz" : x % 3 == 0 ? "fizz" : x % 5 == 0 ? "buzz" : $"{x}")));