function retoFizzBuzz() {
  // Inicializamos la cadena que vamos a imprimir
  let resul = "";
  // Recorremos los números del 1 al 100
  for (let num: number = 1; num <= 100; num++) {
    // Si el número es múltiplo de 3, añadimos "fizz" a la cadena
    if (num % 3 == 0) {
      resul += "fizz";
    }
    // Si el número es múltiplo de 5, añadimos "buzz" a la cadena
    if (num % 5 == 0) {
      resul += "buzz";
    }
    // Si no es múltiplo de ninguno de ellos, añadimos el número a la cadena
    if (resul === "") {
      resul += num;
    }
  }
  // Imprimimos la cadena y un salto de línea
  console.log(resul);
}

