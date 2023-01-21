public class miguelex {
    public static void main(String[] args) {
        System.out.println(generarClave(8, false, true, false));
        System.out.println(generarClave(10, true, true, false));
        System.out.println(generarClave(15, false, true, true));
        System.out.println(generarClave(9, true, true, true));
        System.out.println(generarClave(3, false, true, false));
        System.out.println(generarClave(28, false, true, false));
    }

    public static String generarClave(int max, boolean mayusculas, boolean numeros, boolean especiales) {
        String claveGenerada = "";
        String mayusculasStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String minusculasStr = "abcdefghijklmnopqrstuvwxyz";
        String numerosStr = "0123456789";
        String especialesStr = "!@#$%^&*()_+-=[]|,./?><";

        if (max < 8 || max > 16) {
            return "El numero de caracteres debe estar entre 8 y 16";
        }

        String caracteresUsados = minusculasStr;

        if (mayusculas) {
            caracteresUsados += mayusculasStr;
        }

        if (numeros) {
            caracteresUsados += numerosStr;
        }

        if (especiales) {
            caracteresUsados += especialesStr;
        }

        // Generamos la clave aleatoria de acuerdo al numero de caracteres seleccionado
        // por el usuario.
        for (int i = 0; i < max; i++) {
            int indexAleatorio = (int) (Math.random() * caracteresUsados.length());
            claveGenerada += caracteresUsados.substring(indexAleatorio, indexAleatorio + 1);
        }

        return claveGenerada;
    }
}