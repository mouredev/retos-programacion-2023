import java.util.Scanner;

public class Rfuentes1 {
    public static void main(String args[]){
      int resultadoUsuario = 0;
      Scanner scanner = new Scanner(System.in);
      while(resultadoUsuario != 100){ 
        System.out.println("Ingresa una palabra");
        String palabraUsuario = scanner.nextLine();
        resultadoUsuario = CalculateWordPoints(palabraUsuario);

        if (resultadoUsuario != 100) {
          System.out.println("Tu palabra no es de 100 puntos es de: " + resultadoUsuario + ". Intenta de nuevo.");
        } else{
          System.out.println("¡Bien hecho! Tu puntuación es de 💯 ✨ \nSaliendo del programa...");
        }
      }
      scanner.close();
    }

    public static int CalculateWordPoints(String palabra){
      palabra = palabra.toLowerCase();
      palabra = palabra.replaceAll("á", "a");
      palabra = palabra.replaceAll("é", "e");
      palabra = palabra.replaceAll("í", "i");
      palabra = palabra.replaceAll("ó", "o");       
      palabra = palabra.replaceAll("ú", "u");
      palabra = palabra.replaceAll("ü", "u");

      String abc[] = "-abcdefghijklmnñopqrstuvwxyz".split("");
      String word[] = palabra.split("");
      int sum = 0;
      for(int i = 0; i < palabra.length(); i++){
        for(int j = 1; j < abc.length; j++){
          if (word[i].equals(abc[j])) {
            sum += j;   
            break;
          }   
        }
      }
      return sum;
    }
}