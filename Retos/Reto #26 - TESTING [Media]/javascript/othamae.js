/*
 * Crea tres test sobre el reto 12: "Viernes 13".
 * - Puedes copiar una solución ya creada por otro usuario en
 *   el lenguaje que estés utilizando.
 * - Debes emplear un mecanismo de ejecución de test que posea
 *   el lenguaje de programación que hayas seleccionado.
 * - Los tres test deben de funcionar y comprobar
 *   diferentes situaciones (a tu elección).
 */

const assert = require('assert')

// Function to test
const isFriday13th = (month, year) => {
    const date = new Date(year, month - 1, 13)
    return date.getDay() === 5
}

// Examples
console.log(isFriday13th(8, 2021)) // true
console.log(isFriday13th(10, 2021)) // false
console.log(isFriday13th(5, 2022)) // true
console.log(isFriday13th(1, 2023)) // true
console.log(isFriday13th(6, 2022)) // false
console.log(isFriday13th(10, 2023)) // true

// Test 1: Check a month with Fridat 13th
assert.strictEqual(isFriday13th(8, 2021), true)

// Test 2: Check a month that doesnt have Friday 13th
assert.strictEqual(isFriday13th(10, 2021), false)

// Test 3: Ckeck that the response is not null
const result = isFriday13th(1, 2023)
assert.ok(result !== null)
assert.notStrictEqual(result, null)
assert.notStrictEqual(result, undefined)

console.log("Tests passed")