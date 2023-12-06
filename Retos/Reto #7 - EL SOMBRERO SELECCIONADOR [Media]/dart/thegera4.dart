import 'dart:io';

void main() {
  print("Bienvenido al sombrero seleccionador de Hogwarts");
  print("Responde a las siguientes preguntas");
  print("¿Qué es lo que más te gusta hacer?");
  print("1. Aprender");
  print("2. Ayudar a los demás");
  print("3. Dominar");
  print("4. Ser famoso");
  String answer1 = stdin.readLineSync()!;
  print("¿Qué es lo que más te gusta comer?");
  print("1. Sopa de pollo");
  print("2. Sopa de verduras");
  print("3. Sopa de mariscos");
  print("4. Sopa de tortuga");
  String answer2 = stdin.readLineSync()!;
  print("¿Qué es lo que más te gusta hacer en tu tiempo libre?");
  print("1. Leer");
  print("2. Jugar");
  print("3. Dormir");
  print("4. Hacer travesuras");
  String answer3 = stdin.readLineSync()!;
  print("¿Qué es lo que más te gusta hacer en el bosque?");
  print("1. Cazar");
  print("2. Pasear");
  print("3. Hacer fuego");
  print("4. Hacer travesuras");
  String answer4 = stdin.readLineSync()!;
  print("¿Qué es lo que más te gusta hacer en el mar?");
  print("1. Navegar");
  print("2. Pescar");
  print("3. Nadar");
  print("4. Hacer travesuras");
  String answer5 = stdin.readLineSync()!;
  int gryffindor = 0;
  int slytherin = 0;
  int hufflepuff = 0;
  int ravenclaw = 0;
  if (answer1 == "1") {
    ravenclaw++;
  } else if (answer1 == "2") {
    hufflepuff++;
  } else if (answer1 == "3") {
    slytherin++;
  } else if (answer1 == "4") {
    gryffindor++;
  }
  if (answer2 == "1") {
    hufflepuff++;
  } else if (answer2 == "2") {
    ravenclaw++;
  } else if (answer2 == "3") {
    slytherin++;
  } else if (answer2 == "4") {
    gryffindor++;
  }
  if (answer3 == "1") {
    ravenclaw++;
  } else if (answer3 == "2") {
    hufflepuff++;
  } else if (answer3 == "3") {
    slytherin++;
  } else if (answer3 == "4") {
    gryffindor++;
  }
  if (answer4 == "1") {
    slytherin++;
  } else if (answer4 == "2") {
    hufflepuff++;
  } else if (answer4 == "3") {
    gryffindor++;
  } else if (answer4 == "4") {
    ravenclaw++;
  }
  if (answer5 == "1") {
    gryffindor++;
  } else if (answer5 == "2") {
    hufflepuff++;
  } else if (answer5 == "3") {
    slytherin++;
  } else if (answer5 == "4") {
    ravenclaw++;
  }
  if (gryffindor > slytherin && gryffindor > hufflepuff && gryffindor > ravenclaw) {
    print("¡Gryffindor!");
  } else if (slytherin > gryffindor && slytherin > hufflepuff && slytherin > ravenclaw) {
    print("¡Slytherin!");
  } else if (hufflepuff > gryffindor && hufflepuff > slytherin && hufflepuff > ravenclaw) {
    print("¡Hufflepuff!");
  } else if (ravenclaw > gryffindor && ravenclaw > slytherin && ravenclaw > hufflepuff) {
    print("¡Ravenclaw!");
  } else {
    print("¡No te puedo asignar a ninguna casa!");
  }
}
