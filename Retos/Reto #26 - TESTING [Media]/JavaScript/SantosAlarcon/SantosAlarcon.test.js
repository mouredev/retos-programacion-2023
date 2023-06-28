import { describe, test } from "node:test"
import assert from "node:assert"
import { friday13 } from "./mouredev.js"

describe("Probando la función Viernes 13", () => {
  test("Devuelve false si se le pasa el año en negativo", () => {
    const v13 = friday13(-2023, 15);
    assert.strictEqual(v13, false);
  })

  test("Devuelve false si se le pasa el día en negativo", () => {
    const v13 = friday13(2023, -4);
    assert.strictEqual(v13, false);
  })

  test("Devuelve false si se pone a 0 el día", () => {
    const v13 = friday13(2023, 0);
    assert.strictEqual(v13, false);
  })

  test("Devuelve false si se le pasa el día como una cadena", () => {
    const v13 = friday13(2023, "2");
    assert.strictEqual(v13, false);
  })

  test("Devuelve false si se le pasa el año como una cadena", () => {
    const v13 = friday13("2023", 5);
    assert.strictEqual(v13, false);
  })

  test("Devuelve true si se le pasa el mes donde el viernes es día 13", () => {
    const v13 = friday13(2023, 10);
    assert.strictEqual(v13, true);
  })

  test("Devuelve false si se introducen el mes y el año como cadenas", () => {
    const v13 = friday13("Santos", "Alarcón");
    assert.strictEqual(v13, false);
  })
})
