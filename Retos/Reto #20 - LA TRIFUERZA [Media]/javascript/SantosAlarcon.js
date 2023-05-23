const dibujarTrifuerza = (n) => {
    let espacio;
    let espacio_mitad;
    let asterisco_fila;
    let fila_actual;

    // Se controla que el número de filas sea un entero positivo.
    if (n > 0 && typeof n === "number") {

        // Se dibujará un triángulo con el doble de las filas que se han introducido.
        for (let fila = 0; fila < n * 2; fila++) {

            // La mitad superior dibujará un triángulo de X filas con espacios a los
            // lados.
            if (fila < n) {
                espacio = " ".repeat(((2 * n) - 1) - fila)
                asterisco_fila = "*".repeat((2 * (fila + 1)) - 1);
                console.log(espacio + asterisco_fila + espacio);
            }
            // La mitad inferior dibujarán los espacios de los lados y el espacio del
            // medio.
            else {
                fila_actual = fila - n;
                espacio = " ".repeat((n - fila_actual) - 1);
                espacio_mitad = " ".repeat((2 * (n - fila_actual)) - 1)
                asterisco_fila = "*".repeat((2 * (fila_actual + 1)) - 1);
                console.log(espacio + asterisco_fila + espacio_mitad + asterisco_fila);
            }
        }
        // Se muestra un mensaje de error si se introduce una cadena de texto o un
        // número negativo.
    } else {
        console.error("¡ERROR! Sólo puedes introducir números positivos para dibujar la Trifuerza.");
    }
}

dibujarTrifuerza(10);
