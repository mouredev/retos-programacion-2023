import java.io.*;

public class EspinoLeandroo {
    public static void main(String[] args) {
        String fileName = "text.txt";
        
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            
            File file = new File(fileName);
            boolean fileExists = file.exists();
            
            if (!fileExists) {
                file.createNewFile();
            }
            
            FileWriter fileWriter = new FileWriter(file, true); // true for append mode
            
            if (fileExists) {
                System.out.println("El archivo ya existe. ¿Deseas borrar su contenido? (Si: 1, No: 0)");
                int choice = Integer.parseInt(reader.readLine());
                if (choice == 1) {
                    fileWriter.close();
                    fileWriter = new FileWriter(file);
                } else {
                    BufferedReader fileReader = new BufferedReader(new FileReader(file));
                    String line;
                    System.out.println("Contenido actual del archivo:");
                    while ((line = fileReader.readLine()) != null) {
                        System.out.println(line);
                    }
                    fileReader.close();
                }
            }
            
            System.out.println("Introduce texto (Presiona Enter para guardar, o escribir 'exit' para salir):");
            String input;
            while (!(input = reader.readLine()).equalsIgnoreCase("exit")) {
                fileWriter.write(input + System.lineSeparator());
            }
            
            fileWriter.close();
            System.out.println("Texto guardado en el archivo.");
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
