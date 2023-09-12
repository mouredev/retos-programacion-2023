import java.io.*;
import java.util.Scanner;

public class TextFile {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String option;
        String text;
        File file = new File("text.txt");

        if (!file.exists()){
            try {
                file.createNewFile();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

        if (file.exists()){
            System.out.println("What do you want to do?\n1. Write to the file\n2. Delete file");
            option = sc.nextLine();

            if (option.equals("1")){
                readFile(file);
                while (true){
                    System.out.println("Type the text to add or \"exit\" to quit:");
                    text = sc.nextLine();
                    if (text.equals("exit")) break;
                    text += "\n";
                    writeFile(file, text);
                }
            }

            if (option.equals("2") && (file.delete())) System.out.println("File deleted");
        }
    }

    static void writeFile(File file, String str){
        try (Writer w = new FileWriter(file, true)){
            w.write(str);
            w.flush();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    static void readFile(File file){
        try (Reader r = new FileReader(file);
        BufferedReader bf = new BufferedReader(r)){
            String ch;
            System.out.println("Reading file...\n");
            do {
                ch = bf.readLine();
                if (ch != null) System.out.println(ch);
            } while (ch != null);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

}
