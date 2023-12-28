package reto_34;

import java.io.*;
import java.util.Scanner;
/*
 * Crea un programa capaz de interactuar con un fichero TXT.
 * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección.
 * Únicamente el código.
 *
 * - Si no existe, debe crear un fichero llamado "text.txt".
 * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
 *   en una nueva línea cada vez que se pulse el botón "Enter".
 * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
 *   a continuación o borrar su contenido y comenzar desde el principio.
 * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
 *   el texto que ya posee el fichero.
 */

public class JesusWay69 {

  public static void main(String[] args) {

    JesusWay69 method = new JesusWay69();
    Scanner sc = new Scanner(System.in);
    String text;
    System.out.print("Introduzca el nombre del archivo txt a crear: ");
    String fileName = sc.next();
    boolean flag;
    File file = (method.createFile(fileName));
   
      System.out.println("El fichero \"" + fileName + ".txt\" está creado y está listo para usar.");
      System.out.println("-----------------------------------------------------------------------------------------------------");
      System.out.println("-Escriba y pulse \"Enter\" para saltar línea y continuar escribiendo.");
      System.out.println("-Pulse \"Enter\", escriba  \"exit\" y vuelva a pulsar \"Enter\" para guardar archivo y salir.");
      System.out.println("-Pulse \"Enter\", escriba  \"delete\" y vuelva a pulsar \"Enter\" para borrar todo el texto y salir.");
      System.out.println();
      System.out.println("Escribiendo en " +fileName +".txt:");
   
      do {
        text = sc.nextLine();
        if ("delete".equals(text)) {
          method.deleteText(file);
          System.out.println("Texto borrado , fin del programa");
          flag = true;
          break;
        } else if ("exit".equals(text)) {
          System.out.println("Texto guardado , fin del programa");
          flag = true;
          break;
        } else {
          method.readFile(file);
          method.writeFile(file);
          flag = false;
        }
      } while (!flag);
    
  }

  private File createFile(String fileName) {
    File file = new File("src/reto_34/data/" + fileName + ".txt");
    try {
      if (!file.exists()) {
        file.createNewFile();
   System.out.println("Fichero \"" + fileName + ".txt\" creado con éxito.");
      } 
    } catch (IOException ex) {
      ex.printStackTrace(System.out);
    }
    return file;
  }

  private void writeFile(File file) {
    Scanner sc = new Scanner(System.in);
    String text;
    try {
      FileWriter fw = new FileWriter(file, true);
      do {
        text = sc.nextLine();
        if (!text.equals("")) {
          fw.append(text + "\n");
          fw.flush();
        }
      } while (!text.equals(""));
      fw.close();

    } catch (IOException ex) {
      ex.printStackTrace(System.out);
    }
  }

  private void readFile(File file) {
    String text = "";
    try {
      FileReader fr = new FileReader(file);
      BufferedReader br = new BufferedReader(fr);

      while (text != null) {
        System.out.println(text);
        text = br.readLine();
      }

    } catch (IOException ex) {
      ex.printStackTrace(System.out);

    }
  }

  private void deleteText(File file) {
    try {
      PrintWriter pw = new PrintWriter(file);
      pw.write("");
      pw.close();
    } catch (IOException ex) {
      ex.printStackTrace(System.out);
    }
  }
}
