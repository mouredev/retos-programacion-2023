import java.awt.Font;
import java.awt.GridLayout;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingUtilities;

public class JaviEstacio {
	final static String COCHE_VERDE = "🚙";
	final static String COCHE_ROJO = "🚗";
	final static String META = "🏁";
	final static String ARBOL = "🌲";
	final static String CRASH = "💥";
	static JLabel jlabRojo, jlabVerde, jlabGanador;
	static Pista pistaRojo, pistaVerde;

	public JaviEstacio() {


		JFrame jfrm = new JFrame("Reto #46 de 2023");
		jfrm.setLayout(new GridLayout(3, 1));
		jfrm.setSize(800, 300);
		jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		jlabRojo = new JLabel("");
		jlabRojo.setFont(new Font("Ubuntu", Font.PLAIN, 48));
		jlabVerde = new JLabel("");
		jlabVerde.setFont(new Font("Ubuntu", Font.PLAIN, 48));
		jlabGanador = new JLabel("");
		jlabGanador.setFont(new Font("Ubuntu", Font.PLAIN, 48));
		actualizarPistas();
		jfrm.add(jlabRojo);
		jfrm.add(jlabVerde);
		jfrm.add(jlabGanador);
		jfrm.setVisible(true);

	}

	public static void main(String[] args) {
		pistaRojo = new Pista(JaviEstacio.COCHE_ROJO, 10);
		pistaVerde = new Pista(JaviEstacio.COCHE_VERDE, 10);
		SwingUtilities.invokeLater(new Runnable() {
			public void run() {
				new JaviEstacio();
			}
		});

		while (pistaRojo.posicionCoche >= 0 && pistaVerde.posicionCoche >= 0) {
			try {
				Thread.sleep(1000);
				avanzarCoches();
				actualizarPistas();
				System.out.println();
			} catch (InterruptedException e) {
				System.out.println("Main thread interrupted.");
			}
		}
		validarGanador(pistaRojo, pistaVerde);
	}

	static void actualizarPistas() {
		jlabRojo.setText(vistaPista(pistaRojo));
		jlabVerde.setText(vistaPista(pistaVerde));
	}

	static String vistaPista(Pista pista) {
		StringBuilder sb = new StringBuilder(JaviEstacio.META);
		for (String s : pista.pista)
			sb.append(s);
		return sb.toString();
	}

	static void avanzarCoches() {
		pistaRojo.avanzarCoche();
		pistaVerde.avanzarCoche();
	}

	static void validarGanador(Pista p1, Pista p2) {
		if (p1.posicionCoche < 0 && p2.posicionCoche < 0)
			jlabGanador.setText("EMPATE");
		else if (p1.posicionCoche < 0)
			jlabGanador.setText(p1.coche + " GANA\n");
		else
			jlabGanador.setText(p2.coche + " GANA\n");
	}

	static class Pista {
		public String coche;
		public int posicionCoche;
		public String[] pista;
		final int LONGITUD_DEFECTO = 10;
		final String ARBOL = "🌲";
		final String CRASH = "💥";
		Random rand = new Random();

		Pista(String coche, int longitud) {
			this.coche = coche;

			int arboles = rand.nextInt(3) + 1;

			this.pista = crearPista(longitud, arboles);
			this.posicionCoche = this.pista.length - 1;
			this.pista[posicionCoche] = this.coche;
		}

		private String[] crearPista(int longitud, int arboles) {
			String[] pista;

			if (longitud < (arboles))
				longitud = this.LONGITUD_DEFECTO;

			pista = new String[longitud];

			// Crear pista vacía
			for (int i = 0; i < longitud - 1; i++) {
				// pista[longitud-1] se reserva para la posición inicial del coche
				pista[i] = "_";
			}

			// Colocar árboles
			do {
				int posicionArbol = rand.nextInt(longitud - 2);
				if (pista[posicionArbol] != JaviEstacio.ARBOL) {
					pista[posicionArbol] = JaviEstacio.ARBOL;
					arboles--;
				}
			} while (arboles > 0);

			return pista;
		}

		public void avanzarCoche() {
			if (pista[posicionCoche].compareTo(JaviEstacio.CRASH) == 0)
				pista[posicionCoche] = coche;
			else {
				int avance = rand.nextInt(3) + 1;
				posicionCoche = posicionCoche - avance;
				if (posicionCoche >= 0) {
					if (pista[posicionCoche].compareTo(JaviEstacio.ARBOL) == 0) {
						pista[posicionCoche] = JaviEstacio.CRASH;
					} else {
						pista[posicionCoche] = coche;
					}
					for (int i = posicionCoche + 1; i < pista.length; i++)
						pista[i] = "";
				}
				else {
					for (int i = 0; i < pista.length; i++)
						pista[i] = "";
				}
			}
		}
	}
}
