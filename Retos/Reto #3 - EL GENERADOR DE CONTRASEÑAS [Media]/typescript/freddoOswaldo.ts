/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */


class PasswordBuilder {
  private readonly CHARACTERS = {
    letters: "abcdefghijklmnopqrstuvwxyz",
    numbers: "0123456789",
    symbols: "!@#$%^&*()_+~`|}{[]:;?><,./-=",
  };

  private validateLength(length: number) {
    return length >= 8 && length <= 16;
  }

  private generateWithLowerCase() {
    return this.CHARACTERS.letters.charAt(
      Math.floor(Math.random() * this.CHARACTERS.letters.length)
    );
  }

  private generateWithUpperCase() {
    return this.CHARACTERS.letters
      .toUpperCase()
      .charAt(Math.floor(Math.random() * this.CHARACTERS.letters.length));
  }

  private generateWithNumbers() {
    return this.CHARACTERS.numbers.charAt(
      Math.floor(Math.random() * this.CHARACTERS.numbers.length)
    );
  }

  private generateWithSymbols() {
    return this.CHARACTERS.symbols.charAt(
      Math.floor(Math.random() * this.CHARACTERS.symbols.length)
    );
  }

  private validateOptions(
    withUpperCase = true,
    withWithNumbers = true,
    withSymbols = true
  ) {
    let option = Math.floor(Math.random() * 4);

    if (!withUpperCase && option === 1)
      option = this.validateOptions(withUpperCase, withWithNumbers, withSymbols);
    if (!withWithNumbers && option === 2)
      option = this.validateOptions(withUpperCase, withWithNumbers, withSymbols);
    if (!withSymbols && option === 3)
      option = this.validateOptions(withUpperCase, withWithNumbers,withSymbols);

    return option;
  }

  build({
    length = 16,
    withUpperCase = true,
    withWithNumbers = true,
    withSymbols = true,
  } = {}) {
    if (!this.validateLength(length)) {
      throw new Error("Invalid length");
    }

    const password = Array.from({ length })
      .map(() => {
        const option = this.validateOptions(
          withUpperCase,
          withWithNumbers,
          withSymbols
        );        

        switch (option) {
          case 0:
            return this.generateWithLowerCase();
          case 1:
            return this.generateWithUpperCase();
          case 2:
            return this.generateWithNumbers();
          case 3:
            return this.generateWithSymbols();
          default:
            return this.generateWithLowerCase();
        }
      })
      .join("");
    console.log(password);
  }
}

new PasswordBuilder().build();
