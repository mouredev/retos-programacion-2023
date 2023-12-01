import java.util.Scanner;

public class MultiplicationTable {

	private static double userNumber = 0;
	private static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		if (readNumber()) {
			printMultiplicationTable();
		}
	}

	private static boolean readNumber() {
		try {
			System.out.println("Enter the number for which you want to know its multiplication table: \n");
			userNumber = sc.nextDouble();
			sc.close();
			return true;
		} catch (Exception e) {
			System.out.println("Error: please verify the data entered and try again");
			sc.close();
			return false;
		}

	}

	private static void printMultiplicationTable() {
		try {
			System.out.println("\n-----------MULTIPLICATION TABLE OF NUMBER " + userNumber +"-----------\n");
			for (int i = 1; i <= 10; i++) {
				System.out.println(userNumber + " x " + i + " = " + (userNumber * i));
			}
		} catch (Exception e) {
			System.out.println("Error: " + e.getMessage());
		}
	}

}