using System;
using System.Collections.Generic;
using System.ComponentModel.Design;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
/*
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
 *     siguiente disminuya en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */
namespace Reto43
{
    public class Program
    {
        
        //Declaramos clase dia
        public class dia
        {
            public DateTime fecha { get; set; }
            public int temperatura { get; set; }
            public int precipitaciones { get; set; }

        }
        //Declaramos variables globales
        public static dia[] arrayDias;

        public static int temperaturamMax = 0;
        public static int temperaturaMin = 100;

        //Metodo para dar valores a un dia
        public static dia Creardia(int rango)
        {
            var dia = new dia();
            //Asignar fecha
            var fechaInicio = System.DateTime.Today.AddDays(rango);
            dia.fecha = fechaInicio;
            if (rango <= 0) {
                dia=crearDiaInicial(dia);
            }
            else {
                dia = asignarValoresDias(dia,rango);
                
            }

            return dia;
        }

        //Metodo para dar valores a un dia que no es el primero
        private static dia asignarValoresDias(dia dia,int rango)
        {
            Random random = new Random();

            var diaAnterior= arrayDias[rango - 1];
            //precipitaciones del dia
            if (diaAnterior.temperatura >25) {

                dia.precipitaciones=diaAnterior.precipitaciones + 20;

            }else if(diaAnterior.temperatura<5){

                dia.precipitaciones = diaAnterior.precipitaciones - 20;
            }
            else
            {
                dia.precipitaciones = diaAnterior.precipitaciones;
            }


            if (dia.precipitaciones >= 100)
            {
                dia.precipitaciones = 100;
            }
            else if (dia.precipitaciones <= 0)
            {
                dia.precipitaciones = 0;
            }



            //temperatura dia
            dia.temperatura = diaAnterior.temperatura;
            if (diaAnterior.precipitaciones>=100)
            {
                dia.temperatura = dia.temperatura - 1;
            }
            //calcular 10% de posibilidades de que la temperatura del dia aumente o disminuya 2 grados
            var r = random.Next(0, 101);
            if (r <= 10)
            {
                var a = random.Next(0, 101);
                if (a < 50)
                {
                    dia.temperatura -=2 ;
                }
                else
                {
                    dia.temperatura +=2 ;
                }
            }
            comprobarTemperaturaMaxMin(dia);
           
            return dia;
        }

        //Metodo para dar valores del primer dia
        private static dia crearDiaInicial(dia dia)
        {
            Random random = new Random();
            //random.Next(0, 101) Genera un numero entre 0 y 100 (101 no se incluye)

            dia.temperatura = random.Next(0, 101);
            dia.precipitaciones = random.Next(0, 101);

            comprobarTemperaturaMaxMin(dia);
            return dia;
        }

        //Metodo para comprobar temperatura maxima y minima
        private static void comprobarTemperaturaMaxMin(dia dia)
        {
            
            if (dia.temperatura >= temperaturamMax)
            {
                temperaturamMax = dia.temperatura;
            }
            if (dia.temperatura <= temperaturaMin)
            {
                temperaturaMin = dia.temperatura;
            }
          
        }

        //Metodo para mostrar los datos de un dia
        private static void mostrarDatosDia()
        {
           
            for (int i = 0; i < arrayDias.Length; i++)
            {
                Console.WriteLine("Fecha: " + arrayDias[i].fecha.ToShortDateString());
                if (arrayDias[i].temperatura == temperaturamMax && (temperaturamMax != temperaturaMin))
                {
                    Console.ForegroundColor = ConsoleColor.Magenta;
                    Console.WriteLine("Temperatura: " + arrayDias[i].temperatura + "Cº");
                    Console.ResetColor();
                }
                else if((arrayDias[i].temperatura == temperaturaMin) && (temperaturamMax!=temperaturaMin))
                {
                    Console.ForegroundColor = ConsoleColor.Blue;
                    Console.WriteLine("Temperatura: " + arrayDias[i].temperatura + "Cº");
                    Console.ResetColor();
                }
                else
                {
                    Console.WriteLine("Temperatura: " + arrayDias[i].temperatura + "Cº");
                }
                if (arrayDias[i].precipitaciones == 100)
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("Precipitaciones: " + arrayDias[i].precipitaciones + "%");
                    Console.ResetColor();
                }
                else
                {
                    Console.WriteLine("Precipitaciones: " + arrayDias[i].precipitaciones + "%");
                }
                
                Console.WriteLine("************************");

            }
        }

        static void Main(string[] args)
        {
            //Declaración de variables
            
            var rangoDias = 0;
            //Bucle para solicitar rango de dias <0 y que sea un numero, si no salta excepcion
            do {
                try {
                    Console.WriteLine("¿Cuantos dias quieres saber el analisis de las condiciones climáticas?(sabiendo que la fecha inicial es la actual)");
                    rangoDias = int.Parse(Console.ReadLine());
                    if(rangoDias <=0)
                    {
                        throw new Exception();
                    }

                } catch (Exception e) {
                    Console.WriteLine("Error:El valor tiene que ser un numero y mayor a 0");
                
                }
                
            } while (rangoDias<=0);
          
            //asignamos en el array el rango de dias
            arrayDias = new dia[rangoDias];
            
            //Bucle para asignar valores a los dias
            for (int i = 0; i < rangoDias; i++)
            {
                var dia = Creardia(i);
                arrayDias[i] = dia;
                
            }
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.WriteLine("temperatura maxima: " + temperaturamMax);
            Console.ResetColor();
            Console.ForegroundColor= ConsoleColor.Blue;
            Console.WriteLine("temperatura Minima: " + temperaturaMin);
            Console.ResetColor();

            //Mostramos datos de todos los dias
            mostrarDatosDia();


            Console.ReadLine();
        }
       

    }
}
