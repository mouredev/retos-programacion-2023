/**
 * 
 */
package ec.com.vijes.retos;

/**
 * @author vijes
 *
 */
public class vijesMain {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
        fizzbuzzReto0();
	}

	public static void fizzbuzzReto0() {
		System.out.println("Inicio metodo fizzbuzz");
		for (int i = 1; i <= 100; i++ ) {
			if ( i%3 == 0 && i%5 == 0 ) {
				System.out.println("fizzbuzz");
			} else if ( i%3 == 0 ) {
				System.out.println("fizz");
			} else if ( i%5 == 0 ) {
				System.out.println(i+"buzz");
			} else {
				System.out.println(i);
			}
		}
	}
}
