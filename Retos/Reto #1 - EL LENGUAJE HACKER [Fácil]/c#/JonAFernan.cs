using System;
using System.Collections.Generic;

public class Program
{
  public static void Main()
  {
    string msg = @"* Escribe un programa que reciba un texto y transforme lenguaje natural
* a \""lenguaje hacker\""(conocido realmente como \""leet\"" o \""1337\""). 
* Este lenguaje se caracteriza por sustituir caracteres alfanuméricos. 
* Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
* con el alfabeto y los números en \""leet\"".
* (Usa la primera opción de cada transformación)";
    
    Console.WriteLine(LeetTranslator(msg));
  }

  static string LeetTranslator (string word)
  {
    int counter = 0;
    string[] arrayWordInLeet = new string[word.Length];
    foreach (var letter in word.ToLower())
    {
      switch(letter) 
      {
        case 'a':
          arrayWordInLeet[counter] = "4";
          break;
        case 'b':
          arrayWordInLeet[counter] = "13";
          break;
        case 'c':
          arrayWordInLeet[counter] = "[";
          break;
        case 'd':
          arrayWordInLeet[counter] = ")";
          break;
        case 'e':
          arrayWordInLeet[counter] = "3";
          break;
        case 'f':
          arrayWordInLeet[counter] = "|=";
          break;
        case 'g':
          arrayWordInLeet[counter] = "&";
          break;
        case 'h':
          arrayWordInLeet[counter] = "#";
          break;
        case 'i':
          arrayWordInLeet[counter] = "1";
          break;
        case 'j':
          arrayWordInLeet[counter] = ",_|";
          break;
        case 'k':
          arrayWordInLeet[counter] = ">|";
          break;
        case 'l':
          arrayWordInLeet[counter] = "|_";
          break;
        case 'm':
          arrayWordInLeet[counter] = @"/\/\";
          break;
        case 'n':
          arrayWordInLeet[counter] = "^/";
          break;
        case 'o':
          arrayWordInLeet[counter] = "0";
          break;
        case 'p':
          arrayWordInLeet[counter] = "|*";
          break;
        case 'q':
          arrayWordInLeet[counter] = "(_,)";
          break;
        case 'r':
          arrayWordInLeet[counter] = "12";
          break;
        case 's':
          arrayWordInLeet[counter] = "5";
          break;
        case 't':
          arrayWordInLeet[counter] = "7";
          break;
        case 'u':
          arrayWordInLeet[counter] = "(_)";
          break;
        case 'v':
          arrayWordInLeet[counter] = @"\/";
          break;
        case 'w':
          arrayWordInLeet[counter] = @"\/\/";
          break;
        case 'x':
          arrayWordInLeet[counter] = "><";
          break;
        case 'y':
          arrayWordInLeet[counter] = "j";
          break;
        case 'z':
          arrayWordInLeet[counter] = "2";
          break;
        case '0':
          arrayWordInLeet[counter] = "o";
          break;
        case '1':
          arrayWordInLeet[counter] = "L";
          break;
        case '2':
          arrayWordInLeet[counter] = "R";
          break;
        case '3':
          arrayWordInLeet[counter] = "E";
          break;
        case '4':
          arrayWordInLeet[counter] = "A";
          break;
        case '5':
          arrayWordInLeet[counter] = "S";
          break;
        case '6':
          arrayWordInLeet[counter] = "b";
          break;
        case '7':
          arrayWordInLeet[counter] = "T";
          break;
        case '8':
          arrayWordInLeet[counter] = "B";
          break;
        case '9':
          arrayWordInLeet[counter] = "g";
          break;
        default:
          arrayWordInLeet[counter] = Convert.ToString(letter);
          break;
        
      }

      counter ++;
    }
    string wordInLeet = string.Join("",arrayWordInLeet);
    return(wordInLeet);

  }
  
}
