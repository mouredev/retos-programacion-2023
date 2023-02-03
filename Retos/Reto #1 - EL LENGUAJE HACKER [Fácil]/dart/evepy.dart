// Importing dart:io file
import 'dart:io';
void main() {
  //Leet Speak Cheat Sheet
  var leet = {
    //alphabet
    "A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=",
    "G": "&", "H": "#", "I": "1", "J": ",_|", "K": ">|", "L": "1",
    "M": r"/\/\", "N": "^/", "O": "0", "P": "|*", "Q": "(_,)", "R": "I2",
    "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j",
    "Z": "2",
    //numbers
    "1": "L", "2": "R", "3": "E", "4": "A", "5": "S",
    "6": "b", "7": "T", "8": "B", "9": "g", "0": "o",
  };

  //Final Empty Text
  String textoF='';

  //Get to the text
  print("Escribe tu texto: ");
  String? texto = stdin.readLineSync();

  //Iterate the length of the text
  for (int i = 0; i < texto!.length; i++) {
    //If the character matches the text
    if (leet.containsKey(texto[i].toUpperCase())) {
      //Add character to the final text
      textoF += leet[texto[i].toUpperCase()]!;
    
    } else {
      //Options for the error character
      print("Uno de los caracteres ingresados no es correcto");
      print("Opciones: \n 1: Volver al inicio \n 2: Salir \n");
      String? op = stdin.readLineSync();

      switch (op) {
        //go back to the beginning
        case "1":
          print("\n");
          main();
          return;
        //end
        case "2":
          break;
      }

      break;
    }
  }
  //Answer to the translation
  print("==============");
  print(textoF);
}
