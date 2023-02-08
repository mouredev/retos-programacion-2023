/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Setting the array for the characters
const int Z = 200;
string characterSet[Z];
int pointer = 0;

// Getting all the cahracters for use
string minusChar[] = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};

string mayus[] = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};

string numbers[] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};

string simbols[] = {"|", "!", "\"", "#", "$", "%", "&", "/", "(", ")", "=", "?", "'", "\\", "¡", "¿", "+", "-", "*", "{", "}", "[", "]", ";", ":", "_", "^"};

void concatenate(string newCharacters[], int size);
void checkLength(int &passwordLength);

int main() {
	
	// Asking the user for the selected information
	int passLength;
	char hasMayus, hasNumbers, hasSimbols;
	concatenate(minusChar, sizeof(minusChar) / sizeof(*minusChar));
	cout << "Ingresar la longuitud: ";
	cin >> passLength;
	cout << "Tiene mayusculas?(y/n) ";
	cin >> hasMayus;
	cout << "Tiene números?(y/n) ";
	cin >> hasNumbers;
	cout << "tiene símbolos?(y/n) ";
	cin >> hasSimbols;
	checkLength(passLength);
	// Cheking the different flags for character use
	if (hasMayus == 'y') {
		concatenate(mayus, sizeof(mayus) / sizeof(*mayus));
	}
	if (hasNumbers == 'y') {
		concatenate(numbers, sizeof(numbers) / sizeof(*numbers));
	}
	if (hasSimbols == 'y') {
		concatenate(simbols, sizeof(simbols) / sizeof(*simbols));
	}
	string password = "";
	// Looping through to obtain the password
	for (int i = 0; i < passLength; i++) {
		password += characterSet[rand() % pointer];
	}
	cout << password << endl;
}

// Function to concatenate the new set of chracters with the actual
void concatenate(string newCharacters[], int size) {
	for (int i = 0; i < size; i++) {
		if (pointer < Z) {
			characterSet[pointer] = newCharacters[i];
			pointer++;
		}
	}
}

// Function to determine the size of the password, keeping the restrictions in check
void checkLength(int &passwordLength) {
	if (passwordLength < 8) {
		passwordLength = 8;
	} else if (passwordLength > 16) {
		passwordLength = 16;
	}
}