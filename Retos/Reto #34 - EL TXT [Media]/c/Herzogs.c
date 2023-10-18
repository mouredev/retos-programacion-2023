#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#define FILENAME_ARCHIVE "text.txt"

/*
    Función que verifica existencia de archivo
    true -> si existe
    false -> no existe
*/ 
extern bool verificarExistenciaDeArchivo (const char * nombre){
    bool st = false; 
    if(access(nombre,F_OK) != -1){
        st = true;
    }
    return st;
}

static void vaciarBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

extern void mostrarContenidoAnteriorDelArchivo (FILE *pf){
    fseek(pf,0,SEEK_SET);
    int let;
    while ((let = fgetc(pf)) != EOF){
        putchar(let);
    }
}

extern void agregarContenidoAlArchivo(FILE *pf){
    char buffer[1000];
    vaciarBuffer();
    printf("\n(FIN: .)>: ");
    while (fgets(buffer, sizeof(buffer), stdin) != NULL) {
        // Eliminar el carácter de nueva línea del final de la línea leída
        buffer[strcspn(buffer, "\n")] = '\0';

        if (strcmp(buffer, ".") == 0) {
            break;  // Salir del bucle si se ingresa el punto (.)
        }

        fputs(buffer, pf);
        fputc('\n', pf);  // Agregar una nueva línea después de cada línea escrita

        printf("(FIN: .)>: ");
    }
}

int main(int argc, char const *argv[])
{
    FILE *ptFile = NULL;
    char opc;
    if (verificarExistenciaDeArchivo(FILENAME_ARCHIVE))
    {
        fprintf(stdout,"El archivo ya existe, desea borrarlo?");
        opc = getchar();
        if(opc == 's' || opc == 'S'){
            ptFile = fopen(FILENAME_ARCHIVE,"w");
        }else{
            ptFile = fopen(FILENAME_ARCHIVE,"a+");
            mostrarContenidoAnteriorDelArchivo(ptFile);
        }
        if(ptFile == NULL){
            perror("No se pudo crear el archivo");
            exit(1);
        }
    }else{
        ptFile = fopen(FILENAME_ARCHIVE,"w");
    }
    agregarContenidoAlArchivo(ptFile);
    fclose(ptFile);
    return 0;
}
