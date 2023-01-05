/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
  char string[256] = {'\0'};
  printf("Cual es el texto a convertir?: \t");
  gets(string);
  printf("\nTexto Original: %s \n Texto en l33t: ", string);
  strcpy(string, strlwr(string));
  for (size_t i = 0; i < strlen(string); i++) {
    switch (string[i]) {
    case ' ':
      printf(" ");
      break;
    case '1':
      printf("L");
      break;
    case '2':
      printf("R");
      break;
    case '3':
      printf("E");
      break;
    case '4':
      printf("A");
      break;
    case '5':
      printf("S");
      break;
    case '6':
      printf("b");
      break;
    case '7':
      printf("T");
      break;
    case '8':
      printf("B");
      break;
    case '9':
      printf("g");
      break;
    case 'a':
      printf("4");
      break;
    case 'b':
      printf("I3");
      break;
    case 'c':
      printf("[");
      break;
    case 'd':
      printf(")");
      break;
    case 'e':
      printf("3");
      break;
    case 'f':
      printf("|=");
      break;
    case 'g':
      printf("&");
      break;
    case 'h':
      printf("#");
      break;
    case 'i':
      printf("1");
      break;
    case 'j':
      printf(",_|");
      break;
    case 'k':
      printf(">|");
      break;
    case 'l':
      printf("1");
      break;
    case 'm':
      printf("/\\/\\");
      break;
    case 'n':
      printf("^/");
      break;
    case 'ñ':
      printf("ñ");
      break;
    case 'o':
      printf("0");
      break;
    case 'p':
      printf("|*");
      break;
    case 'q':
      printf("(_,)");
      break;
    case 'r':
      printf("I2");
      break;
    case 's':
      printf("5");
      break;
    case 't':
      printf("7");
      break;
    case 'u':
      printf("(_)");
      break;
    case 'v':
      printf("\\/");
      break;
    case 'w':
      printf("\\/\\/");
      break;
    case 'x':
      printf("><");
      break;
    case 'y':
      printf("j");
      break;
    case 'z':
      printf("2");
      break;
    }
  }
  printf("\n");
  system("pause");
  return 0;
}
