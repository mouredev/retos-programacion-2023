/*

════╗
╔══╗║
║╔╗║║
║╚═╝║
╚═══╝

Reto #22 - Espiral
Santos Alarcón Asensio
https://github.com/SantosAlarcon

*/

/**
 * Dibuja una espiral por pantalla dependiendo de la altura y la anchura.
 * @param size: El tamaño que tendrá la espiral, tanto de alto como de ancho.
 **/
const dibujarEspiral = (size) => {
    let espiral = "";

    if (size >= 5) {

        for (let fila = 1; fila <= size; fila++) {
            for (let columna = 1; columna <= size; columna++) {

                /* PRIMERA FILA */
                if (fila === 1) {
                    if (columna < size) {
                        espiral += "═";
                    } else if (columna === size) {
                        espiral += "╗\n";
                    }
                }

                /* SEGUNDA FILA */
                if (fila === 2) {
                    if (columna === 1) {
                        espiral += "╔";
                    } else if (columna < size - 1) {
                        espiral += "═";
                    } else if (columna === size - 1) {
                        espiral += "╗║";
                    }
                }

                /* TERCERA FILA */
                if (fila === 3) {
                    if (columna == 2) {
                        espiral += "╔";
                    } else if (columna > 2 && columna < size - 2) {
                        espiral += "═";
                    } else if (columna === size - 2) {
                        espiral += "╗║";
                    }
                }

                /* Se imprimen las tuberías de inicio y final de las filas intermedias. */
                if ((fila > 2 && fila < size) && columna === 1) {
                    espiral += "\n║";
                } else if ((fila > 2 && fila < size) && columna === size) {
                    espiral += "║";
                }

                /* Se dibujará la antepenúltima fila en caso de que el tamaño sea
                 * superior a 5. 
                 */

                if (size > 5) {
                    /* Filas intermedidas */
                    if (fila > 3 && fila < size - 2) {
                        if (columna === 2) {
                            espiral += "║";
                        } else if (columna === size - 2) {
                            espiral += "║║";
                        } else if (columna > 2 && columna < size - 2) {
                            espiral += " ";
                        }
                    }


                    /* ANTEPENÚLTIMA FILA */
                    if (fila === size - 2) {
                        if (columna === 2) {
                            espiral += "║ ";
                        }

                        if (size > 6 && (columna > 2 && columna < size - 3)) {
                            espiral += "═";
                        }

                        if (columna === size - 2) {
                            espiral += "╝║";
                        }
                    }

                }

                /* PENÚLTIMA FILA */
                if (fila === size - 1) {
                    if (columna === 2) {
                        espiral += "╚";
                    } else if (columna > 2 && columna <= size - 2) {
                        espiral += "═";
                    } else if (columna === size - 1) {
                        espiral += "╝";
                    }
                }

                /* ÚLTIMA FILA */
                /* Se imprime el cierre inferior izquierda en la última fila. */
                if (fila === size) {
                    if (columna === 1) {
                        espiral += "\n╚";
                    } else if (columna < size && columna > 1) {
                        espiral += "═";
                    } else if (columna === size) {
                        espiral += "╝";
                    }
                }
            }
        }
    } else {
        espiral = "Solo se puede dibujar una espiral a partir de 5x5."
    }

    return espiral;

}
console.log(dibujarEspiral(7));
