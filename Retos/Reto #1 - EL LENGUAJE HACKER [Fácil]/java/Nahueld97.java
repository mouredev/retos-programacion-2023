import java.util.*;

public class Nahueld97 {

	public static void main(String[] args) {
		String in,out;
		Scanner teclado = new Scanner(System.in);
		HashMap<Character, String> traductor = new HashMap<Character,String>();
		
		//letras
		traductor.put('a', "4");
		traductor.put('b', "I3");
		traductor.put('c', "[");
		traductor.put('d', ")");
		traductor.put('e', "3");
		traductor.put('f', "|=");
		traductor.put('g', "&");
		traductor.put('h', "#");
		traductor.put('i', "1");
		traductor.put('j', ",_|");
		traductor.put('k', ">|");
		traductor.put('l', "1");
		traductor.put('m', "/\\/\\");
		traductor.put('n', "^/");
		traductor.put('o', "0");
		traductor.put('p', "|*");
		traductor.put('q', "(_,)");
		traductor.put('r', "I2");
		traductor.put('s', "5");
		traductor.put('t', "7");
		traductor.put('u', "(_)");
		traductor.put('v', "\\/");
		traductor.put('w', "\\/\\/");
		traductor.put('x', "><");
		traductor.put('y', "j");
		traductor.put('z', "2");
		
		//numeros
		traductor.put('0', "o");
		traductor.put('1', "L");
		traductor.put('2', "R");
		traductor.put('3', "E");
		traductor.put('4', "A");
		traductor.put('5', "S");
		traductor.put('6', "b");
		traductor.put('7', "T");
		traductor.put('8', "B");
		traductor.put('9', "g");
		
		System.out.println("Ingresa el texto a traducir: ");
		in = teclado.nextLine();
		out = traducir(in, traductor);
		System.out.println(out);
		teclado.close();
	}
	
	public static String traducir(String input, Map<Character, String> traductor) {
		String output = "",aux;
		aux = input.toLowerCase();
		for (char letra : aux.toCharArray()) {
			if (traductor.containsKey(letra)) {
				output += traductor.get(letra);
			}else {
				output += letra;
			}
		}
		input.toLowerCase();
		
		return output;
	}

}
