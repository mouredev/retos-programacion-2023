import java.util.Scanner;
import java.util.HashMap;

class Cryo {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in) ;
        System.out.println("Ingresa la palabra:");

        String dato = keyboard.nextLine();
        String resultado = change(dato.toLowerCase());

        System.out.println("Traducción: " + resultado);
        keyboard.close();
    }

    public static String change(String entry) {
        char[] tamarindo = entry.toCharArray(); 
        HashMap<Character, String> diccionario = new HashMap<Character, String>();
        diccionario.put('a',"4");
        diccionario.put('b',"I3");
        diccionario.put('c',"[");
        diccionario.put('d',")");
        diccionario.put('e',"3");
        diccionario.put('f',"|=");
        diccionario.put('g',"&");
        diccionario.put('h',"#");
        diccionario.put('i',"1");
        diccionario.put('j',",_|");
        diccionario.put('k',">|");
        diccionario.put('l',"1");
        diccionario.put('m',"/\\/\\");
        diccionario.put('n',"^/");
        diccionario.put('o',"0");
        diccionario.put('p',"|*");
        diccionario.put('q',"(_,)");
        diccionario.put('r',"I2");
        diccionario.put('s',"5");
        diccionario.put('t',"7");
        diccionario.put('u',"(_)");
        diccionario.put('v',"\\/");
        diccionario.put('w',"\\/\\/");
        diccionario.put('x',"><");
        diccionario.put('y',"j");
        diccionario.put('z',"2");
        String patata = "";
        for (char i: tamarindo) {
            patata += diccionario.get(i); 
        }
        
        return patata;
    }
}