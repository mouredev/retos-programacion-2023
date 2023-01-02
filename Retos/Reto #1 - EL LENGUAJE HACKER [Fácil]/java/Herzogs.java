import java.util.HashMap;
import java.util.Map;

public class Herzogs {

    public static void generarLenguajeHacker(Map<Character, String> lng) {
        lng.put('a', "4");
        lng.put('b', "I3");
        lng.put('c',"[");
        lng.put('d',")");
        lng.put('e',"3");
        lng.put('f',"|=");
        lng.put('g',"&");
        lng.put('h',"#");
        lng.put('i',"1");
        lng.put('j',",_|");
        lng.put('k',">|");
        lng.put('l',"1");
        lng.put('m',"^^");
        lng.put('n',"^/");
        lng.put('o',"0");
        lng.put('p',"|*");
        lng.put('q',"(_,)");
        lng.put('r',"I2");
        lng.put('s',"5");
        lng.put('t',"7");
        lng.put('u',"(_)");
        lng.put('v',"|/");
        lng.put('w',"2u");
        lng.put('x',"><");
        lng.put('y',"j");
        lng.put('z',"2");
        lng.put('1',"L");
        lng.put('2',"R");
        lng.put('3',"E");
        lng.put('4',"A");
        lng.put('5',"S");
        lng.put('6',"b");
        lng.put('7',"T");
        lng.put('8',"B");
        lng.put('9',"g");
        lng.put('0',"o");
    }


    public static void main(String[] args) {
        Map<Character, String> leng = new HashMap<>();
        generarLenguajeHacker(leng);
        String palabra = "Adios muñdo cru3l";
        StringBuilder enc = new StringBuilder();
        System.out.println("PALABRA DESENCRIPTADA: " + palabra);
        for (Character idx: palabra.toLowerCase().toCharArray()) {
            String dev = leng.get(idx);
            enc.append((dev !=null)?dev:idx);
        }
        System.out.println("PALABRA ENCRIPTADA: "+ enc);
    }
}
