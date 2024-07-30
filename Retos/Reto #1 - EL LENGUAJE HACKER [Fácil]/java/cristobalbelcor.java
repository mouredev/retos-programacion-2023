/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

import java.util.Scanner;

public class Main {
    private String texto;
    private String nuevoTexto;
    public int tamañoTexto(){
        return texto.length();
    }

    public void textoMinuscula(){
        texto =  texto.toLowerCase();
    }

    public Main() {
        nuevoTexto = "";
    }

    public void solicitarTexto(){
        Scanner cs = new Scanner(System.in);

        System.out.println("Introduce un texto");
        texto = cs.nextLine();
    }

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


    public static void main(String[] args){
        Main alphabeth = new Main();

        alphabeth.solicitarTexto();
        alphabeth.textoMinuscula();
        for (int i = 0; i < alphabeth.tamañoTexto(); i++) {

            switch (alphabeth.getTexto().charAt(i)) {
                case 'a':
                case 'á':
                case 'à':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "4");
                    break;
                case 'b':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "I3");
                    break;
                case 'c':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "[");
                    break;
                case 'd':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + ")");
                    break;
                case 'e':
                case 'é':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "3");
                    break;
                case 'f':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "|=");
                    break;
                case 'g':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "&");
                    break;
                case 'h':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "#");
                    break;
                case 'i':
                case 'í':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "1");
                    break;
                case 'j':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + ",_|");
                    break;
                case 'k':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + ">|");
                    break;
                case 'l':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "1");
                    break;
                case 'm':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "/\\/\\");
                    break;
                case 'n':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "^/");
                    break;
                case 'o':
                case 'ó':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "0");
                    break;
                case 'p':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "|*");
                    break;
                case 'q':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "(_,)");
                    break;
                case 'r':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "I2");
                    break;
                case 's':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "5");
                    break;
                case 't':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "7");
                    break;
                case 'ú':
                case 'u':
                case 'ü':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "(_)");
                    break;
                case 'v':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "\\/");
                    break;
                case 'w':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "\\/\\/");
                    break;
                case 'x':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "><");
                    break;
                case 'y':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "j");
                    break;
                case 'z':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "2");
                    break;
                case '1':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "L");
                    break;
                case '2':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "R");
                    break;
                case '3':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "E");
                    break;
                case '4':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "A");
                    break;
                case '5':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "S");
                    break;
                case '6':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "b");
                    break;
                case '7':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "T");
                    break;
                case '8':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "B");
                    break;
                case '9':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "g");
                    break;
                case '0':
                    alphabeth.setNuevoTexto(alphabeth.getNuevoTexto() + "o");
                    break;


            }

        }
        System.out.println(alphabeth.nuevoTexto);

    }

}
