
package fizzbuzz;

/**
 *
 * @author jony1
 */
public class FizzBuzz {
    
    public static void main(String[] args) {
        for (int i = 1; i <= 100; i++) {
            
            
            if (i%3==0 && i%5 !=0) {
                System.out.println("\u001B[37m"+i+"\u001B[31m Fizz");
            }if (i%5==0 && i%3 !=0) {
                System.out.println("\u001B[37m"+i+"\u001B[34m Buzz");
            }if (i%3==0 && i%5 ==0){
                System.out.println("\u001B[37m"+i+"\u001B[32m Fizzbuzz");
            }if (i%3!=0 && i%5 !=0){
                System.out.println("\u001B[37m"+i);
            }
        }
    }
    
}
