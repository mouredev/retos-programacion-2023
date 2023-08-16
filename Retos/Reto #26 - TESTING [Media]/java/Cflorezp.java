package reto26test;

import org.testng.annotations.Test;

import java.time.DayOfWeek;
import java.time.LocalDate;

import static org.testng.AssertJUnit.assertFalse;
import static org.testng.AssertJUnit.assertTrue;

/*
 * Crea tres test sobre el reto 12: "Viernes 13".
 * - Puedes copiar una solución ya creada por otro usuario en
 *   el lenguaje que estés utilizando.
 * - Debes emplear un mecanismo de ejecución de test que posea
 *   el lenguaje de programación que hayas seleccionado.
 * - Los tres test deben de funcionar y comprobar
 *   diferentes situaciones (a tu elección).
 */
public class Cflorezp {

    @Test
    public void test1Viernes13() {
        assertFalse(hayViernes13(2022, 11));
    }

    @Test
    public void test2Viernes13() {
        assertFalse(hayViernes13(1983, 10));
    }

    @Test
    public void test3Viernes13() {
        assertTrue(hayViernes13(2000, 10));
    }

    public static boolean hayViernes13(int anio, int mes) {
        LocalDate actual = LocalDate.of(anio, mes, 13);
        DayOfWeek dia = actual.getDayOfWeek();
        String nombre = dia.name();
        return nombre.equals("FRIDAY") ? true : false;
    }


}
