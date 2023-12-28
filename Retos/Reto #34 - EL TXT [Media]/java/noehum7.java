import java.io.*;
import java.util.Scanner;

public class ficheroTXT {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        File archivo = null;
        FileReader fr = null;
        BufferedReader br = null;
        FileWriter archivoEscribir = null;
        PrintWriter pw = null;

        int opcion = 0;
        String textoEscribir, lineaLeer, primeraLinea;
        boolean salir = false;

        archivo = new File("text.txt");
      
        if (!archivo.exists()) {
            try {
                archivo.createNewFile();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

        System.out.println("Bienvenido al programa.");
        while (!salir) {
            System.out.println("Pulse 1 para seguir escribiendo en el fichero," +
                    " pulse 2 para borrar el contenido del fichero o pulse 3 para salir.");
            opcion = sc.nextInt();
          
            switch (opcion) {
                case 1:
                    try {
                        fr = new FileReader(archivo);
                        br = new BufferedReader(fr);

                        primeraLinea = br.readLine();
                        if (primeraLinea == null) {
                            System.out.println("El archivo está vacío.");
                        } else {
                            System.out.println("El texto del archivo es:");
                            System.out.println(primeraLinea);
                            while ((lineaLeer = br.readLine()) != null) {
                                System.out.println(lineaLeer);
                            }
                        }
                        sc.nextLine();
                        System.out.println("Escribe lo que quieras a continuación:");
                        textoEscribir = sc.nextLine();
                        archivoEscribir = new FileWriter("text.txt", true);
                        pw = new PrintWriter(archivoEscribir);
                        pw.println(textoEscribir);
                        System.out.println("Archivo escrito exitosamente!");
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    } finally {
                        try {
                            br.close();
                            fr.close();
                            pw.close();
                            archivoEscribir.close();
                        } catch (IOException e) {
                            System.out.println("Error cerrando el fichero: " + e);
                        }
                    }
                    break;
                case 2:
                    if (archivo.delete()) {
                        System.out.println("Archivo borrado correctamente.");
                    } else {
                        System.out.println("No se pudo borrar el archivo.");
                    }
                    salir = true;
                    break;
                case 3:
                    salir = true;
                    break;
                default:
                    System.out.println("Tienes que introducir una opción válida, solo números del 1 al 3.");
            }
        }

        System.out.println("Has salido del programa.");

    }
}
