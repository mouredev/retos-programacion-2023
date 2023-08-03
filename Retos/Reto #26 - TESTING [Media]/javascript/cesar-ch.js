/*
 * Crea tres test sobre el reto 12: "Viernes 13".
 * - Puedes copiar una solución ya creada por otro usuario en
 *   el lenguaje que estés utilizando.
 * - Debes emplear un mecanismo de ejecución de test que posea
 *   el lenguaje de programación que hayas seleccionado.
 * - Los tres test deben de funcionar y comprobar
 *   diferentes situaciones (a tu elección).
 */

import { describe, expect, it, } from "vitest";

function itsFridayThirteenth(month, year) {
    return new Date(`${month} 13, ${year}`).getDay() === 5
}



describe('itsFridayThirteenth', () => {
    it('should return true for friday the 13th', () => {
        expect(itsFridayThirteenth('January', 2023)).toBe(true)
    })

    it('should return false for friday the 13th', () => {
        expect(itsFridayThirteenth('May', 2022)).toBe(true)
    })

    it('should return false for friday the 13th', () => {
        expect(itsFridayThirteenth('July', 2023)).toBe(false)
    })
})