public class Reto0_FizzBuzz {

	public static void main(String[] args) {
		
		String texto = "";
		  
		for (int i = 1; i>=1 && i<=100; i++) {
			
			if (i%3==0 && i%5==0){ // multiplos de ambos. la condicion más excluyente primero
				texto = "FizzBuzz";
				System.out.println(texto);
					
			} else if (i%5==0) { // multiplos de 5
				texto = "Buzz";
				System.out.println(texto);
				
			} else if (i%3==0) {// multiplos de ambos
				texto = "Fizz";
				System.out.println(texto);
				
				} else { // número
					System.out.print(i + "\n");
				}
			
		}

	}

}
