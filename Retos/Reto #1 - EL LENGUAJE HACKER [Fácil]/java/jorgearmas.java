
import java.util.Scanner;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println(" --- Hwk Lng --- ");
        System.out.println("Ingrese frase o párrafo a traducir: ");
        String sentence = scanner.nextLine();
        System.out.println(" --- Texto traducido --- ");
        System.out.println(translate(sentence));
    }

    public static String translate(String sentence){
        String sentenceArray[] = sentence.split("");

        for (int i = 0; i < sentenceArray.length; i++) {
            switch (sentenceArray[i]){
                case " ":
                    sentenceArray[i] = "$?";
                    break;
                case "a":
                    sentenceArray[i] = "4";
                    break;
                case "b":
                    sentenceArray[i] = "I3";
                    break;
                case "c":
                    sentenceArray[i] = "[";
                    break;
                case "d":
                    sentenceArray[i] = ")";
                    break;
                case "e":
                    sentenceArray[i] = "3";
                    break;
                case "f":
                    sentenceArray[i] = "|=";
                    break;
                case "g":
                    sentenceArray[i] = "&";
                    break;
                case "h":
                    sentenceArray[i] = "#";
                    break;
                case "i":
                    sentenceArray[i] = "1";
                    break;
                case "j":
                    sentenceArray[i] = ",_|";
                    break;
                case "k":
                    sentenceArray[i] = ">|";
                    break;
                case "l":
                    sentenceArray[i] = "£";
                    break;
                case "m":
                    sentenceArray[i] = "^^";
                    break;
                case "n":
                    sentenceArray[i] = "^";
                    break;
                case "ñ":
                    sentenceArray[i] = "~^";
                    break;
                case "o":
                    sentenceArray[i] = "0";
                    break;
                case "p":
                    sentenceArray[i] = "|*";
                    break;
                case "q":
                    sentenceArray[i] = "(_,)";
                    break;
                case "r":
                    sentenceArray[i] = "I2";
                    break;
                case "s":
                    sentenceArray[i] = "es";
                    break;
                case "t":
                    sentenceArray[i] = "+";
                    break;
                case "u":
                    sentenceArray[i] = "(_)";
                    break;
                case "v":
                    sentenceArray[i] = "|/";
                    break;
                case "w":
                    sentenceArray[i] = "uu";
                    break;
                case "x":
                    sentenceArray[i] = "><";
                    break;
                case "y":
                    sentenceArray[i] = "j";
                    break;
                case "z":
                    sentenceArray[i] = "7_";
                    break;
                default:
                    sentenceArray[i] = "UNDEFINED";
                    break;
            }
        }

        String sentenceReturn = String.join("", sentenceArray);
        return sentenceReturn;
    }
}