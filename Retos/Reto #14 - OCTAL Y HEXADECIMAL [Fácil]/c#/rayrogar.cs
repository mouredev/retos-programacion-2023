namespace Reto_Semanal
{
    class Reto_14
    {
        /*
        * Crea una función que reciba un número decimal y lo trasforme a Octal
        * y Hexadecimal.
        * - No está permitido usar funciones propias del lenguaje de programación que
        * realicen esas operaciones directamente.
        */
       

        static void Main(string[] args)
        {
            char[] hexChar = { 'A', 'B', 'C', 'D', 'E', 'F' };

            while ( true)
            {
                string hex = "", oct = "";
                int dec = 0;
                int expHex = 0, expOct = 0;

                try
                {
                     Console.WriteLine("Ingrese un número en formato decimal para mostrarle la representación en notación Hexadecimal y Octal");
                     dec = int.Parse(Console.ReadLine());

                    ///Determinando exponente
                    bool fhex = false, foct = false;

                    while (!fhex || !foct)
                    {
                       
                        if(!foct){
                            if(dec > Math.Pow(8,expOct)){
                               
                                expOct++;
                            }
                            else{
                                if(expOct > 0)
                                    expOct--;
                                foct = true;
                            }
                        }

                        if(!fhex){
                            if(dec > Math.Pow(16,expHex)){
                                expHex++;
                            }
                            else{
                                if (expHex > 0)
                                    expHex--;
                                fhex = true;
                            }
                        }
                       

                    }
                  

                    //Conformando Octal!!
                    int decCopy = dec;
                    for (int i = expOct; i > -1; i--)
                    {
                      
                        if(decCopy >= 8){
                            oct += (int)(decCopy / Math.Pow(8, i));
                            decCopy = (int)(decCopy % (Math.Pow(8, i)));

                        }
                        else
                            oct += decCopy;

                    }

                    //Conformando HEX!!
                    decCopy = dec;
                    for (int i = expHex; i > -1; i--)
                    {
                        if (decCopy >= 16)
                        {
                            int t = (int)(decCopy / (Math.Pow(16, i)));
                            hex += (t >= 10 ? hexChar[t - 10].ToString() : t);
                            decCopy = (int)(decCopy % (Math.Pow(16, i)));
                        }
                        else
                            hex += decCopy;
                    }

                    Console.WriteLine(String.Format("DEC: " + dec));
                    Console.WriteLine(String.Format("OCT: "+ oct));
                    Console.WriteLine(String.Format("HEX: " + hex));
                    Console.WriteLine("expOct: {0}, expHex: {1}", expOct, expHex);

                }
                catch (Exception)
                {

                    Console.WriteLine("Hasta la vista!!! Bebe !!!");
                    break;
                }
                
            }
           
        }
    }
}