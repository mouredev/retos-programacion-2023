import java.util.Scanner;

/**
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje se
 * caracteriza por sustituir caracteres alfanuméricos. - Utiliza esta tabla
 * (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) con el alfabeto y
 * los números en "leet". (Usa la primera opción de cada transformación. Por
 * ejemplo "4" para la "a")
 *
 * @author Abel
 */
public class AbelADE {
    /**
     * Texto que vamos a traducir.
     */
    private String texto;
    
    /**
     * Texto traducido.
     */
    private String nuevoTexto;

    public String getTexto() {
        return texto;
    }

    public void setTexto(String texto) {
        this.texto = texto;
    }

    public String getNuevoTexto() {
        return nuevoTexto;
    }

    public void setNuevoTexto(String nuevoTexto) {
        this.nuevoTexto = nuevoTexto;
    }

    /**
     * Constructor del programa.
     */
    public AbelADE() {
        nuevoTexto = "";
    }

    /**
     * Pide el texto a traducir al usuario.
     */
    public void pedirTexto() {
        Scanner scan = new Scanner(System.in);

        System.out.println("Introduce un texto:");
        texto = scan.nextLine();
    }

    /**
     * Devuelve el tamaño del texto a traducir.
     * @return el tamaño del texto a traducir.
     */
    public int tamañoTexto() {
        return texto.length();
    }

    /**
     * Pone el texto a traducir en minúsculas.
     */
    public void textoEnMinusculas() {
        texto = texto.toLowerCase();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        AbelADE textTransform = new AbelADE();

        //Pido el texto
        textTransform.pedirTexto();

        //Paso el texto a minúsculas
        textTransform.textoEnMinusculas();

        //Recorro el texto
        for (int i = 0; i < textTransform.tamañoTexto(); i++) {
            //Realizo la transformación de cada carácter y lo añado a nuevoTexto
            switch (textTransform.getTexto().charAt(i)) {
                //Transformación del abecedario
                case 'a':
                case 'á':
                case 'à':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "4");
                    break;
                case 'b':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "I3");
                    break;
                case 'c':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "[");
                    break;
                case 'd':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + ")");
                    break;
                case 'e':
                case 'é':
                case 'è':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "3");
                    break;
                case 'f':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "|=");
                    break;
                case 'g':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "&");
                    break;
                case 'h':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "#");
                    break;
                case 'l':
                case 'i':
                case 'í':
                case 'ì':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "1");
                    break;
                case 'j':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + ",_|");
                    break;
                case 'k':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + ">|");
                    break;
                case 'm':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "/\\/\\");
                    break;
                case 'n':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "^/");
                    break;
                case 'o':
                case 'ó':
                case 'ò':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "0");
                    break;
                case 'p':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "|*");
                    break;
                case 'q':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "(_,)");
                    break;
                case 'r':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "I2");
                    break;
                case 's':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "5");
                    break;
                case 't':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "7");
                    break;
                case 'u':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "(_)");
                    break;
                case 'v':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "\\/");
                    break;
                case 'w':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "\\/\\/");
                    break;
                case 'x':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "><");
                    break;
                case 'y':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "j");
                    break;
                case 'z':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "2");
                    break;
                //Transformación de números
                case '1':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "L");
                    break;
                case '2':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "R");
                    break;
                case '3':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "E");
                    break;
                case '4':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "A");
                    break;
                case '5':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "S");
                    break;
                case '6':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "b");
                    break;
                case '7':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "T");
                    break;
                case '8':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "B");
                    break;
                case '9':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "g");
                    break;
                case '0':
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + "o");
                    break;
                default:
                    textTransform.setNuevoTexto(textTransform.getNuevoTexto() + textTransform.getTexto().charAt(i));
            }

        }

        //Muestro por consola el texto resultado de la transformación
        System.out.println(textTransform.nuevoTexto);

    }

}
