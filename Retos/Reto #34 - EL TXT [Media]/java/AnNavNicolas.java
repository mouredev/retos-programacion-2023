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
public class AnNavNicolas {
    public static void main(String[] args) {
        File file = new File("..\\text.txt");

        if(file.exists()){
            read(file);
        } else {
            create(file);
        }
    }

    public static void read(File file){
        try {
            BufferedReader br = new BufferedReader(new FileReader(file));

            System.out.println("Contenido del documento: \n");
            String linea = "";
            while((linea = br.readLine()) != null){
                System.out.println(linea);
            }
            br.close();

            write(file);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public static void create(File file){
        try {
            file.createNewFile();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        write(file);
    }

    public static void write(File file){
        System.out.println("\nEscribe guardar para cerrar el fichero con la nueva información");
        Scanner sc = new Scanner(System.in);
        System.out.print("\nNuevo texto: ");
        try {
            FileWriter fw = new FileWriter(file, true);

            String linea = "";
            while(!(linea = sc.nextLine()).equalsIgnoreCase("guardar")){
                fw.write(linea+System.lineSeparator());
            }

            fw.close();
            System.out.println("Texto guardado");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}