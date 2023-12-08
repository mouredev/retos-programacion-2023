package reto_37;

import java.util.Scanner;

/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */
public class JesusWay69 {

  public static void main(String[] args) {
    do {
      System.out.println("Teclee una opción: \n");
      int option = enterDec("-1 Convertir Hex en RGB\n-2 convertir RGB en Hex\n-3 salir\n");

      switch (option) {
        case 1:
          String rHex = enterHex("introduzca los primeros 2 caracteres hexadecimales: ");
          String gHex = enterHex("introduzca los segundos 2 caracteres hexadecimales: ");
          String bHex = enterHex("introduzca los últimos 2 caracteres hexadecimales: ");
          hexToRGB(rHex, gHex, bHex);

          break;
        case 2:
          int r = enterDec("introduzca el valor de R: ");
          int g = enterDec("introduzca el valor de G: ");
          int b = enterDec("introduzca el valor de B: ");

          RGBToHex(r, g, b);

          break;
        case 3:
          System.exit(0);

      }
    } while (true);
  }

  public static int enterDec(String message) {
    Scanner sc = new Scanner(System.in);
    String er = "[0-9]{1,3}";
    String sNumeroEntero;
    int iNumeroEntero;
    boolean correcto;
    do {
      System.out.print(message);
      sNumeroEntero = sc.next();
      correcto = sNumeroEntero.matches(er);
      iNumeroEntero = Integer.parseInt(sNumeroEntero);
      if (!correcto || (iNumeroEntero < 0 || iNumeroEntero > 255)) {
        System.out.println("Sólo se pueden introducir números del 0 al 255");
        System.exit(0);
      }
    } while (!correcto);

    return iNumeroEntero;
  }

  public static String enterHex(String message) {
    Scanner sc = new Scanner(System.in, "ISO-8859-1");
    String hexString;
    boolean reValidate;
    do {
      System.out.print(message);
      hexString = sc.next().toLowerCase();
      reValidate = hexString.matches("[a-f1-9]{1,2} || [1-9a-f]{1,2}");
      if (!reValidate && hexString.length() != 2) {
        System.out.println("Sólo se pueden introducir 2 caracteres del 0 al 9 y/o de la 'a' a la 'f'.");
       System.exit(0);
      }
    } while (reValidate);
    return hexString;
  }

  private static void hexToRGB(String rHex, String gHex, String bHex) {
    long rDec = 0;
    long gDec = 0;
    long bDec = 0;

    int pow = 0;
    for (int i = 1; i >= 0; i--) {
      int valueR = letterToValue(rHex.charAt(i));
      int valueG = letterToValue(gHex.charAt(i));
      int valueB = letterToValue(bHex.charAt(i));
      long rUp = (long) Math.pow(16, pow) * valueR;
      long gUp = (long) Math.pow(16, pow) * valueG;
      long bUp = (long) Math.pow(16, pow) * valueB;
      rDec += rUp;
      gDec += gUp;
      bDec += bUp;
      pow++;
    }
    System.out.println("El color compuesto por #" + rHex + gHex + bHex +  " equivale a    R:" + rDec + " G:" + gDec + " B:" + bDec);
    System.exit(0);
  }

  private static void RGBToHex(int r, int g, int b) {
    String red = Integer.toHexString(r);
    String green = Integer.toHexString(g);
    String blue = Integer.toHexString(b);

    System.out.println("El color compuesto por R:" + r + " G:" + g + " B:" + b + " equivale a #" + red + green + blue);
    System.exit(0);
  }

  public static int letterToValue(char letter) {
    switch (letter) {
      case 'A':
        return 10;
      case 'B':
        return 11;
      case 'C':
        return 12;
      case 'D':
        return 13;
      case 'E':
        return 14;
      case 'F':
        return 15;
      default:
        return Integer.parseInt(String.valueOf(letter));
    }
  }

}
