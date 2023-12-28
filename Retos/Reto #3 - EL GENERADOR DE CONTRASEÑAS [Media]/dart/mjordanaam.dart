/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

import 'dart:math';

String uppercase = "ABCDEFGHIJKLMNOPKRSTUVWXYZ";
String lowercase = uppercase.toLowerCase();
String numbers = "0123456789";
String special = "*@%_:./^~>#()<";

String generatePasword(length, upper, lower, numeric, spec){
  String password = "";
  int counter = 0;
  String characters = "";
  Random random = Random();

  if(length > 7 && length < 17){
    if (upper == true){
      password += uppercase[random.nextInt(uppercase.length)];
      counter += 1;
      characters += uppercase;
    }
    
    if (lower == true){
      password += lowercase[random.nextInt(lowercase.length)];
      counter += 1;
      characters += lowercase;
    }

    if (numeric == true){
      password += numbers[random.nextInt(numbers.length)];
      counter += 1;
      characters += numbers;
    }

    if (spec == true){
      password += special[random.nextInt(special.length)];
      counter += 1;
      characters += special;
    }

    if (password != ""){
      List<String> provisional = List<String>.generate(counter, (counter) => '$counter');
      
      for(int j = 0; j < counter; j++){
        provisional[j] = password[j];
      }
      
      provisional.shuffle();     
      
      password = "";
      
      for(int k = 0; k < provisional.length; k++){
        password += provisional[k];
      }
      
      for(int i = 0; i < length-counter; i++){
        password += characters[random.nextInt(characters.length)];
      }
    }
  }else{
    password += "Invalid length";
  }
  return password;
}


void main()
{
  late String password;
	password = generatePasword(8, true, true, true, true);
  print(password);

  password = generatePasword(15, true, false, false, false);
  print(password);

  password = generatePasword(10, true, true, false, false);
  print(password);

  password = generatePasword(8, true, true, false, true);
  print(password);

  password = generatePasword(16, false, false, true, true);
  print(password);

  password = generatePasword(5, true, true, true, true);
  print(password);

  password = generatePasword(17, true, true, true, true);
  print(password);
}
