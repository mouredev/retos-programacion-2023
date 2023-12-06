/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
 */

// n es el número de filas de los triángulos. 
// 2n-1 es el número de columnas de los triángulos.
// La altura de la trifuerza es 2 veces el número de filas
// La anchura de la trifuerza es 2*anchora de los triángulos + 1

// Se importa la librería io para leer de teclado
use std::io;

// Se importa la librería bit-matrix
use bit_matrix::matrix::BitMatrix;

fn main() {

    // Variable entera para el número de filas
    let n : usize;

    // Solicitar el número de filas
    println!("Introduce el número de filas de los triángulos: ");

    // Leer el número de filas
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Error al leer el número de filas");
    n = input.trim().parse().expect("Error al convertir el número de filas");

    let alto_matriz : usize = 2*n;
    let ancho_matriz : usize = 2*(2*n-1)+1;  

    // Crear la matriz de la trifuerza   
    let mut trifuerza = BitMatrix::new(alto_matriz, ancho_matriz);

    // Poner a 0 todos los bits de la matriz
    trifuerza.set_all(false);

    // Generar los triangulos
    generar_triangulo(&mut trifuerza, n, 0, ((2*n-1)/2)+1);
    generar_triangulo(&mut trifuerza, n, n, 0);
    generar_triangulo(&mut trifuerza, n, n, 2*n);

    // Mostrar la trifuerza
    mostrar_trifuerza(trifuerza, alto_matriz, ancho_matriz);
}

// Funcion para generar un triangulo de altura n en la posicion (x,y) de la matriz
fn generar_triangulo(matriz : &mut BitMatrix, n : usize, fil : usize, col : usize) {

    // Calcular la fila mayor del triangulo
    let col_mayor = 2*n-1;

    // Primera fila del triangulo
    matriz.set(fil, col+n-1, true);

    // Borde izquierdo y derecho del triangulo
    for fila in 1..n-1 {
        matriz.set(fil+fila, col+n-1-fila, true);
        matriz.set(fil+fila, col+n-1+fila, true);
    }

    // Ultima fila del triangulo
    for columna in 0..col_mayor {
        matriz.set(fil+n-1, col+columna, true);
    }
}

fn mostrar_trifuerza(matriz : BitMatrix, alto_matriz : usize, ancho_matriz : usize) {

    // Mostrar la matriz por linea de comandos
    for fila in 0..alto_matriz {
        for columna in 0..ancho_matriz {
            if matriz[fila][columna] {
                print!("*");
            } else {
                print!(" ");
            }
        }
        println!("");
    }
}

