#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

typedef struct{
  char key;
  char value[4];
}leet;

static leet* buscarReferenciaEnElDiccionario(const leet *dict, const char key, const int size ){
  leet * aux = NULL;
  bool enc = false;
  int idx = 0;
  while(idx < size && !enc){
    if(dict->key == key){
      aux = dict;
      enc = true;
    }
    dict++;
  }
  return (enc==true)?aux:NULL;
}



char* generarCodigoLeet(const char *msg, const leet *dict, int size){
  char *nuevaCadena = NULL;
  nuevaCadena = (char*) malloc(sizeof(char)*100);
  if(nuevaCadena == NULL)
    return NULL;
  while(*msg != '\0'){
    leet *cod = buscarReferenciaEnElDiccionario(dict,*msg,size);
    if(cod != NULL)
      strcat(nuevaCadena,cod->value);
    else
      strcat(nuevaCadena,msg);
    msg++;
  }
  return nuevaCadena;
}

void generarDiccionario(leet *diccionario){
  diccionario[0].key = 'a';
  strcpy(diccionario[0].value,"4");
  diccionario[1].key='b';
  strcpy(diccionario[1].value,"I3");
  diccionario[2].key='c';
  strcpy(diccionario[2].value,"[");
  diccionario[3].key='d';
  strcpy(diccionario[3].value,")");
  diccionario[4].key='e';
  strcpy(diccionario[4].value,"3");
  diccionario[5].key='f';
  strcpy(diccionario[5].value,"|=");
  diccionario[6].key='g';
  strcpy(diccionario[6].value,"&");
  diccionario[7].key='h';
  strcpy(diccionario[7].value,"#");
  diccionario[8].key='i';
  strcpy(diccionario[8].value,"1");
  diccionario[9].key='j';
  strcpy(diccionario[9].value,",_|");
  diccionario[10].key='k';
  strcpy(diccionario[10].value,">|");
  diccionario[11].key='l';
  strcpy(diccionario[11].value,"1");
  diccionario[12].key='m';
  strcpy(diccionario[12].value,"^^");
  diccionario[13].key='n';
  strcpy(diccionario[13].value,"^/");
  diccionario[14].key='o';
  strcpy(diccionario[14].value,"0");
  diccionario[15].key='p';
  strcpy(diccionario[15].value,"|*");
  diccionario[16].key='q';
  strcpy(diccionario[16].value,"(_,)");
  diccionario[17].key='r';
  strcpy(diccionario[17].value,"I2");
  diccionario[18].key='s';
  strcpy(diccionario[18].value,"5");
  diccionario[19].key='t';
  strcpy(diccionario[19].value,"7");
  diccionario[20].key='u';
  strcpy(diccionario[20].value,"(_)");
  diccionario[21].key='v';
  strcpy(diccionario[21].value,"|/");
  diccionario[22].key='w';
  strcpy(diccionario[22].value,"2u");
  diccionario[23].key='x';
  strcpy(diccionario[23].value,"><");
  diccionario[24].key='y';
  strcpy(diccionario[24].value,"j");
  diccionario[25].key='z';
  strcpy(diccionario[25].value,"2");
  diccionario[26].key='1';
  strcpy(diccionario[26].value,"L");
  diccionario[27].key='2';
  strcpy(diccionario[27].value,"R");
  diccionario[28].key='3';
  strcpy(diccionario[28].value,"E");
  diccionario[29].key='4';
  strcpy(diccionario[29].value,"A");
  diccionario[30].key='5';
  strcpy(diccionario[30].value,"S");
  diccionario[31].key='6';
  strcpy(diccionario[31].value,"b");
  diccionario[32].key='7';
  strcpy(diccionario[32].value,"T");
  diccionario[33].key='8';
  strcpy(diccionario[33].value,"B");
  diccionario[34].key='9';
  strcpy(diccionario[34].value,"g");
  diccionario[35].key='0';
  strcpy(diccionario[35].value,"o");
}

int main(const int nargs, const char **args){
  leet diccionario[36];
  generarDiccionario(diccionario);
  char * msg = "hola\0";
  //fputs(msg,stdout);
  fprintf(stdout,"Mensaje sin decodificar es: %s\nMensaje codificado es %s\n",msg,generarCodigoLeet(msg,diccionario,36));
  return 0;
}
