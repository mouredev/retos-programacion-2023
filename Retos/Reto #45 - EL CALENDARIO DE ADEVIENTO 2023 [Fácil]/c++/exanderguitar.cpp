#include <iostream>
#include <vector>
#include <random>

int main() {
   std::vector<std::string> contestants {};

   bool exitFlag {false};

   while(!exitFlag) {
      std::cout << "Sorteo Calendario de Adviento\n";
      std::cout << "=============================\n";
      std::cout << '\n';
      std::cout << "Selecciona una opcion.\n";
      std::cout << " 1. Nuevo participante.\n";
      std::cout << " 2. Borrar participante.\n";
      std::cout << " 3. Mostrar lista de participantes.\n";
      std::cout << " 4. Realizar sorteo.\n";
      std::cout << " 5. Salir.\n";
      std::cout << "\n >> ";

      int selection {};
      std::cin >> selection;

      std::cout << '\n';

      switch(selection) {
         case 1:
            {
               std::cout << "Cual es el nombre del participante?\n";
               std::cout << ">> ";

               std::string userName {};
               std::cin >> userName;

               bool userExists {false};

               for(size_t i = 0; i < contestants.size(); i++) {
                  if(userName == contestants[i]) {
                     userExists = true;
                  }
               }

               if(userExists) {
                  std::cout << "Este usuario ya existe.\n";
               }
               else {
                  contestants.push_back(userName);
               }
            }

            std::cout << '\n';

            break;

         case 2:
            {
               std::cout << "Que participante quieres borrar?\n";
               std::cout << ">> ";

               std::string userName {};
               std::cin >> userName;

               bool userExists {false};

               for(size_t i = 0; i < contestants.size(); i++) {
                  if(userName == contestants[i]) {
                     contestants.erase(contestants.begin() + i);
                     userExists = true;
                  }
               }

               std::cout << '\n';

               userExists ? 
                  std::cout << "El nombre ha sido borrado.\n" : 
                  std::cout << "Este participante no existe.\n";

               std::cout << '\n';
            }
            break;

         case 3:
            std::cout << "Esta es la lista de participantes.\n";
            std::cout << "==================================\n";
            
            if(contestants.empty()) {
               std::cout << "Aun no hay participantes.\n";
            }
            else {
               for(size_t i = 0; i < contestants.size(); i++) {
                  std::cout << contestants[i] << '\n';
               }  
            }

            std::cout << '\n';

            break;

         case 4:
            {
               if(!contestants.empty()) {
                  std::cout << "Empieza el sorteo.\n";
                  std::cout << '\n';
                  std::cout << "El ganador es: ";

                  std::random_device rd;
                  std::mt19937 gen(rd());
                  std::uniform_int_distribution<int> numGenerator(0, contestants.size());
                  int randomNumber = numGenerator(gen);
            
                  std::cout << contestants[randomNumber] << '\n';

                  contestants.erase(contestants.begin() + randomNumber);
               }
               else {
                  std::cout << "No hay participantes para el sorteo.\n";
               }

               std::cout << '\n';
            }
            break;

         case 5:
            std::cout << "Hasta pronto";
            exitFlag = true;
            break;

         default:
            std::cout << "No te entinedo.\n";
            break;
      }

   }

	return 0;
}
