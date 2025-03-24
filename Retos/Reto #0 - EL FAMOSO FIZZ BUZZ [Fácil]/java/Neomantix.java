public class Neomantix {

	public static void main(String[] args) {

		for(int i=1; i<=100; i++) {
			boolean divisiblePor3 = (i%3==0);
			boolean divisiblePor5 = (i%5==0);
			
			if(divisiblePor3 && divisiblePor5) {
				System.out.println(i + " fizzbuzz");
			} else if(divisiblePor3) {
				System.out.println(i + " fizz");
			} else if(divisiblePor5) {
				System.out.println(i + " buzz");
			} else {
				System.out.println(i);
			}
		}
		
	}

}

