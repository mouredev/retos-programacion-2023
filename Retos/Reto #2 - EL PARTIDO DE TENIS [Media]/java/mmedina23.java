import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicReference;

/**
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * <p>
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 * 15 - Love
 * 30 - Love
 * 30 - 15
 * 30 - 30
 * 40 - 30
 * Deuce
 * Ventaja P1
 * Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
 */
public class R2_PartidoTenis {

    private static final String JUGADOR_1 = "p1";
    private static final String JUGADOR_2 = "p2";

    public static void main(String[] args) {
        puntuacion(List.of("p2", "p2", "p1", "p2", "p1", "p1", "p2", "p2", "p1"));
    }

    private static void puntuacion(List<String> puntos) {
        AtomicInteger puntosJugador1 = new AtomicInteger();
        AtomicInteger puntosJugador2 = new AtomicInteger();
        AtomicReference<String> mensaje = new AtomicReference<>();
        mensaje.set("");

        puntos.stream()
                .filter(i -> JUGADOR_1.equals(i) || JUGADOR_2.equals(i))
                .takeWhile(i -> !mensaje.get().contains("Ha ganado"))
                .forEach(i -> {
                    if (i.equals(JUGADOR_1)) {
                        puntosJugador1.set(sumaPuntos(puntosJugador1));
                    } else if (i.equals(JUGADOR_2)) {
                        puntosJugador2.set(sumaPuntos(puntosJugador2));
                    }

                    mensaje.set(comparacion(puntosJugador1, puntosJugador2));
                    System.out.println(mensaje.get());
                });
    }

    private static String comparacion(AtomicInteger pj1, AtomicInteger pj2) {
        StringBuilder mostrar = new StringBuilder();

        if (pj1.get() == pj2.get()) {
            mostrar.append("Deuce");
            return mostrar.toString();
        }

        if ((pj1.get() < 40) && (pj2.get() > 40)) {
            mostrar.append("Ha ganado p2");
            return mostrar.toString();
        }

        if ((pj2.get() < 40) && (pj2.get() > 40)) {
            mostrar.append("Ha ganado p1");
            return mostrar.toString();
        }

        if (pj1.get() >= 40 && pj2.get() >= 40) {
            int diferecia = pj1.get() - pj2.get();
            if (diferecia == 10) {
                return mostrar.append("Ventaja p1").toString();
            } else if (diferecia == -10) {
                return mostrar.append("Ventaja p2").toString();
            }

            if (diferecia == 20) {
                return mostrar.append("Ha ganado el p1").toString();
            } else if (diferecia == -20) {
                return mostrar.append("Ha ganado p2").toString();
            }
        }

        if (pj1.get() == 0) {
            mostrar.append("LOVE");
            mostrar.append(" - ");
        } else {
            mostrar.append(pj1);
            mostrar.append(" - ");
        }

        if (pj2.get() == 0) {
            mostrar.append("LOVE");
        } else {
            mostrar.append(pj2);
        }

        return mostrar.toString();
    }

    private static int sumaPuntos(AtomicInteger punto) {
        int puntosJugador = punto.get();
        if (punto.get() >= 30) {
            puntosJugador = puntosJugador + 10;
        } else {
            puntosJugador = puntosJugador + 15;
        }

        return puntosJugador;
    }
}
