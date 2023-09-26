package com.retos.ej27;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {
		countdown(10, 1);
	}

	private static void countdown(int start, int interval) {
		if (start <= 0 || interval <= 0) {
			System.out.println("Los parámetros deben ser números enteros positivos.");
			return;
		}

		for (; start >= 0;start = switch (start) {
		case 0 -> -1;
		default -> {
			System.out.println(start);
			yield start - 1;
		}
		}) {
			try {
				Thread.sleep(interval * 1000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}
