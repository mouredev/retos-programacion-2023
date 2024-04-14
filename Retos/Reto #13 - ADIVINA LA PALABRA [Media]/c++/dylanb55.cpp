#include<iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;

string palabras[8] = {"arbol", "camion","perro","auto","vasija","paralelepipedo","mouredev","java"};


string seleccionPalabra(string palabras[8]){

	srand(time(NULL)); 
	int numero_aleatorio = rand() % 8;
	return palabras[numero_aleatorio];
};

string mostrarTablero(){
	string tablero = seleccionPalabra(palabras);
	int largo = tablero.size();
	
	for(int i = 0;i<largo*0.6; i++){
		tablero[rand() % tablero.size()] = '_';
 	}
	
	return tablero;
}

void juego(){
	string palabra_seleccionada = seleccionPalabra(palabras);
	string tablero = mostrarTablero();
	string rpt;
	int vidas = palabra_seleccionada.size();
	cout << "\nBienvenido al juego adivina la palabra" << endl;
	cout << "\nA continuacion se mostrara el tablero del juego" << endl;
	cout << "Vidas: " << vidas << endl; 
	cout << "\n";
	cout << "Tablero: " << endl;
	cout << tablero << endl;
	
	
	do{
		bool palabra = false;
		cout << endl;
		cout << "Ingrese una letra o la palabra completa para ver si corresponde o no: " << endl;
		getline(cin,rpt);
		
		cout << "\n";
		
		for(int i = 0;i<palabra_seleccionada.size();i++){
			for(int j = 0;j<rpt.size();j++){
				if(palabra_seleccionada == rpt){
					cout << "Ha encontrado la palabra oculta, felicitaciones " << endl;
					cout << "La palabra oculta era: " << palabra_seleccionada << endl;
					cout << "Fin del juego" << endl;
					exit(0);
					
				}
				else if(palabra_seleccionada[i] == rpt[j]){
					tablero[i] = rpt[j];
					palabra = true;
							
				}
			
								
				}
				
			}
		
			if(palabra == true){
				cout << "La palabra que eligio se encontro en el tablero" << endl;
			}
			else{
				cout << "La palabra que eligio no se encontro en el tablero "<< endl;
				cout << "Pierde una vida" << endl;
				vidas--;
			}
			cout << "\n";
	
		
		cout << "\nMostrando tablero actualizado" << endl;
		cout << "Vidas: " << vidas << endl;
		cout << tablero << endl;
		
		
		if(tablero == palabra_seleccionada){
			cout << "Ha logrado completar el tablero, la palabra oculta era: " << palabra_seleccionada << endl;
			cout << "Fin del juego" << endl;
			exit(0);
		}
		else if(vidas == 0){
			cout << "Se le acabaron las vidas fin de la partida" << endl;
		}
	
	}while(palabra_seleccionada != rpt and tablero != palabra_seleccionada and vidas != 0);
}

int main(){
	juego();
	
}
