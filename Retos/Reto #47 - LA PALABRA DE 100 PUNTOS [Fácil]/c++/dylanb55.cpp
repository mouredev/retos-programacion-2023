#include<iostream>
#include<algorithm> 


int main(){
	
	int suma = 0;
	std::string palabra;
	char rpt;
	do{
		
		suma = 0;
		std::cout << "Ingrese una palabra para calcular si llegara a 100 puntos: " << std::endl;
		std::getline(std::cin,palabra);
		
		
		//Transformamos la palabra a mayusculas para evitar problemas
		for(int i = 0; i < palabra.length(); i++){
			palabra[i] = toupper(palabra[i]);
		}
		
		
		//Si existen espacios en la palabra los borraremos para evitar problemas con el algoritmo de obtencion de puntos
		
		palabra.erase(remove(palabra.begin(), palabra.end(), ' '), palabra.end());
		
		//Obteniendo los puntos de la palabra
		for(int i = 0; i < palabra.length();i++){
			suma+= palabra[i] - 64;
		}
		
		if(suma > 100){
			std::cout << "Tu palabra sumo " << suma << " lo cual es mayor a 100 puntos" << std::endl;
			std::cout << "Desea volver a intentarlo? (S/N) " << std::endl;
			std::cin >> rpt;
		}
		
		else if(suma < 100){
			std::cout << "Tu palabra sumo " << suma << " lo cual es menor a 100 puntos" << std::endl;
			std::cout << "Desea volver a intentarlo? (S/N) " << std::endl;
			std::cin >> rpt;
		}
		else{
			std::cout << "Enhorahora buena tu palabra sumo los 100 puntos" << std::endl;
			std::cout << "Fin del juego" << std::endl; 
		}
		
		std::cin.ignore();
			
	}while(rpt == 'S' or rpt == 's' and suma != 100);
	
	
	return 0;
}
