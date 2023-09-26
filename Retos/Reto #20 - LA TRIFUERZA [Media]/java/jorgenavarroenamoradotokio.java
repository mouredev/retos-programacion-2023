package com.retos.ej20;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {
		drawTriforce(2);
	}

	public static void drawTriforce(int rows) {
		for (int row = 0; row < rows * 2; row++) {
			if (row < rows) {
				String startSpace = " ".repeat(((2 * rows) - 1) - row);
				String printRow = "*".repeat((2 * (row + 1)) - 1);
				System.out.println(startSpace + printRow);
			} else {
				int currentRow = row - rows;
				String startSpace = " ".repeat((rows - currentRow) - 1);
				String middleSpace = " ".repeat((2 * (rows - currentRow)) - 1);
				String printRow = "*".repeat((2 * (currentRow + 1)) - 1);
				System.out.println(startSpace + printRow + middleSpace + printRow);
			}
		}
	}

}
