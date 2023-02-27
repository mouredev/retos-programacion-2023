package reto8GeneradorPseudoaleatorio;

import java.time.LocalDateTime;
import java.time.ZoneId;

/*
 * Generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 */
public class Cflorezp {

    public static void main(String[] args) {
        LocalDateTime ahora = LocalDateTime.now();
        long milisegundos = ahora.atZone(ZoneId.systemDefault()).toInstant().toEpochMilli();
        int milisegundosReducidos = (int) (milisegundos / 10 % 100);
        if (milisegundosReducidos >= 100) {
            milisegundosReducidos = 0;
        }
        System.out.println(milisegundosReducidos);
    }
}
