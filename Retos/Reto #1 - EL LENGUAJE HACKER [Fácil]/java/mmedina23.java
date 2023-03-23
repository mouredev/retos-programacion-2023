import java.util.Arrays;

public class LenguajeHacker {

    public static void main(String[] args) {
        System.out.println(toLeet("HOLA"));
    }

    private static String toLeet(String palabra) {
        String[] vector = (palabra.toLowerCase()).split("");
        StringBuilder leet = new StringBuilder();
        Arrays.stream(vector).forEach(i -> {
            leet.append(Equivalente.buscar(i));
        });

        return leet.toString();
    }

    enum Equivalente {
        _a("4"),
        _b("I3"),
        _c("["),
        _d(")"),
        _e("3"),
        _f("|="),
        _g("&"),
        _h("#"),
        _i("1"),
        _j(",_|"),
        _k(">|"),
        _l("1"),
        _m("^^"),
        _n("^/"),
        _o("0"),
        _p("|*"),
        _q("(_,)"),
        _r("I2"),
        _s("5"),
        _t("7"),
        _u("(_)"),
        _v("|/"),
        _w("2u"),
        _x("><"),
        _y("j"),
        _z("2"),
        _1("L"),
        _2("R"),
        _3("E"),
        _4("A"),
        _5("S"),
        _6("b"),
        _7("T"),
        _8("B"),
        _9("g"),
        _0("o");
        public final String code;

        equivalente(String code) {
            this.code = code;
        }

        public static String buscar(String valor) {
            for (equivalente eq : values()) {
                if (eq.name().equals("_"+valor)) {
                    return eq.code;
                }
            }
            return valor;
        }
    }

}