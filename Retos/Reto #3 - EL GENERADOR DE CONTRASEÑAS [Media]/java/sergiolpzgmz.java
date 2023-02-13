import java.util.ArrayList;
import java.util.Scanner;

public class sergiolpzgmz {
    /*
     * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
     * Podrás configurar generar contraseñas con los siguientes parámetros:
     * - Longitud: Entre 8 y 16.
     * - Con o sin letras mayúsculas.
     * - Con o sin números.
     * - Con o sin símbolos.
     * (Pudiendo combinar todos estos parámetros entre ellos)
     */


    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String[] diccionarioLetrasMayusc = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","K","R","S","T","U","V","W","X","Y","Z"};
        String[] diccionarioSimbolos ={"-","@","#","~","$","%","&","*","<",">"};
        String[] diccionarioNumeros = {"1","2","3","4","5","6","7","8","9","0"};
        ArrayList<String>seleccionUsuario = new ArrayList<String>();

        System.out.println("=================================================================");
        System.out.println("Generador de contraseñas");
        System.out.println("Introduce la longitud de la contraseña (Entre 8 y 16 caracteres):");
        int longitudContrasenha = entrada.nextInt();
        entrada.nextLine();

        System.out.println("Escoja las siguientes opciones: ");
        System.out.println("Letras mayusculas?(SI/NO): ");
        String letrasMayusculas = entrada.nextLine().toLowerCase();

        if(letrasMayusculas.equals("si")){
            for (int i = 0; i < diccionarioLetrasMayusc.length; i++) {
                seleccionUsuario.add(diccionarioLetrasMayusc[i]);
                seleccionUsuario.add(diccionarioLetrasMayusc[i].toLowerCase());
            }
        } else if(letrasMayusculas.equals("no")) {
            for (int i = 0; i < diccionarioLetrasMayusc.length; i++) {
                seleccionUsuario.add(diccionarioLetrasMayusc[i].toLowerCase());
            }
        } else{
            System.out.println("Error introduce 1 o 2");
        }

        System.out.println("Numeros?(SI/NO): ");
        String numeros = entrada.nextLine().toLowerCase();

        if(numeros.equals("si")){
            for (int i = 0; i < diccionarioNumeros.length; i++) {
                seleccionUsuario.add(diccionarioNumeros[i]);
            }
        }

        System.out.println("Simbolos?(SI/NO): ");
        String simbolos = entrada.nextLine().toLowerCase();

        if(simbolos.equals("si")){
            for (int i = 0; i < diccionarioSimbolos.length; i++) {
                seleccionUsuario.add(diccionarioSimbolos[i]);
            }
        }
        ArrayList<String>contrasenhaFinal = new ArrayList<String>();
        while (contrasenhaFinal.size()!=longitudContrasenha){
            int numeroAleatorio = (int)(Math.random()*seleccionUsuario.size()+1);

            for (int j = 0; j < seleccionUsuario.size() ; j++) {
                if(j==numeroAleatorio) contrasenhaFinal.add(seleccionUsuario.get(j));
            }
        }
        System.out.println("Contraseña: ");
        for (int i = 0; i < contrasenhaFinal.size(); i++) {
            System.out.print(contrasenhaFinal.get(i));
        }
        System.out.println();
        System.out.println("===========================================================");

        entrada.close();
        
        
        
        






    }
}
