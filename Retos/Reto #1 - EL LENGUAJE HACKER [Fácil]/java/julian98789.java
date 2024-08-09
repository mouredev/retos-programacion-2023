import java.util.Scanner;

public class lenguajeHaker {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Introduce el texto a traducir a lenguaje hacker (leet):");
        String input = scanner.nextLine();
        
        String textoLeet = traducirALeet(input);
        System.out.println("Texto en lenguaje hacker: " + textoLeet);
        
        scanner.close();
    }

    public static String traducirALeet(String texto) {
        String[][] diccionarioLeet = {
            {"a", "4"},
            {"b", "8"},
            {"c", "<"},
            {"d", "d"},
            {"e", "3"},
            {"f", "f"},
            {"g", "9"},
            {"h", "#"},
            {"i", "1"},
            {"j", "j"},
            {"k", "k"},
            {"l", "1"},
            {"m", "m"},
            {"n", "n"},
            {"o", "0"},
            {"p", "p"},
            {"q", "q"},
            {"r", "2"},
            {"s", "5"},
            {"t", "7"},
            {"u", "u"},
            {"v", "v"},
            {"w", "w"},
            {"x", "x"},
            {"y", "y"},
            {"z", "2"},
            {"0", "0"},
            {"1", "1"},
            {"2", "2"},
            {"3", "3"},
            {"4", "4"},
            {"5", "5"},
            {"6", "6"},
            {"7", "7"},
            {"8", "8"},
            {"9", "9"}
        };

        StringBuilder traducido = new StringBuilder();

        for (char ch : texto.toCharArray()) {
            String charComoString = String.valueOf(ch).toLowerCase();
            boolean encontrado = false;

            for (String[] par : diccionarioLeet) {
                if (par[0].equals(charComoString)) {
                    traducido.append(par[1]);
                    encontrado = true;
                    break;
                }
            }

            if (!encontrado) {
                traducido.append(ch); 
            }
        }

        return traducido.toString();
    }
    }


