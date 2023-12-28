using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Xml;

namespace Semana02
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*       **Programa para traducir de español a leet ***
             * En esta solucion a la semana 1 se tuvo en cuenta si la frase tiene
             * mayusculas, o signos de puntución que si es asi estos los escribe en rojo para diferenciar 
             * de los signos usados en el lenguaje leet
             * duración aprox 2 horas (tuve varios errores y aprendi cosas nuevas)
             */ 
            //variables
            // dos string para texto y para volver a traducir otro texto
            string frase, sn;
            //int 3 para recorer arrays y para ciclar
            int posicion, letra, estado = 0;
            //arrays con para poder reconocer letra y otro para escribir la correpodiente en leet
            char[] abc = new char[] { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ' };
            string[] leet = new string[]{"4", "i3", "[", ")", "3", "i=", "&", "#", "1", ",_l", ">i", "1","/\\/\\", "^/", "~", "0", "I*", "(_,)", "i2", "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2"," "};
            // programa como tal 
            while (estado == 0)
            {
            //pide y verifica que se escria el texto
                Console.Write("*****************************************************\n" + 
                    "Bienvenido al traductor de español a lenaguaje leet. \n" + 
                    "Escriba el texto que desea traducir. \n" + ""); 
                frase = Console.ReadLine(); frase.ToLower();
                if (String.IsNullOrEmpty(frase))
                    estado = 2;
                while (estado == 2)
                {
                    Console.WriteLine("No Escribio ningún texto para traducir \nVuelvalo a escribir"); frase = Console.ReadLine();
                    if (String.IsNullOrEmpty(frase)) { }
                    else estado = 0;
                }
                estado = 0;
                //se recorren el array del abecedario y cuando encuentra el letra que se encuentra en el texto escriba el correspodiente leet
                for (letra = 0; letra < frase.Length; letra++)
                {
                    for (posicion = 0; posicion < abc.Length; posicion++)
                        if (frase[letra] == abc[posicion]) Console.Write(leet[posicion]);
                        //excepcion de signos
                    Console.ForegroundColor = ConsoleColor.Red;
                    if (abc.Contains(frase[letra])){ }
                    else Console.Write(frase[letra]);
                    Console.ForegroundColor = ConsoleColor.White;
                }
                Console.WriteLine("\nDesea traducir otro texto?? \nEscribe 'y' para SI o 'n' para NO");
                sn = Console.ReadLine();
                while (sn != "y" && sn != "n" && sn != "Y" && sn != "N")
                {
                    Console.WriteLine("no respondio 'y' o 'n'\nVuelvalo a escribir");
                    sn = Console.ReadLine();
                }
                if (sn == "n" || sn == "N")
                    estado = 1;
                Console.Clear();
            }
        }
    }
}
