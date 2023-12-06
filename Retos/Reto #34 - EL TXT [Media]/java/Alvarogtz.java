import java.io.*;
import java.util.Scanner;

public class Alvarogtz {
    public static void main(String args[]){
        File file = new File("text.txt");
        Scanner sc = new Scanner(System.in);
        boolean correct = true;

        if(file.exists()){
            do {
                System.out.println("1- Continuar escribiendo");
                System.out.println("2- Borrar fichero y escribir");
                int option = sc.nextInt();
                try {
                    if (option == 1) {
                        readFile(file);
                        writeFile(file);
                        correct = true;
                    } else if (option == 2) {
                        file.delete();
                        file = new File("text.txt");
                        writeFile(file);
                        correct = true;
                    }
                } catch (Exception e) {
                    System.out.println("Opcion incorrecta");
                    correct = false;
                }
            }while(!correct);

        }else{
            writeFile(file);
        }
    }

    public static void readFile(File file){
        try {
            FileReader fr = new FileReader(file);
            BufferedReader br = new BufferedReader(fr);
            String linea;

            while ((linea = br.readLine()) != null) {
                System.out.println(linea);
            }
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    public static void writeFile(File file){
        String texto = "";
        Scanner sc = new Scanner(System.in);
        try {
            FileWriter fw = new FileWriter(file,file.exists());

            do{
                System.out.println("Texto: ");
                texto = sc.nextLine();
                if(!texto.equals(""))
                    fw.append(texto + "\n");
            }while(!texto.equals(""));

            fw.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
