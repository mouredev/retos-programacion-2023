import java.security.SecureRandom;
/*
Reto 3: 
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

 public class TaidaCR{

    private static final String CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=<>?";

    //STATIC: solo hay 1 instancia y se usa en toda la clase. Mejor que tener varias
    //FINAL: una vez creado random no se puede modificar, se convierte en una constante...
    //...si lo elimino funciona igual 
    private static final SecureRandom random = new SecureRandom ();

    public static String generatePass(int longitud){
        StringBuilder resultado=new StringBuilder();

        for (int i=0;i<longitud;i++){
            //elige un indice aleatorio de entre 0 y la long de la cadena de caracteres
            int indice = random.nextInt(CARACTERES.length());

            //coge el caracter en esa posición
            char caracter = CARACTERES.charAt(indice);

            //lo añade a la contraseña
            resultado.append(caracter);
        }
        //devuelve la contraseña
        return resultado.toString();
    }

    //Donde comienza la ejecución del programa. Métodos fuera. No sout fuera.
    public static void main(String[] args) {
        //Generar un número aleatorio entre 8 y 16 inclusive. El +8 para que empiece en 8.
        int longitud = random.nextInt(8) + 8;

        String pass=generatePass(longitud);
        System.out.println(pass);
    }
 }