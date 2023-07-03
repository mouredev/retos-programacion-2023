#include <iostream>
#include <stdlib.h>
#include <cstring>
int main(int argc, char const *argv[])
{
	int cont;
	if (argc < 3){
		std::cerr<<"Bad Usage "<<argv[0]<<" <inicio> <interval>";
		return  1;
	}
	cont = atoi(argv[1]);
	std::string  comand= "sleep " + std::string(argv[2]);	
	while (cont>0) {
		std::cout<<cont<<std::endl;		
		system(comand.c_str());
		cont--;
	}
	return 0;
}