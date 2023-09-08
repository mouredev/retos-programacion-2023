package com.retos.ej16;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {
		drawStaircase(0);
		drawStaircase(4);
		drawStaircase(-4);
	}

	public static void drawStaircase(int steps) {
		if (steps > 0) {
            // Escalera ascendente de izquierda a derecha
            for (int step = 0; step <= steps; step++) {
                String spaces = "  ".repeat(steps - step);
                String stepDraw = (step == 0) ? "_" : "_|";
                System.out.println(spaces + stepDraw);
            }
        } else if (steps < 0) {
            // Escalera descendente de izquierda a derecha
            for (int step = 0; step <= Math.abs(steps); step++) {
                String spaces = " ".repeat((step * 2));
                String stepDraw = (step == 0) ? "_" : "|_";
                System.out.println(spaces + stepDraw);
            }
        } else {
            System.out.println("__");
        }
	}

}
