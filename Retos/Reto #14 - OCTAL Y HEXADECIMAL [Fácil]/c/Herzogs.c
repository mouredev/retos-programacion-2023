#include <stdio.h>

/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */


static void convertHexa (int num){
    if(num == 0)
        return;
    convertHexa(num / 16);
    int resto = num % 16;
    printf("%c",(resto>=10)?resto+ 55 : resto + '0');
}

/* Otra forma de obtener el número en hexadecimal es usando el
 * desplazamiento de bits o sea el num << 4 */

static void convertOctal(int num) {
  if (num == 0) {
    return;
  }
  convertOctal(num / 8);
  printf("%d", num % 8);
}

int main(int argc, char *argv[]) {
  int num;
  printf("Ingrese numero: ");
  scanf("%d", &num);
  printf("Hexadecimal: ");
  convertHexa(num);
  printf("\nOctal: ");
  convertOctal(num);
  return 0;
}
