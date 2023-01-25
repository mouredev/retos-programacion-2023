#include <ctype.h>
#include <sodium/core.h>
#include <sodium/randombytes.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LONG_NUM 10
#define LONG_SIM 22
#define LONG_LET 26
#define MINUSCULA 1
#define MAYUSCULA 2
#define NUMERO 3
#define SIMBOLO 4

/* Pasos para correr esta solución:
 * 1- Instalar sodium
 * 2- compilar con <<gcc -Wall -lsodium -O3 Herzogs.c -o main>>
 * 3- run <<./main>>
 * */

typedef struct {
  int tam;
  bool min;
  bool may;
  bool num;
  bool sym;
} Configuracion;

static inline char obtenerCaracter(const char *str, int size) {
  return *(str + randombytes_uniform(size));
}

static inline int obtenerNumeroRandom(int size){
  return randombytes_uniform(size);
}

char *generarPassword(Configuracion opt, char *let, char *num, char *simb) {
  char *newPass = (char *)malloc(sizeof(char *) * opt.tam);
  int i = 0;
  bool finished = false;
  if (sodium_init() < 0)
    return NULL;
  if (newPass == NULL)
    return NULL;
  memset(newPass, 0, opt.tam);
  while (!finished) {
    switch (obtenerNumeroRandom(opt.tam)) {
    case MINUSCULA:
      if (opt.min) {
        newPass[i] = obtenerCaracter(let, LONG_LET);
        i++;
      }
      break;
    case MAYUSCULA:
      if (opt.may) {
        newPass[i] = toupper(obtenerCaracter(let, LONG_LET));
        i++;
      }
      break;
    case NUMERO:
      if (opt.num) {
        newPass[i] = obtenerCaracter(num, LONG_NUM);
        i++;
      }
      break;
    case SIMBOLO:
      if (opt.sym) {
        newPass[i] = obtenerCaracter(simb, LONG_SIM);
        i++;
      }
      break;
    }
    if (i == opt.tam)
      finished = true;
  }
  return newPass;
}

int main(int argc, char *argv[]) {
  char *letras = "abcdefghijklmnopqrstuvwxyz";
  char *numeros = "0123456789";
  char *simbolo = "!\"#$%&\'()*+,-./:;<=>?@";
  Configuracion opt = {
      .tam = 8, .min = true, .may = false, .num = true, .sym = false};
  char *res = generarPassword(opt, letras, numeros, simbolo);
  if (res == NULL)
    fprintf(stderr, "Error al generar la contraseña");
  else {
    fprintf(stdout, "PASSWORD [%s]", res);
    free(res);
  }
  return 0;
}
