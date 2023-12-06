
public class miguelex {

    public enum Jugada {
        PIEDRA("🗿"),
        PAPEL("📄"),
        TIJERAS("✂️"),
        LAGARTO("🦎"),
        SPOCK("🖖");

        private String emoji;

        Jugada(String emoji) {
            this.emoji = emoji;
        }

        public String getEmoji() {
            return emoji;
        }
    }

    public static void main(String[] args) {
        Jugada[][] juegos = {
                { Jugada.PIEDRA, Jugada.TIJERAS },
                { Jugada.PIEDRA, Jugada.PAPEL },
                { Jugada.LAGARTO, Jugada.SPOCK }
        };

        System.out.println("Resultado: " + jugar(juegos));

        Jugada[][] juegos2 = {
                { Jugada.TIJERAS, Jugada.TIJERAS },
                { Jugada.PIEDRA, Jugada.PAPEL },
                { Jugada.LAGARTO, Jugada.SPOCK },
                { Jugada.PIEDRA, Jugada.PAPEL },
                { Jugada.LAGARTO, Jugada.SPOCK },
                { Jugada.PIEDRA, Jugada.PAPEL },
                { Jugada.SPOCK, Jugada.PAPEL },
                { Jugada.LAGARTO, Jugada.LAGARTO },
                { Jugada.SPOCK, Jugada.LAGARTO }
        };

        System.out.println("Resultado: " + jugar(juegos2));
    }

    private static String jugar(Jugada[][] juegos) {
        int p1Points = 0;
        int p2Points = 0;

        for (Jugada[] juego : juegos) {
            Jugada jugador1 = juego[0];
            Jugada jugador2 = juego[1];
            if (jugador1 == jugador2) {
                p1Points++;
                p2Points++;
            } else {
                switch (jugador1) {
                    case PIEDRA:
                        if (jugador2 == Jugada.TIJERAS || jugador2 == Jugada.LAGARTO) {
                            p1Points++;
                        } else {
                            p2Points++;
                        }
                        break;
                    case PAPEL:
                        if (jugador2 == Jugada.PIEDRA || jugador2 == Jugada.SPOCK) {
                            p1Points++;
                        } else {
                            p2Points++;
                        }
                        break;
                    case TIJERAS:
                        if (jugador2 == Jugada.PAPEL || jugador2 == Jugada.LAGARTO) {
                            p1Points++;
                        } else {
                            p2Points++;
                        }
                        break;
                    case LAGARTO:
                        if (jugador2 == Jugada.PAPEL || jugador2 == Jugada.SPOCK) {
                            p1Points++;
                        } else {
                            p2Points++;
                        }
                        break;
                    case SPOCK:
                        if (jugador2 == Jugada.TIJERAS || jugador2 == Jugada.PIEDRA) {
                            p1Points++;
                        } else {
                            p2Points++;
                        }
                        break;
                }
            }
        }

        if (p1Points == p2Points)
            return "Empate a " + p1Points + " puntos";
        else if (p1Points > p2Points)
            return "Gana el jugador 1 por " + p1Points + " puntos a " + p2Points;
        else
            return "Gana el jugador 2 por " + p2Points + " puntos a " + p1Points;
    }
}