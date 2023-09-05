import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;

class Qv1ko {

    public static void main(String[] args) {
        txt();
    }

    private static void txt() {

        File txt = new File(".\\text.txt");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = null;
        String option = "";

        try {

            if (!txt.exists()) {
                txt.createNewFile();
            }

            bw = new BufferedWriter(new FileWriter(txt));

            writeFile(bw, br);
            
            do {
                
                System.out.print("\nOptions:\n  1) Cotinue\n  2) Delete all\n\nSelect option: ");
                option = br.readLine();
                
                if (option.equals("1")) {
                    readFile(new BufferedReader(new FileReader(txt)));
                    writeFile(bw, br);
                }
                
            } while (!option.equals("2"));

            clearFile(bw, txt);
            
        } catch (IOException exc) {
            exc.getMessage();
        }

    }
    
    private static void writeFile(BufferedWriter bw, BufferedReader br) throws IOException {

        System.out.print("Write: ");
        bw.write(br.readLine());
        bw.newLine();
        
        bw.flush();

    }

    private static void readFile(BufferedReader brf) throws IOException {

        System.out.println();

        while(brf.ready()) {
            System.out.println(brf.readLine());
        }

        System.out.println();

    }

    private static void clearFile(BufferedWriter bw, File txt) throws IOException{

        FileWriter file = new FileWriter(".\\text.txt");
        file.write("");
        file.close();
        
    }

}
