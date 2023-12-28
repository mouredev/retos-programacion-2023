for (var i = 1; i <= 100; i++)
{
    var fizzbuzzToPrint = "";
    
    fizzbuzzToPrint += i % 3 == 0 ? "fizz" : "";
    fizzbuzzToPrint += i % 5 == 0 ? "buzz" : "";

    fizzbuzzToPrint = fizzbuzzToPrint == "" ? i.ToString() : fizzbuzzToPrint;
    
    Console.WriteLine(fizzbuzzToPrint);
}