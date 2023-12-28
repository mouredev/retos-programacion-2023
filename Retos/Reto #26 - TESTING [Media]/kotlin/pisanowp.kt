/*
* Reto #26 26/06/2023
*
* Crea tres test sobre el reto 12: "Viernes 13".
* - Puedes copiar una solución ya creada por otro usuario en
*   el lenguaje que estés utilizando.
* - Debes emplear un mecanismo de ejecución de test que posea
*   el lenguaje de programación que hayas seleccionado.
* - Los tres test deben de funcionar y comprobar
*   diferentes situaciones (a tu elección).
*
*/


import org.junit.jupiter.api.Test
import org.junit.jupiter.api.Assertions.*

internal class Reto26_viernes_13KtTest {

    @Test
    fun hasViernes13() {
        /*  Relación de Viernes de 13 desde 2022 a 2025
        MAY de 2022 tiene un VIERNES 13
        JANUARY de 2023 tiene un VIERNES 13
        OCTOBER de 2023 tiene un VIERNES 13
        SEPTEMBER de 2024 tiene un VIERNES 13
        DECEMBER de 2024 tiene un VIERNES 13
        JUNE de 2025 tiene un VIERNES 13 */

        val viernes13 = listOf( Pair(5, 2022), Pair(1, 2023), Pair(10, 2023), Pair(9, 2024), Pair(12, 2024), Pair(6, 2025))

        viernes13.forEach() {
            assertEquals(true, hasViernes13(it.first, it.second) )

        }

    }

    @Test
    fun hasNotViernes13(){
        /* Fechas que NO son viernes 13 */
        val viernes13 = listOf( Pair(1, 2022), Pair(2, 2023), Pair(11, 2023), Pair(6, 2024))

        viernes13.forEach() {
            assertNotEquals(true, hasViernes13(it.first, it.second) )

        }
    }
}