namespace Reto_2_Tenis
{
    internal class salaguna
    {
        private static bool _lPartidoTerminado = false;
        private static List<String> _puntuaciones = new List<String>() { "0", "15", "30", "40" };
        public static void Main()
        {
            int puntuacionP1 = 0;
            int puntuacionP2 = 0;
            while (_lPartidoTerminado == false)
            {
                Console.WriteLine("Dime los próximos puntos ganadores (P1/P2 o P1,P1,P2,...): ");
                string? miSecuencia = Console.ReadLine();
                if(miSecuencia != null)
                {
                    if (miSecuencia.Length == 2) //Solo un punto ganador
                    {
                        CompruebaPuntuaciones(ref puntuacionP1, ref puntuacionP2, miSecuencia);
                    }
                    else  //Array de puntos separado por comas
                    {
                        string[] miArray = miSecuencia.Split(',');
                        List<string> miSecuenciaFiltrada = new List<string>();
                        foreach (string item in miArray)
                        {
                            if (item.Length == 2)
                            {
                                miSecuenciaFiltrada.Add(item);
                            }
                        }
                        foreach (string item in miSecuenciaFiltrada)
                        {
                            CompruebaPuntuaciones(ref puntuacionP1, ref puntuacionP2, item);
                        }
                    }
                }
            }
        }

        private static void CompruebaPuntuaciones(ref int puntuacionP1, ref int puntuacionP2, string miSecuencia)
        {
            switch (miSecuencia.ToUpper())
            {
                case "P1":
                    if (puntuacionP2 == 4)
                        puntuacionP2--;
                    else
                        puntuacionP1++;
                    break;
                
                case "P2":
                    if (puntuacionP1 == 4)
                        puntuacionP1--;
                    else
                        puntuacionP2++;
                    break;
                
                default:
                    Console.WriteLine(miSecuencia + " no es un jugador válido");
                    break;
            }
            
            if (puntuacionP1 < 4 && puntuacionP2 < 3 || puntuacionP1 < 3 && puntuacionP2 < 4)
                Console.WriteLine(_puntuaciones[puntuacionP1]+"-"+ _puntuaciones[puntuacionP2]);
            
            if (puntuacionP1 == 3 && puntuacionP2 == 3)
                Console.WriteLine("Deuce");
            if (puntuacionP1 == 4 && puntuacionP2==3)
                Console.WriteLine("P1 Ventaja");
            if (puntuacionP2 == 4 && puntuacionP1 == 3)
                Console.WriteLine("P2 Ventaja");

            if (puntuacionP1 == 5 && puntuacionP2 == 3)
            {
                Console.WriteLine("P1 GANADOR");
                _lPartidoTerminado = true;
            }
            if (puntuacionP2 == 5 && puntuacionP1 == 3)
            {
                Console.WriteLine("P2 GANADOR");
                _lPartidoTerminado = true;
            }
            if (puntuacionP1 == 4 && puntuacionP2 < 3)
            {
                Console.WriteLine("P1 GANADOR");
                _lPartidoTerminado = true;
            }
            if (puntuacionP2 == 4 && puntuacionP1 < 3)
            {
                Console.WriteLine("P2 GANADOR");
                _lPartidoTerminado = true;
            }
        }
    }
}
