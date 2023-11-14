
/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

public class josepmonclus {
    public static void main(String[] args) {
        
        System.out.println(random());
        
    }

    private static long random() {
        return System.currentTimeMillis() % 100;
    }
}
