using System;
public class Reto0
{
    public static void Main(string[] args)
    {
       for(int i = 1; i <= 100; i++){
           string res = string.Empty;
           if(i % 3 == 0)
            res += "Fizz";
           if(i % 5 == 0)
            res +="Buzz";
           Console.WriteLine(res != string.Empty ? res : i);
       }
    }
}