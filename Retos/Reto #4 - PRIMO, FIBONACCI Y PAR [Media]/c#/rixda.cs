/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

 class dataNumber
 {
    

    public string whatIsThisNumber(int number)
    {
        string thisNumberIs = number + " ";
        if (isPrimo(number))
        {
            thisNumberIs += "es primo";
        }
        else
        {
            thisNumberIs += "No es primo";
        }
        if (isFibonacci(number))
        {
            thisNumberIs += ", fibonacci";
        }
        else
        {
            thisNumberIs += ",no es fibonacci";
        }

        if (isPar(number))
        {
            thisNumberIs += " y es par";
        }
        else
        {
            thisNumberIs += " y es impar";
        }



        return thisNumberIs;
    }
//
    private bool isFibonacci(int number)
    {
        int auxA = 0;
        int auxB = 1;

        if (number == 0) return true;
        while (auxA <= number && auxB <= number)
        {
            auxB = auxA + auxB;
            if (auxB == number)
            {
                return true;
            }
            auxA = auxB - auxA;

        }
        return false;
    }
    private bool isPar(int number)
    {
        if (number % 2 == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    private bool isPrimo(int number)
    {
        if (number <= 1) return false;
        if (number == 2 || number == 3) return true;
        if (isPar(number)) return false;
        for (int i = 3; i < number; i += 2)
        {
            if (number % i == 0) return false;
        }
        return true;
    }
 }