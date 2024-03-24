#include<iostream>
#include<vector>
using namespace std;

void octal(int numero){
	vector<int> octal;
	//Algoritmo octal
	while(numero > 0){
		octal.push_back(numero % 8);
		numero = numero / 8;
	}
	cout << "El numero en octal es: ";
	//Reversa del numero
	for(int i = octal.size()-1; i>= 0;i--){
		cout << octal[i];
	}             
}

void hexadecimal(int numero){
	int resto;
	vector <char> hexadecimal;
	//Algoritmo Hexadecimal
	while(numero > 0){
		resto = numero%16;
		if(resto < 10){
			resto = resto + 48;
			hexadecimal.push_back(resto);
		}
		else{
			resto = resto + 55;
			hexadecimal.push_back(resto);
		}
		numero = numero/16;
	}
	cout << "El numero en hexadecimal es: ";
	//Recursion
	for(int i = hexadecimal.size()-1;i>= 0;i--){
		cout << hexadecimal[i];
	}
}
int main(){
	int numero;
	
	cout << "Ingrese un numero: " << endl;
	cin >> numero;
	
	octal(numero);
	cout << endl;
	hexadecimal(numero);
}
