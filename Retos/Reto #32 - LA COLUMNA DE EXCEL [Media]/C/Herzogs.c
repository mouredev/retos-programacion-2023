#include <stdio.h>
#include <string.h>

extern int convertExcelColumnToNumber(const char *cad){
    int acc = 0;
    int tam = strlen(cad)-1;
    while(*cad != '\0'){
        int pot = pow(26,tam);
        int ascii = (*cad - 'A')+1; 
        acc += ascii * pot;
        cad ++;
        tam--;
    }
    return acc;
}

int main(){
    char a[20];
    fprintf(stdout,"Ingrese columna: ");
    fgets(a,20,stdin);
    printf("\nCOLUMNA [%s] => %d",a,convertExcelColumnToNumber(a));
    return 0;
}