package com.mouredev.retos2023.reto0;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {

		for (int i = 1; i <= 100; i++) {
			boolean isMultipleOfThree = (i % 3 == 0);
			boolean isMultipleOfFive = (i % 5 == 0);
			
			if (isMultipleOfThree && isMultipleOfFive) System.out.println("fizzbuzz");
			else if (isMultipleOfThree) System.out.println("fizz");
			else if (isMultipleOfFive) System.out.println("buzz");
			else System.out.println(i);
		}
	}
}
