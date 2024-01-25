#include <iostream>
#include <string>

using namespace std;
bool static isPrimo(int value) {
	int divisor = 2;
	while (((value % divisor) != 0))
	{
		divisor++;
	}
	return (value == divisor);
}
bool static isFibonacci(int value) {
	int aux;

	int anterior = 1;
	int actual = 1;
	while (actual < value) {
		aux = actual;
		actual += anterior;
		anterior = aux;
	}
	return (actual == value);

}
bool static isPar(int value) {
	return ((value % 2) == 0);
}
void main()
{
	while (true) {
		int number;
		string text ;

		cout << "Escribe un numero: ";
		cin >> number;
		text = to_string(number);
		if (number == 1) {
			number = 3;
		}
		if (not isPrimo(number)) {
			text += " no";
		}
		text += " es primo,";
		if (not isFibonacci(number)) {
			text += " no es";
		}
		text += " fibonacci,";

		if (isPar(number)) {
			text += " es par";
		}
		else {
			text += " es impar";
		}

		cout << text << endl;
	}
}
