/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

#include <stdio.h>

void getParams(char url[], int length);

char params[10][10];
int paramCount = 0;

int main() {

	char url[] = "https://retosdeprogramacion.com?year=2023&challenge=0";
	//char url[] = "https://retosdeprogramacion.com?year=2023&challenge=0&a=1&b=2&c=3&d=4&e=5&f=6&g=7&h=8";
	//char url[] = "https://retosdeprogramacion.com?year=2023";
	//char url[] = "https://retosdeprogramacion.com";
	//char url[] = "https://retosdeprogramacion.com?year=2023&challenge=0&lang=c";
	
	int length = sizeof(url);
	getParams(url, length);

	for (int a = 0; a < paramCount; a++) {
		for (int b = 0; b < 10; b++) {
			printf("%c", params[a][b]);
		}
		printf("\n");
	}

	return 0;
}

void getParams(char url[], int length) {
	int j = 0;
	char isParam = 0;

	for (int i = 0; i < length; i++) {
		if (url[i] == '&' || url[i] == '\0' && isParam == 1) {
			isParam = 0;
			paramCount++;
			j = 0;
		}
		
		if (isParam == 1) {
			params[paramCount][j] = url[i];
			j++;
		} 

		if(url[i] == '=') {
			isParam = 1;
		}
	}
}
