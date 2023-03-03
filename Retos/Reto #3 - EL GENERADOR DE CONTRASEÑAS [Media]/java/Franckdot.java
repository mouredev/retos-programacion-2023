package generador.de.contraseñas;
import java.util.Scanner;
import java.util.Random;
import java.util.HashMap;
public class Franckdot {
   
    public static void main(String[] args) {
        HashMap newHash = new HashMap();
        Scanner newScan = new Scanner(System.in);
        Random newRan = new Random();
        System.out.println("Hola Usuario Nuevo"
                + "para generar una nueva contraseña debes ingresar un digito "
                + "igual a 8 o mayor y menor o igual a 16");
        int tamCon = newScan.nextInt();
        if(tamCon >= 8 && tamCon <= 16){
        String newPass = "";
        for(int i=0; i < tamCon; i++){
            switch (newRan.nextInt(3)) {
                case 0:
                    newPass += newRan.nextInt(9);
                    break;
                case 1:
                    newHash.put(0, "a");
                    newHash.put(1, "b");
                    newHash.put(2, "c");
                    newHash.put(3, "d");
                    newHash.put(4, "e");
                    newHash.put(5, "f");
                    newHash.put(6, "g");
                    newHash.put(7, "h");
                    newHash.put(8, "i");
                    newHash.put(9, "j");
                    newHash.put(10, "k");
                    newHash.put(11, "l");
                    newHash.put(12, "m");
                    newHash.put(13, "n");
                    newHash.put(14, "ñ");
                    newHash.put(15, "o");
                    newHash.put(16, "p");
                    newHash.put(17, "q");
                    newHash.put(18, "r");
                    newHash.put(19, "s");
                    newHash.put(20, "t");
                    newHash.put(21, "u");
                    newHash.put(22, "v");
                    newHash.put(23, "w");
                    newHash.put(24, "x");
                    newHash.put(25, "y");
                    newHash.put(26, "z");
                    newPass += newHash.get(newRan.nextInt(27));
                    break;
                case 2:
                    newHash.put(0, "A");
                    newHash.put(1, "B");
                    newHash.put(2, "C");
                    newHash.put(3, "D");
                    newHash.put(4, "E");
                    newHash.put(5, "F");
                    newHash.put(6, "G");
                    newHash.put(7, "H");
                    newHash.put(8, "I");
                    newHash.put(9, "J");
                    newHash.put(10, "K");
                    newHash.put(11, "L");
                    newHash.put(12, "M");
                    newHash.put(13, "N");
                    newHash.put(14, "Ñ");
                    newHash.put(15, "O");
                    newHash.put(16, "P");
                    newHash.put(17, "Q");
                    newHash.put(18, "R");
                    newHash.put(19, "S");
                    newHash.put(20, "T");
                    newHash.put(21, "U");
                    newHash.put(22, "V");
                    newHash.put(23, "W");
                    newHash.put(24, "X");
                    newHash.put(25, "Y");
                    newHash.put(26, "Z");
                    newPass += newHash.get(newRan.nextInt(27));
                    break;
                default:
                    break;
            }
        }
        System.out.println("Esta es su nueva contraseña: " + newPass);
        }else{
            System.out.println("Agrego una valor no deseado, por favor vuelva a intentarlo!!!!");
        }
        
    }
}
