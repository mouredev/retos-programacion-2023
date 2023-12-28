package com.retos.ej14;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {

		System.out.println(decimalToOctal(255));
		System.out.println(decimalToHexadecimal(255));
	}

	private static String decimalToOctal(int numero) {
		if (numero == 0) {
			return "0";
		}

		StringBuilder octal = new StringBuilder();
		while (numero > 0) {
			int remainder = numero % 8;
			octal.insert(0, remainder);
			numero /= 8;
		}

		return octal.toString();
	}
	
	private static String decimalToHexadecimal(int decimal) {
        if (decimal == 0) {
            return "0";
        }

        StringBuilder hexadecimal = new StringBuilder();
        char[] hexChars = "0123456789ABCDEF".toCharArray(); // Caracteres hexadecimales

        while (decimal > 0) {
            int remainder = decimal % 16;
            hexadecimal.insert(0, hexChars[remainder]); // Insertar el carácter en la posición inicial
            decimal /= 16; // Dividir el número decimal entre 16
        }

        return hexadecimal.toString();
    }

}
