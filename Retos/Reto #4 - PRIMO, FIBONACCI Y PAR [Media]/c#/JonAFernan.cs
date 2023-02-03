namespace EjerciciosSueltos;

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

class Program
{
    static void Main(string[] args)
   {
        primeFiboEvenCheck(97);
        primeFiboEvenCheck(55);
        primeFiboEvenCheck(12);
   }


    static void primeFiboEvenCheck(int number)
    {
        string prime = PrimeCheck(number) ?"es primo": "no es primo";
        string fibo = FiboChek(number) ?" es fibonacci": "no es fibonacci";
        string even = EvenChek(number) ?"es par": "no es par";
        Console.WriteLine($"El {number} {prime}, {fibo} y {even}");
    }

    static bool PrimeCheck (int number)
    {
        if(number < 2) return false;

        for (int i = 2; i < number; i++)
        {
            if(number%i == 0) return false;
        }
        
        return true;
    }
    
    static bool FiboChek (int number)
    {
        int a = 0 ; 
        int b = 1;
        if (number == a || number == b) return true;
        int c = a+b;
        while(c <= number)
        {
            if(c == number) return true;
            a = b;
            b = c;
            c = a+b;
            
        }
        return false;
    }

    static bool EvenChek (int number)
    {
        return number%2 == 0 ? true:false;
    }
}



