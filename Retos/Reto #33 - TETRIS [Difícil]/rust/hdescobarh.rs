// author: hdescobarh (Hans D. Escobar H.)

use gestion_cli::input_movimiento;
use juego::Pantalla;

const CARACTER_ACTIVOS: char = '🔳';
const CARACTER_INACTIVOS: char = '🔲';
const FILAS_TABLERO: usize = 10;
const COLUMNAS_TABLERO: usize = 10;

fn main() {
    let mut pantalla = Pantalla::default();
    pantalla.imprimir_estado();
    loop {
        if let Some(tipo_movimiento) = input_movimiento() {
            pantalla.mover_tetromino(tipo_movimiento);
            pantalla.imprimir_estado();
        }
    }
}
mod juego {
    use crate::CARACTER_ACTIVOS;
    use crate::CARACTER_INACTIVOS;
    use crate::COLUMNAS_TABLERO;
    use crate::FILAS_TABLERO;

    #[derive(Copy, Clone)]
    struct Coordenada {
        fila: isize,
        columna: isize,
    }

    /**
     * Representa un tetrominó, una ficha de Tetris.
     * Corresponde a una región cuadrada de longitud 3 o 4 cuadrados.
     */
    struct Tetromino {
        // Esta es la coordenada en el tablero del cuadrado de la esquina inferior izquierda
        coordenada_referencia: Coordenada,
        // El origen de las coordenadas internas (0,0) es el cuadrado central
        activos: Vec<Coordenada>,
    }

    impl Tetromino {
        fn new(coordenada_real: Coordenada) -> Self {
            // para esta prueba, la figura es el Tetromino J (L invertida)
            let figura_activos = [[1, -1], [0, -1], [0, 0], [0, 1]];
            let activos = figura_activos
                .into_iter()
                .map(|[fila, columna]| Coordenada { fila, columna })
                .collect();
            Tetromino {
                coordenada_referencia: coordenada_real,
                activos,
            }
        }
        /**
         * Indica las coordenadas reales de los cuadrados activos del tetrominó
         */
        fn traducir_a_coordenadas_reales(&self) -> Vec<Coordenada> {
            self.activos
                .iter()
                .map(|coordenada| Coordenada {
                    fila: self.coordenada_referencia.fila - (1 + coordenada.fila),
                    columna: self.coordenada_referencia.columna + (1 + coordenada.columna),
                })
                .collect()
        }

        /**
         * Se encarga de llamar el movimiento correcto y generar el
         * tetrominó con la configuración y posición correspondientes.
         */
        fn realizar_movimiento(&self, tipo: Movimiento) -> Tetromino {
            let nuevos_activos: Vec<Coordenada>;
            let nueva_coordenada_referencia: Coordenada;

            match tipo {
                Movimiento::Rotacion => {
                    nuevos_activos = self.rotar();
                    nueva_coordenada_referencia = self.coordenada_referencia;
                }
                Movimiento::Derecha => {
                    nuevos_activos = self.activos.clone();
                    nueva_coordenada_referencia = self.desplazar(1, 0);
                }
                Movimiento::Izquierda => {
                    nuevos_activos = self.activos.clone();
                    nueva_coordenada_referencia = self.desplazar(-1, 0);
                }
                Movimiento::Abajo => {
                    nuevos_activos = self.activos.clone();
                    nueva_coordenada_referencia = self.desplazar(0, 1);
                }
            };

            Tetromino {
                coordenada_referencia: nueva_coordenada_referencia,
                activos: nuevos_activos,
            }
        }

        fn rotar(&self) -> Vec<Coordenada> {
            self.activos
                .iter()
                .map(|coor| Coordenada {
                    fila: coor.columna,
                    columna: -coor.fila,
                })
                .collect()
        }

