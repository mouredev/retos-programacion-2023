//! author: Hans D. Escobar H. (hdescobarh)
//! La Solución se compone de dos módulos:
//! * `game` - Implementa la lógica del juego.
//! * `rendering` - Encargado de la presentación en consola de los elementos del juego.

/* Cargo manifest:
[package]
name = "carrera_de_coches"
version = "0.1.0"
edition = "2021"
[dependencies]
rand = "0.8.5"
*/

use std::process::exit;
use std::thread;
use std::time::Duration;

/// Tiempo en ms entre ticks del juego
const TICK_TIME: u64 = 1000;
fn main() {
    let mut race = game::Race::default();
    loop {
        println!("{race}");
        thread::sleep(Duration::from_millis(TICK_TIME));
        match race.tick() {
            Some(_) => continue,
            None => {
                println!("{race}");
                println!("Game over. {}", race.winner().as_ref().unwrap());
                exit(0)
            }
        }
    }
}

/// Modulo encargado de la lógica interna del juego
pub mod game {

    // Biblioteca para la generación de valores aleatorios
    use rand::rngs::StdRng;
    use rand::{Rng, SeedableRng};

    /// Número de ticks el carro no puede moverse después de estrellarse.
    const CRASHED_TICKS: usize = 1;
    /// Tamaño mínimo permitido para el circuito
    const TRACK_MIN_LENGTH: usize = 10;
    /// Tamaño máximo permitido para el circuito
    const TRACK_MAX_LENGTH: usize = 30;

    /// Representa el estado del carro. El valor numérico, cuando esta presente,
    /// indica el tiempo que lleva en ese estado
    #[non_exhaustive]
    pub enum CarStatus {
        OK,
        Crashed(usize),
    }

    #[non_exhaustive]
    #[derive(PartialEq)]
    /// Representa eventos del juego relacionados con el vehículo.
    pub enum CarEvent {
        /// Efectivamente se mueve
        Advances,
        /// Se choca
        Crash,
        /// Ha cruzado la linea de meta
        FinishLine,
    }

    /// Representa los vehículos del juego
    pub struct Car {
        /// Identificador único del vehículo
        id: usize,
        /// Posición actual sobre la pista
        position: usize,
        /// Estado del carro. Condiciona las acciones que puede llevar a cabo.
        status: CarStatus,
    }

    impl Car {
        /// Crea un nuevo vehículo con la id especificada
        fn new(id: usize) -> Self {
            Self {
                id,
                position: 0,
                status: CarStatus::OK,
            }
        }
        /// Indica el número de posiciones de movimiento hacia la meta
        fn try_to_advance(&mut self) -> usize {
            // el carro valida sí puede moverse en este turno
            self.update_status();
            match self.status {
                CarStatus::OK => StdRng::from_entropy().gen_range(1..=3),
                CarStatus::Crashed(_) => 0,
            }
        }
        /// Actualiza estados dependientes del tiempo. Pensado para ser usado únicamente por el mismo objeto.
        fn update_status(&mut self) {
            if let CarStatus::Crashed(t) = self.status {
                if t >= CRASHED_TICKS {
                    self.status = CarStatus::OK
                } else {
                    self.status = CarStatus::Crashed(t + 1)
                }
            }
        }
    }

    /// Representación de un arbol
    pub struct Tree {
        /// Posición actual sobre la pista
        position: usize,
    }

    /// Representación de las pistas del juego.
    pub struct Track {
        /// Longitud de la pista. Invariable.
        length: usize,
        /// Vehículo ocupando esa pista.
        car: Car,
        /// Árboles sobre la pista. Invariables.
        trees: Vec<Tree>,
    }

    impl Track {
        /// Crea una nueva pista de tamaño y con un vehículo ocupándola.
        fn new(car: Car, length: usize) -> Self {
            // escoge aleatoriamente el número de árboles y sus posiciones
            // Los arboles NO pueden estar ni la meta ni el punto de salida.
            let tree_number: u8 = StdRng::from_entropy().gen_range(1..=3);
            let mut trees: Vec<Tree> = Vec::with_capacity(tree_number as usize);
            for _id in 0..tree_number {
                let position: usize = StdRng::from_entropy().gen_range(1..length);
                trees.push(Tree { position })
            }

            Self { length, trees, car }
        }

        /// Corre la lógica correspondiente para cada turno
        fn tick(&mut self) -> CarEvent {
            let next_car_position = self.car.try_to_advance() + self.car.position;
            // Verifica el carro no haya pasado la meta
            if next_car_position >= self.length {
                self.car.position = self.length;
                return CarEvent::FinishLine;
            }
            // Como no ha cruzado la meta, actualiza su estado y evalúa las consecuencias
            self.car.position = next_car_position;

            if self.car_collision() {
                match self.car.status {
                    CarStatus::OK => self.car.status = CarStatus::Crashed(0),
                    CarStatus::Crashed(_) => (),
                }
                return CarEvent::Crash;
            }
            // No ha pasado la linea de meta ni chocado
            CarEvent::Advances
        }

