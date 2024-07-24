#include <stdio.h>

int main(int argc, char const *argv[])
{
   for (size_t i = 0; i <= 100; i++)
   {
    if  (i % 3 == 0 && i% 5 == 0)//cuidar el orden de la comprobacion
    {   
        printf("fizzbuzz \n");
    }else if (i%5 == 0)
    {
        printf("buzz \n");
    }else if (i % 3 == 0)
    {
        printf("fizz \n");
    }else{
        printf("%d\n",i);

    }
   }
   
    return 0;
}
