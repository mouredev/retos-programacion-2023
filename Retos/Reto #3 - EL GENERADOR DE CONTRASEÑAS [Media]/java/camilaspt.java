import java.sql.Array;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        /*
         * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
         * Podrás configurar generar contraseñas con los siguientes parámetros:
         * - Longitud: Entre 8 y 16.
         * - Con o sin letras mayúsculas.
         * - Con o sin números.
         * - Con o sin símbolos.
         * (Pudiendo combinar todos estos parámetros entre ellos)
         */
        Integer longitud = 9;
        boolean mayusc = true;
        boolean minusc = true;
        boolean num = true;
        boolean simb = true;
        String password[] = new String[16];

        List<Integer> pos = new ArrayList<>();
        List<String> config = new ArrayList<>();

        for (int i = 0; i < longitud; i++) {
            pos.add(i);
        }
        Collections.shuffle(pos);

        if (mayusc) {
            config.add("mayusc");
        }
        if(num) {
            config.add("num");
        }
        if(simb) {
            config.add("simb");
        }
        if(minusc) {
            config.add("minusc");
        }

        for (int i = 0; i < longitud; i++) {
            int random = randomInt(config.size() - 1);
            switch (config.get(random)){
                case "mayusc":
                    String l = Character.toString(randomLetter()).toUpperCase();
                    password[pos.get(i)] = l;
                    break;
                case "num":
                    String n = Integer.toString(randomInt(10));
                    password[pos.get(i)] = n;
                    break;
                case "simb":
                    String c = Character.toString(randomChar());
                    password[pos.get(i)] = c;
                    break;
                case "minusc":
                    String m = Character.toString(randomLetter());
                    password[pos.get(i)] = m;
                    break;
            }
        }

        for (int j=0; j < 9; j++){
            System.out.println(password[j]);
        }
    }

    private static char randomLetter() {
        String abc = "abcdefghijklmnoprstuvwxyz";
        return abc.charAt(randomInt(abc.length()));
    }
    private static int randomInt(int max) {
        Random r = new Random();
        return r.nextInt(max)+1;
    }

    private static char randomChar()  {
        String simb = "!@#$%^&*()_+=-?.<>``";
        return simb.charAt(randomInt(simb.length())-1);
    }
}