        fn car_collision(&self) -> bool {
            self.trees
                .iter()
                .any(|tree| tree.position == self.car.position)
        }

        /// Lectura de las posiciones que ocupan los arboles
        pub fn get_tree_positions(&self) -> Vec<&usize> {
            self.trees.iter().map(|tree| &tree.position).collect()
        }

        /// Lectura de la longitud de la pista
        pub fn get_length(&self) -> &usize {
            &self.length
        }

        /// Lectura de la información del vehículo.
        /// Retorna ( ID_del_carro, posición_actual_en_pista, estado_de_carro)
        pub fn get_car_info(&self) -> (&usize, &usize, &CarStatus) {
            (&self.car.id, &self.car.position, &self.car.status)
        }
    }

    /// Representación del ganador o ganadores de la carrera
    pub enum Winner {
        A,
        B,
        Both,
    }

    /// Contiene todos los elementos del juego y estados del juego.
    pub struct Race {
        track_a: Track,
        track_b: Track,
        winner: Option<Winner>,
    }

    impl Default for Race {
        fn default() -> Self {
            //randomly chooses track length
            let length: usize =
                StdRng::from_entropy().gen_range(TRACK_MIN_LENGTH..=TRACK_MAX_LENGTH);
            Self {
                track_a: Track::new(Car::new(1), length),
                track_b: Track::new(Car::new(2), length),
                winner: None,
            }
        }
    }

    impl Race {
        /// realiza la lógica de cada paso de tiempo. Sí hay un ganador, retorna None,
        /// de lo contrario, retorna que eventos ocurrieron
        pub fn tick(&mut self) -> Option<(CarEvent, CarEvent)> {
            // No realiza nada sí ya hay ganador
            if self.winner.is_some() {
                return None;
            }
            // Ejecuta el paso del tiempo
            let event_track_a = self.track_a.tick();
            let event_track_b = self.track_b.tick();

            // Evalúa consecuencias
            let a_wins = event_track_a == CarEvent::FinishLine;
            let b_wins = event_track_b == CarEvent::FinishLine;

            if !a_wins && !b_wins {
                return Some((event_track_a, event_track_b));
            }

            if a_wins && b_wins {
                self.winner = Some(Winner::Both);
            } else if a_wins {
                self.winner = Some(Winner::A)
            } else {
                self.winner = Some(Winner::B)
            }

            None
        }

        /// Lectura de la pista A dela carrera
        pub fn get_track_a(&self) -> &Track {
            &self.track_a
        }

        /// Lectura de la pista B dela carrera
        pub fn get_track_b(&self) -> &Track {
            &self.track_b
        }

        /// Lectura del ganador del juego. None sí aun no existe, Some(ganador) sí existe.
        pub fn winner(&self) -> &Option<Winner> {
            &self.winner
        }
    }
}

/// Modulo encargado de formatear el texto a presentar en consola.
pub mod rendering {

    use std::fmt::Display;

    use crate::game::*;

    const C_FLAG: &str = "🏁";
    const C_CAR_A: &str = "🚙";
    const C_CAR_B: &str = "🚗";
    const C_CAR_AB: &str = "🚙🚗";
    const C_CRASH: &str = "💥";
    const C_TREE: &str = "🌲";
    // Reemplacé el underscore por Full width Low Line (U+FF3F)
    // Así visualmente las pistas no parecen de diferente longitud cuando tienen diferente numero de arboles.
    const C_TRACK: &str = "＿"; //"_";

    impl Display for Track {
        fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
            let mut line = vec![C_TRACK; *self.get_length() + 1];
            for tree_loc in self.get_tree_positions() {
                line[*tree_loc] = C_TREE;
            }
            if let Some(last) = line.last_mut() {
                *last = C_FLAG;
            }

            let (car_id, car_loc, car_status) = self.get_car_info();

            let car_char = match car_status {
                CarStatus::OK => car_id_to_char(car_id),
                CarStatus::Crashed(_) => C_CRASH,
            };
            line[*car_loc] = car_char;
            line.reverse();
            write!(f, "{}", line.join(""))
        }
    }

    impl Display for Race {
        fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
            writeln!(
                f,
                "{a}\n{b}",
                a = self.get_track_a(),
                b = self.get_track_b()
            )
        }
    }

    fn car_id_to_char(car_id: &usize) -> &'static str {
        if *car_id == 1 {
            C_CAR_A
        } else if *car_id == 2 {
            C_CAR_B
        } else {
            C_CAR_AB
        }
    }

    impl Display for Winner {
        fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
            let s = match self {
                Winner::A => car_id_to_char(&1),
                Winner::B => car_id_to_char(&2),
                Winner::Both => car_id_to_char(&0),
            };
            write!(f, "🥇 {s}")
        }
    }
}
