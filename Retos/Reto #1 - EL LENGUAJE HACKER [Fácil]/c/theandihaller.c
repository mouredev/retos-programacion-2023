
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 * se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 * con el alfabeto y los números en "leet".
 * (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

#include <stdio.h>
#include <ctype.h>

char* dictionary (char c);

int main() {
	char c;
	printf("Ingrese el texto a traducir: ");

	while ((c = getchar()) != EOF) {
		if (c == '\n' || c == '\0') break;
		printf("%s", dictionary(tolower(c)));
	}
	printf("\n");

	return 0;
}

char* dictionary (char c) {
	char *aux = &c;

	switch (c) {
		case 'a':
			return "4";
		case 'b':
			return "I3";
		case 'c':
			return "[";
		case 'd':
			return ")";
		case 'e':
			return "3";
		case 'f':
			return "|=";
		case 'g':
			return "&";
		case 'h':
			return "#";
		case 'i':
			return "1";
		case 'j':
			return ",_|";
		case 'k':
			return ">|";
		case 'l':
			return "1";
		case 'm':
			return "/\\/\\";
		case 'n':
			return "^/";
		case 'o':
			return "0";
		case 'p':
			return "(|*)";
		case 'q':
			return "(_,)";
		case 'r':
			return "I2";
		case 's':
			return "5";
		case 't':
			return "7";
		case 'u':
			return "(_)";
		case 'v':
			return "\\/";
		case 'w':
			return "\\/\\/";
		case 'x':
			return "><";
		case 'y':
			return "j";
		case 'z':
			return "2";
		case '1':
			return "L";
		case '2':
			return "R";
		case '3':
			return "E";
		case '4':
			return "A";
		case '5':
			return "S";
		case '6':
			return "b";
		case '7':
			return "T";
		case '8':
			return "B";
		case '9':
			return "g";
		case '0':
			return "0";
		default:  // Si no existe en la lista, devuelvo el mismo char
			return aux;
	}
} 
