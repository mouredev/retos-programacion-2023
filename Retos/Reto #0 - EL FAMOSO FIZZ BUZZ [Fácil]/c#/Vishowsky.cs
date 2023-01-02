using Retos_de_programacion;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Retos_de_programacion
{
    internal class FizzBuzz
    {
        public void imprimirBFizzBuzz()
        {

            for(int i = 0; i <=100 ; i++ ) {

                if (i % 3 == 0  && i % 5 ==0)
                {
                    Console.WriteLine("FizzBuzz");
                }
                else if(i % 3 == 0){
                    Console.WriteLine("Fizz");
                }
                else if(i % 5 == 0)
                {
                    Console.WriteLine("Buzz");
                }
                else
                {
                    Console.WriteLine(i);
                }

            
            
            
            }

        }

    }

}

