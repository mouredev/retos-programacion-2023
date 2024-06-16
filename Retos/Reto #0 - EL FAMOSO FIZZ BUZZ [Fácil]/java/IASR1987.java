package reto_00_FIZZBUZZ;

public class IASR1987 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for(int i=1; i<=100;i++) {
			if(i%3==0) {
				if(i%5==0) {
					System.out.println("FIZZBUZZ");
				}else {
					System.out.println("FIZZ");
				}
			}else if(i%5==0) {
				System.out.println("BUZZ");
			}else {
				System.out.println(i);
			}
		}
	}

}
