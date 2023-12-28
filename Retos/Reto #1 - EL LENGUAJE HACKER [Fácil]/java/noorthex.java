/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

public class noorthex {
	
	public void leet()
	{
		Map<Character, String> map = new HashMap<Character, String>();
		
		map.put('A', "4"); map.put('B', "I3"); map.put('C', "["); 
		map.put('D', ")"); map.put('E', "3");  map.put('F', "|="); 
		map.put('G', "&"); map.put('H', "#");  map.put('I', "1");
		map.put('J', ",_|"); map.put('K', ">|");  map.put('L', "£");
		map.put('M', "/\\/\\"); map.put('N', "^/");  map.put('O', "0");
		map.put('P', "|*"); map.put('Q', "(_,)");  map.put('R', "I2");
		map.put('S', "5"); map.put('T', "7");  map.put('U', "(_)");
		map.put('V', "\\/"); map.put('W', "\\/\\/");  map.put('X', "><");
		map.put('Y', "j"); map.put('Z', "2");  
		
		Scanner lectura = new Scanner (System.in);
		System.out.println("Ingrese el texto");
		String txt = lectura.next();
		String compact = txt.replaceAll(" ","").trim().toUpperCase();
		 char[] caracteres = compact.toCharArray();
		 for(int i=0;i<caracteres.length;i++)
		 {
			 System.out.print(map.get(caracteres[i]));
		 }	 
	}
}