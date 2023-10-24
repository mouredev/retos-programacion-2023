/*
 * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
 * en dos dimensiones.
 * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
 *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
 * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
 * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
 * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
 */

using System;

namespace reto42
{
    public class Reto42
    {
        static void Main(string[] args)
        {
            //Punto obj1 = new Punto(0, 0);
            //Vector vel1 = new Vector(1, 1);

            //Punto obj2 = new Punto(5, 0);
            //Vector vel2 = new Vector(-1, 1);

            Punto obj1 = new Punto(0, 0);
            Vector vel1 = new Vector(1, 1);

            Punto obj2 = new Punto(3, 0);
            Vector vel2 = new Vector(-1, 1);

            Calcula_encuentro(obj1, vel1, obj2, vel2);

            Console.ReadKey();
        }

        static void Calcula_encuentro(Punto obj1, Vector vel1, Punto obj2, Vector vel2)
        {
            double deltaX = obj2.X - obj1.X;
            double deltaY = obj2.Y - obj1.Y;
            double deltaVX = vel2.X - vel1.X;
            double deltaVY = vel2.Y - vel1.Y;

            double tiempo_encuentro = -(deltaX * deltaVX + deltaY * deltaVY) / (Math.Pow(deltaVX, 2) + Math.Pow(deltaVY, 2));

            if (double.IsNaN(tiempo_encuentro) || tiempo_encuentro < 0)
            {
                Console.WriteLine("Los objetos se están alejando o ya se han encontrado");
                return;
            }

            double punto_encuentro_x = obj1.X + vel1.X * tiempo_encuentro;
            double punto_encuentro_y = obj1.Y + vel1.Y * tiempo_encuentro;

            Console.WriteLine($"El punto de encuentro es el ({punto_encuentro_x.ToString().Replace(',', '.')},{punto_encuentro_y.ToString().Replace(',', '.')}) y se encontrarán pasadas {tiempo_encuentro} unidades de tiempo");
        }

        public class Punto
        {
            public double X { get;}
            public double Y { get; }

            public Punto(double x, double y)
            {
                X = x;
                Y = y;
            }
        }

        public class Vector
        {
            public double X { get; }
            public double Y { get; }

            public Vector(double x, double y)
            {
                X = x;
                Y = y;
            }
        }
    }
}