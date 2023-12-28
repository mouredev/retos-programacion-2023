// Proposición de solution al reto #1 - Viernes 6 de enero de 2023
// Sitio web de retos: https://retosdeprogramacion.com/semanales2023
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Función para traducir un caracter del lenguaje normal al lenguaje "leet"
char* translate(char *c)
{
  int i;
  char *alfabeto = "abcdefghijklmnopqrstuvwxyz0123456789";
  char *letra = alfabeto;
  char *translation[] = {"4", "I3", "[", ")", "3", "|=", "&", "#", "1",
                         ",_|", ">|", "1", "/\\/\\", "^/", "0", "|*", "(_,)",
                         "I2", "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2",
                         "L", "R", "E", "A", "S", "b", "T", "B", "g", "o"};
  char minuscula;
  minuscula = tolower(*c);
  for(i=0; i<36; i++)
  {
    if (*letra==minuscula)
    {
      return translation[i];
    }
    letra++;
  }
  //Si se introduce un caracter desconocido, se devuelve el mismo caracter
  char sintraduccion[2];
  sintraduccion[0] = *c;
  sintraduccion[1] = '\0';
  char *caractersintraducir = sintraduccion;
  return caractersintraducir;
}

int main()
{
  char *frase = "¡Hola! ¿Cómo va todo? Hoy es viernes 6 de enero de 2023";  //Escribimos aquí la frase que queremos traducir
  char *caracter = frase;
  printf("Frase a traducir: %s \n", frase);
  printf("Traducción: ");
  while (*caracter)
    {
    printf("%s",translate(caracter));
    caracter++;
    }
  printf("\n");
  return 0;
}
