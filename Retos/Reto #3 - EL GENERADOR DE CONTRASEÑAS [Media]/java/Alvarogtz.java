
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

import java.util.*;

public class Alvarogtz {

    private final  String[]options = {"MAYUSCULAS","NUMEROS","SIMBOLOS","GENERAR","SALIR"};
    private Scanner entrada = new Scanner(System.in);
    private Password password = new Password();

    public static void main(String[] args) {

        Alvarogtz start = new Alvarogtz();
        boolean generarPassword = false;
        boolean salir = false;

        do {
            String option = start.printMenu(start.password);
            switch (option) {
                case "MAYUSCULAS":
                    start.password.mayusculas = !start.password.mayusculas;
                    break;
                case "NUMEROS":
                    start.password.numeros = !start.password.numeros;
                    break;
                case "SIMBOLOS":
                    start.password.simbolos = !start.password.simbolos;
                    break;
                case "GENERAR":
                    generarPassword = true;
                    break;
                default:
                    salir = true;
                    break;
            }
        }while(!generarPassword && !salir);

        if(generarPassword)
            System.out.println(start.doPassword(start.password));

        System.out.println("FIN");
    }

    public String printMenu(Password password){

        boolean continuar = false;
        String option = "";

        do {
            System.out.println(" * GENERADOR DE CONTRASEÑAS * \n");

            System.out.println("0 - Mayusculas - " + (password.mayusculas?"Si":"No"));
            System.out.println("1 - Numeros    - " + (password.numeros?"Si":"No"));
            System.out.println("2 - Simbolos   - " + (password.simbolos?"Si":"No"));
            System.out.println("3 - Generar password");
            System.out.println("4 - Salir\n");

            System.out.println(" Seleccione las opciones para su password y pulse generar ");

            try {
                option = options[Integer.parseInt(entrada.nextLine())];
                continuar = true;
            } catch (Exception e) {
                System.out.println(" Opcion incorrecta ");
            }
        }while(!continuar);

        return option;
    }

    public int getLongitud(){
        boolean valid = false;
        int longitud = 0;
        System.out.println("Longitud de la password (entre 8 y 16): ");
        do {
            try {
                longitud = entrada.nextInt();
                if (longitud < 8 || longitud > 16) {
                    System.out.println("Longitud fuera del rango de valores\n");
                    System.out.println("introducir valor entre 8 y 16: ");
                } else {
                    valid = true;
                }
            }catch(Exception e){
                System.out.println("Valor incorrecto. Introducir valor entre 8-16");
            }
        } while (!valid);

        return longitud;
    }

    public String doPassword(Password password){

        List result = new ArrayList();
        Random random = new Random();
        boolean numbers = false;
        boolean upperCase = false;
        boolean special = false;
        char[] numeros = { '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' };
        char[] letras_minusculas = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
        char[] letras_mayusculas = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'C', 'W', 'X', 'Y', 'Z' };
        char[] caracteres_especiales = { '!', '@', '#', '$', '^', '&', '(', ')', '_', '=', '+', '-', '*', '/', '%', '<', '>', '?', '[', ']', '{', '}' };

        List all = new ArrayList<char[]>();
        all.add(letras_minusculas);

        password.longitud = getLongitud();

        for(int i = 0; i < password.longitud; i++) {

            if (password.numeros && !numbers) {
                result.add(numeros[random.nextInt(numeros.length - 1)]);
                all.add(numeros);
                numbers = true;
            } else if (password.mayusculas && !upperCase) {
                result.add(letras_mayusculas[random.nextInt(letras_mayusculas.length - 1)]);
                all.add(letras_mayusculas);
                upperCase = true;
            } else if (password.simbolos && !special) {
                result.add(caracteres_especiales[random.nextInt(caracteres_especiales.length - 1)]);
                all.add(caracteres_especiales);
                special = true;
            } else {
                char[] selection = (char[]) all.get(random.nextInt(all.size()));
                result.add(selection[random.nextInt(selection.length - 1)]);
            }
        }

        Collections.shuffle(result);
        return result.toString().replace("[","").replace("]","").replace(",","").replace(" ","");
    }

    public class Password{
        private boolean mayusculas,numeros,simbolos;
        private int longitud;
    }
}