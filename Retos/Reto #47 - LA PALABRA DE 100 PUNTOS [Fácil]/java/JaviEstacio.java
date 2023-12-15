import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.Normalizer;

public class JaviEstacio {
	public static void main(String[] args) {
		int puntos;
		char[] palabra;

		System.out.println("LA PALABRA DE LOS 100 PUNTOS");
		System.out.println("============================");
		System.out.println();
		System.out.println("El programa finaliza si se introduce una palabra de 100 puntos.");
		System.out.println("Ejemplo: Zoología");
		System.out.println("Z\to\to\tl\to\tg\tí\ta");
		System.out.println("26\t15\t15\t12\t15\t7\t9\t1 = 100 puntos.");
		System.out.println();

		try {
			do {
				System.out.println("Inserta la palabra: ");
				BufferedReader br = new BufferedReader(new InputStreamReader(System.in, System.console().charset()));

				palabra = limpiarPalabra(br.readLine()).toCharArray();
				puntos = calcularPuntos(palabra);
				System.out.println("Valor: " + puntos + " puntos.\n");
			} while (puntos != 100);
		} catch (IOException e) {
			System.out.println("\nEXCEPCIÓN leyendo la palabra. Fin de aplicación\n\n");
		}
	}

	private static String limpiarPalabra(String palabra) {
		palabra = palabra.trim().toLowerCase();
		palabra = Normalizer.normalize(palabra, Normalizer.Form.NFD);
		return palabra;
	}

	private static int calcularPuntos(char[] palabra) {
		int puntos = 0;
		boolean finPalabra = false;
		int minVal = 'a';
		int maxVal = 'z';
		Character[] separadores = { ' ', '\t', '\n' };

		for (char letra : palabra) {
			for (char separador : separadores) {
				if (letra == separador) {
					finPalabra = true; // Si se detecta un separador, se asume que la primera palabra ha finalizado y
														 // deja de sumar puntos
					break;
				} else if (letra >= minVal && letra <= maxVal) {
					puntos += (letra - (minVal - 1));
					break;
				}
			}
			if (finPalabra)
				break;
		}
		return puntos;
	}
}
