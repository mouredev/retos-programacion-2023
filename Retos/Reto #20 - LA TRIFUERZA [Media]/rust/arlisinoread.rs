use std::string::ToString;

fn main() {
    let valor_n = 10;

    let trifuerza = Trifuerza::new(valor_n);
    println!("{}", trifuerza.to_string());
}

struct Trifuerza {
    matriz_triangulo: Vec<Vec<char>>,
}

impl Trifuerza {
    pub fn new(n: i32) -> Self {
        let ancho_matriz = n * 4 - 1;
        let alto_matriz = n * 2;

        let mut matriz_triangulo: Vec<Vec<char>> =
            vec![vec![' '; ancho_matriz as usize]; alto_matriz as usize];

        //Primer Triángulo:
        Trifuerza::dibuja_triangulo(n, n, 0, &mut matriz_triangulo);
        //Segundo Tríangulo inferior izquierdo:
        Trifuerza::dibuja_triangulo(n, 0, n, &mut matriz_triangulo);
        //Tercer Tríangulo inferior derecho:
        Trifuerza::dibuja_triangulo(n, 2 * n, n, &mut matriz_triangulo);

        Self { matriz_triangulo }
    }

    fn dibuja_triangulo(n: i32, desplazo_x: i32, desplazo_y: i32, matriz: &mut Vec<Vec<char>>) {
        //Cada triángulo calcula el 2n-1.
        let fila_mayor = 2 * n - 1;

        for y in desplazo_y..(n + desplazo_y) {
            let fila = matriz
                .get_mut(y as usize)
                .expect(format!("Y fuera de límites: {}", y).as_str());

            if y == n + desplazo_y - 1 {
                for x in desplazo_x..(fila_mayor + desplazo_x) {
                    let casilla = fila
                        .get_mut(x as usize)
                        .expect(format!("X fuera de límites: {}", x).as_str());

                    *casilla = '*';
                }
            }

            let val_x_casilla_izq = fila_mayor / 2 - (y - desplazo_y);

            let casilla_izq = fila
                .get_mut((desplazo_x + val_x_casilla_izq) as usize)
                .expect(format!("X fuera de límites: {}", val_x_casilla_izq).as_str());

            *casilla_izq = '*';

            let val_x_casilla_der = y - desplazo_y + fila_mayor / 2;

            let casilla_der = fila
                .get_mut((desplazo_x + val_x_casilla_der) as usize)
                .expect(format!("X fuera de límites: {}", val_x_casilla_der).as_str());

            *casilla_der = '*';
        }
    }
}

impl ToString for Trifuerza {
    fn to_string(&self) -> String {
        let mut ret = String::from("");

        for fila in &self.matriz_triangulo {
            for c in fila {
                ret.push(*c);
            }
            ret.push('\n');
        }
        ret
    }
}
