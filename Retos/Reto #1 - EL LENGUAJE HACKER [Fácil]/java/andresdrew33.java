import java.util.Scanner;

public class Reto_1 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String cadena;
        
        System.out.println("Escribe una frase:");
        cadena=sc.nextLine();
        cadena=cadena.replace("a", "4");
        cadena=cadena.replace("b", "13");
        cadena=cadena.replace("c", "[");
        cadena=cadena.replace("d", ")");
        cadena=cadena.replace("e", "3");
        cadena=cadena.replace("f", "|=");
        cadena=cadena.replace("g", "&");
        cadena=cadena.replace("h", "#");
        cadena=cadena.replace("i", "1");
        cadena=cadena.replace("j", ",_|");
        cadena=cadena.replace("k", ">|");
        cadena=cadena.replace("l", "1");
        cadena=cadena.replace("m", "/\\/\\");
        cadena=cadena.replace("n", "^/");
        cadena=cadena.replace("o", "0");
        cadena=cadena.replace("p", "|*");
        cadena=cadena.replace("q", "(_,)");
        cadena=cadena.replace("r", "|2");
        cadena=cadena.replace("s", "5");
        cadena=cadena.replace("t", "7");
        cadena=cadena.replace("u", "(_)");
        cadena=cadena.replace("v", "\\/");
        cadena=cadena.replace("w", "\\/\\/");
        cadena=cadena.replace("x", "><");
        cadena=cadena.replace("y", "j");
        cadena=cadena.replace("z", "2");
        
        System.out.println("El sistema te devuelve:");
        System.out.println(cadena);
       
    }
    
}
