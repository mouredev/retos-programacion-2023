public class Elez95 {
	
	public static void main(String [] args) {
		
		for(int i = 1; i <= 100; i++) {
			
			if(es_multiplo_de_3_y_5(i)) {
				System.out.println("fizzbuzz");
			} 
			else if(es_multiplo_de_3(i)) {
				System.out.println("fizz");
			}
			else if(es_multiplo_de_5(i)) {
				System.out.println("buzz");
			}
			else {
				System.out.println(i);
			}
				
			
		}
		
	}
	
	
	private static boolean es_multiplo_de_3_y_5(int numero) {
		return (numero % 3 == 0 && numero % 5 == 0) ? true : false;		
	}
	
	private static boolean es_multiplo_de_3(int numero) {
		return (numero % 3 == 0) ? true: false;
	}

	private static boolean es_multiplo_de_5(int numero) {
		return (numero % 5 == 0) ? true: false;
	}
}