        fn desplazar(
            &self,
            movimiento_horizontal: isize,
            movimiento_vertical: isize,
        ) -> Coordenada {
            let fila = self.coordenada_referencia.fila + movimiento_vertical;
            let columna = self.coordenada_referencia.columna + movimiento_horizontal;
            Coordenada { fila, columna }
        }
    }

    /**
     * Representa el espacio donde se puede mover las fichas. Se encarga de contener
     * el tetrominó activo, así como determinar si su configuración es legal
     */
    pub struct Pantalla {
        estado: [[char; COLUMNAS_TABLERO]; FILAS_TABLERO],
        tetromino_activo: Tetromino, // Empieza con un activo para la prueba de concepto
    }

    impl Pantalla {
        // Para este ejercicio, la pantalla inicia con una ficha en una posición fija
        pub fn default() -> Self {
            let estado = [[CARACTER_INACTIVOS; COLUMNAS_TABLERO]; FILAS_TABLERO];
            let tetromino_activo = Tetromino::new(Coordenada {
                fila: 2,
                columna: 0,
            });

            Pantalla {
                estado,
                tetromino_activo,
            }
        }

        // TODO Quizá mejor delegar esta tarea fuera de este struct
        pub fn imprimir_estado(&self) {
            let mut para_imprimir = self.estado;

            for coord in self.tetromino_activo.traducir_a_coordenadas_reales() {
                para_imprimir[coord.fila as usize][coord.columna as usize] = CARACTER_ACTIVOS;
            }

            for fila in para_imprimir {
                println!("\t{}", String::from_iter(fila.iter()));
            }

            println!("\n");
        }

        /**
         * Verifica si las nuevas coordenadas del tetrominó esta en los limites
         */
        fn validar_bordes(tetromino: &Tetromino) -> bool {
            for coor in tetromino.traducir_a_coordenadas_reales() {
                let fila_ilegal = coor.fila < 0 || coor.fila as usize >= FILAS_TABLERO;
                let columna_ilegal = coor.columna < 0 || coor.columna as usize >= COLUMNAS_TABLERO;
                if fila_ilegal || columna_ilegal {
                    return false;
                }
            }
            true
        }

        /**
         * Se encarga indicarle al tetrominó que se mueva, y de validar la legalidad del
         * nuevo estado.
         */
        pub fn mover_tetromino(&mut self, tipo: Movimiento) {
            // La ficha realiza el movimento, el tablero lo valida y sí es valido, actualiza la ficha activa
            let tetromino = self.tetromino_activo.realizar_movimiento(tipo);
            let bordes_validados = Pantalla::validar_bordes(&tetromino);
            if bordes_validados {
                self.tetromino_activo = tetromino;
            };
        }
    }

    /**
     * Tipos de movimientos validos
     */
    pub enum Movimiento {
        Rotacion,
        Derecha,
        Izquierda,
        Abajo,
    }
}

mod gestion_cli {
    use crate::juego::Movimiento;
    use std::io;

    /**
     * Se encarga de imprimir mensajes en consola y del parsing del input del usuario
     */
    pub fn input_movimiento() -> Option<Movimiento> {
        println!(
            "Ingrese el número de la acción:
        0 Rotar
        1 Derecha
        2 Izquierda
        3 Abajo
        10 Salir"
        );

        let mut input: String = String::new();

        io::stdin()
            .read_line(&mut input)
            .expect("Error al leer la entrada.\n");

        let instruccion = match input.trim().parse::<usize>() {
            Ok(numero) => numero,
            Err(_) => {
                println!("No es un número.\n");
                return None;
            }
        };

        match instruccion {
            0 => Some(Movimiento::Rotacion),
            1 => Some(Movimiento::Derecha),
            2 => Some(Movimiento::Izquierda),
            3 => Some(Movimiento::Abajo),
            10 => {
                println!("Cerrando el juego.\n");
                std::process::exit(0);
            }
            _ => {
                println!("Número no valido.\n");
                None
            }
        }
    }
}
