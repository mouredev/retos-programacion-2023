using System;
namespace Zamudiio
{
   class Program
   {
      static void Main()
      {
         Console.WriteLine("🔢 Tabla de multiplicar 🔢");
         Console.Write("Ingresa algun numero entero:");
         program();

      }

      static void program()
      {
         try
         {
            string value = Console.ReadLine();
            int valueInt = int.Parse(value);
            operation(valueInt);
         }
         catch (Exception e)
         {
            Console.WriteLine("Porfavor ingresa un formato valido, debe ser un numero entero.");
            program();
         }
      }

      static void operation(int number)
      {
         Console.WriteLine($"La tabla de multiplicar de {number} es:");

         for (int i = 1; i <= 10; i++)
         {
            Console.WriteLine($"{number} x {i} = {number * i}");
         }
      }

   }
}
