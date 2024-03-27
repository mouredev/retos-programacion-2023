#include<iostream>
#include<vector>
using namespace std;

int main(){
	int rango;
	int divisores = 0;
	vector <int> primos;
	cout << "Digite el rango" << endl;
	cin >> rango;
	
	//Algoritmo para encontrar numeros primos y guardarlos en nuestro vector
	for(int i = 1; i<=rango;i++){
		for(int j = 1;j<=rango;j++){
			if(i % j == 0){
				divisores++;
			}
		}
		if(divisores == 2){
			primos.push_back(i);
		}

		divisores = 0;
	}
	
	//Algoritmo para encontrar los primos gemelos
	for(int i = 0;i<primos.size();i++){
		if(primos[i+1] - primos[i] == 2){
			cout << "Primos Gemelos: " << primos[i] << "," << primos[i+1] << endl;
		}
	}
}
