public class noorthex {

    public String comprobador(int num)
    {
        // NUMEROS PRIMOS
        
        String mensajePrimo = "";

        mensajePrimo = "Es primo";

        if (num == 0 || num == 1 || num == 4) 
        {
            mensajePrimo = "No es primo";
        }
        for (int x = 2; x < num / 2; x++) 
        {
            if (num % x == 0)
            {
                mensajePrimo = "No es primo";
            }
        }
        // FIBONACCI

        int aux = 1;
        int fib = 0;
        String mensajeFibo = "";
        if(num>0)
        {
            for(int x=0;x<46;x++) // 46 porque después de ese numero pasan a ser negativos.
            {
                if(num == aux)
                {
                    mensajeFibo = "es fibonacci";
                    break;
                }
                else
                {
                    aux += fib; 
                    fib = aux - fib;
                    mensajeFibo = "no es fibonacci";
                }
            }
        }
        else
        {
            System.out.println("Numero no válido");
        }

        // NUMEROS PARES

        String mensajePares = "";
        if(num % 2 == 0)
        {
            mensajePares = "es un numero par";
        }
        else
        {
            mensajePares = "es un numero impar";
        }
        //FINAL
        return mensajePrimo + ", " + mensajeFibo + " y " + mensajePares;
    }
}
