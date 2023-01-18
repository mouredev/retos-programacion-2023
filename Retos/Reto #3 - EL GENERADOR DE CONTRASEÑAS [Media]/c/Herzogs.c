#include <sodium/core.h>
#include <sodium/randombytes.h>
#include <sodium/utils.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define LONG_NUM 10
#define LONG_SIM 22
#define LONG_LET 26

char obtenerCaracter(const char *str, int size) {
  int idx = randombytes_uniform(size);
  printf("\nSIZE[%d] - IDX[%d] - CH[%c]",size,idx,*(str+idx));
  return *(str + idx);
}

int validar(bool hasMin, bool hasMay, bool hasNum,bool hasSim){
  int pos;
  bool corte = false;
  do{
    pos = randombytes_uniform(4) + 1;
    printf("\nNUMERO RANDOM[%d]",pos);
    switch (pos) {
      case 1:
        if(hasMin)
          corte = true;
        break;
        case 2:
          if(hasMay)
          corte = true;
        break;
        case 3:
          if(hasNum)
          corte = true;
        break;
        case 4:
          if(hasSim)
          corte = true;
        break;
    }
  }while(corte == false);
  return pos;
}

char *generarPassword(int tam, bool hasMin, bool hasMay, bool hasNum,
                      bool hasSim, char *let, char *num, char *simb) {
  char *newPass = (char *)malloc(sizeof(char *) * tam);
  int i = 0;
  if (sodium_init() < 0)
    return NULL;
  if (newPass == NULL)
    return NULL;
  memset(newPass, 0, tam);
  for (; i < tam; i++) {
    switch (validar(hasMin, hasMay, hasNum, hasSim)) {
    case 1:
          newPass[i] = obtenerCaracter(let, LONG_LET);
      break;
    case 2:
        newPass[i] = toupper(obtenerCaracter(let, LONG_LET));
      break;
    case 3:
        newPass[i] = obtenerCaracter(num, LONG_NUM);
      break;
    case 4:
        newPass[i] = obtenerCaracter(simb, LONG_SIM);
      break;
    }
  }
  return newPass;
}

char confirmacion(char *msg, char valid) {
  char rsp;
  fprintf(stdout, msg);
  fscanf(stdin, "%c", &rsp);
  char c;
  while ((c = getchar()) != '\n' && c != EOF);
  return rsp;
}

int main(int argc, char *argv[]) {
  char *letras = "abcdefghijklmnopqrstuvwxyz";
  char *numeros = "0123456789";
  char *simbolo = "!\"#$%&\'()*+,-./:;<=>?@";
  char resp;
  int tam;
  bool hasMin, hasMay, hasSim, hasNum;
  do {
    fprintf(stdout, "Ingrese tamaño de la contraseña: ");
    fscanf(stdin, "%d", &tam);
    char c;
    while ((c = getchar()) != '\n' && c != EOF);

  } while (tam < 8 || tam > 16);
  fflush(stdin);
  resp = confirmacion("Desea tener numeros: ", 's');
  hasNum = (resp == 's' || resp == 'S') ? true : false;
  resp = confirmacion("Desea tener minusculas: ", 's');
  hasMin = (resp == 's' || resp == 'S') ? true : false;
  resp = confirmacion("Desea tener mayusculas: ", 's');
  hasMay = (resp == 's' || resp == 'S') ? true : false;
  resp = confirmacion("Desea tener simbolos: ", 's');
  hasSim = (resp == 's' || resp == 'S') ? true : false;
  char *res =
      generarPassword(tam, hasMin, hasMay, hasNum, hasSim, letras, numeros, simbolo);
  if (res == NULL)
    fprintf(stderr, "\nError al generar la contraseña");
  else {
    fprintf(stdout, "\nPASSWORD [%s]", res);
    free(res);
  }
  return 0;
}
