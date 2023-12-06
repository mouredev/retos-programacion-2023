/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdbool.h>

bool viernesTrece(int month, int year);

int main () {
	int month;
	int year;

	printf("Ingrese el mes: ");
	scanf("%d", &month);
	printf("Ingrese el año: ");
	scanf("%d", &year);
	
	bool hasFri13 = viernesTrece(month, year);

	printf("%s\n", hasFri13? "Viernes 13 existe!":"No hay viernes 13 este mes");
	return 0;
}


bool viernesTrece(int month, int year) {
	// La Congrunecia de Zeller
	// h = (q + ((13(m + 1)) / 5) + K + (K/4) + (J/4) + 5J) mod 7
	
	int K;		// Centuria
	int J;		// El año de la Centuria
	int q = 13;	// Dia del mes

	if (month == 1) {    // Enero y Febrero se cuentan como mes 13 y 14 del año anterior
		month = 13;
		year = year - 1;
	} else if (month == 2) {
		month = 14;
		year = year - 1;
	} 

	K = year % 100;
	J = year / 100;

	int day = (q + round((13 * (month+1)) / 5) + K + round(K/4) + round(J/4) + (5 * J));
	day = day % 7;

	// sab = 0, dom = 1, lun = 2, mar = 3, mie = 4, jue = 5, vie = 6
	if (day == 6) return true;
	else return false;
}
