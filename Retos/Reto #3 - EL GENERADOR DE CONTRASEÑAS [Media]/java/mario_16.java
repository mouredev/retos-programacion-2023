import java.util.*;

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

public class mario_16 {

    public static void main(String[] args) {
        Scanner escaner = new Scanner(System.in);

        System.out.println("Ingrese la longitud de su contraseña");
        int longitud = escaner.nextInt();

        if (longitud < 8 || longitud > 16) {
            System.out.println("La longitud de la contraseña no es valida");
        }else{
            System.out.println("Ingrese cantidad de mayusculas");
            int cantMayus = escaner.nextInt();
            System.out.println("Ingrese cantidad de numeros");
            int cantNumeros = escaner.nextInt();
            System.out.println("Ingrese cantidad de simbolos");
            int cantSimbolos = escaner.nextInt();

            int suma = cantMayus + cantNumeros + cantSimbolos;
            if (suma != longitud){
                System.out.println("La suma de los parametros ingresados no coinciden con la longitud de la contraseña");
            }else{
                generarContraseña(longitud, cantMayus, cantNumeros, cantSimbolos);
            }
        }

    }

    private static void generarContraseña(int longitud, int cantMayus, int cantNumeros, int cantSimbolos) {
        String conjuntoMayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
        String conjuntoNumeros = "0123456789";
        String conjuntoSimbolos = "/\\+*-!·$%&()=?¿º|@#~€¬¡{}[],.;^:_çÇ`";
        List<String> listaCaracteres = new ArrayList<>();
        Random random = new Random();

        if (cantMayus > 0 ){
            for (int i=0; i < cantMayus; i++){
                int randomInt = random.nextInt(conjuntoMayusculas.length());
                char randomChar = conjuntoMayusculas.charAt(randomInt);
                listaCaracteres.add(String.valueOf(randomChar));
            }
        }
        if (cantNumeros > 0){
            for (int i=0; i < cantNumeros; i++){
                int randomInt = random.nextInt(conjuntoNumeros.length());
                char randomChar = conjuntoNumeros.charAt(randomInt);
                listaCaracteres.add(String.valueOf(randomChar));
            }
        }
        if (cantSimbolos > 0){
            for (int i=0; i < cantSimbolos; i++){
                int randomInt = random.nextInt(conjuntoSimbolos.length());
                char randomChar = conjuntoSimbolos.charAt(randomInt);
                listaCaracteres.add(String.valueOf(randomChar));
            }
        }

        Collections.shuffle(listaCaracteres);
        System.out.println(listaCaracteres.toString().replace("[", "")
                .replace(", ", "").replace("]", ""));

    }

}
