/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
use std::io;
use std::io::BufRead;
use std::slice::Chunks;

struct Jugador {
    puntos: i32,
}
struct Tenis {
    p1: Jugador,
    p2: Jugador,
    finalizado: bool,
}

impl Tenis {
    fn new() -> Self {
        Tenis {
            p1: Jugador { puntos: 0 },
            p2: Jugador { puntos: 0 },
            finalizado: false,
        }
    }
    fn punto(&mut self, ganador: String) {
        match ganador.as_str() {
            "P1" => self.p1.puntos+=1,
            "P2" => self.p2.puntos+=1,
            _ => println!("Error no valid player"),
        };
        if (self.p1.puntos > 3  || self.p2.puntos > 3) && (self.p1.puntos - self.p2.puntos).abs() > 1 {
            self.finalizado = true;
        }
    }
    
    fn punto_to_string(&self, puntos: i32) -> String {
        match puntos {
            0 => "Love".to_string(),
            1 => "15".to_string(),
            2 => "30".to_string(),
            3 => "40".to_string(),
            _ => "Error".to_string(),
        }
    }

    fn mostrar_puntuacion(&self) {

        if self.p1.puntos == 3  && self.p2.puntos == 3 {
            println!("Deuce");
        } else if self.p1.puntos > 3  || self.p2.puntos > 3 {
            let ventaja = self.p1.puntos-self.p2.puntos;
            match ventaja.abs() {
                0 => println!("Deuce"),
                1 => println!("Ventaja P{}", if ventaja > 0 {1} else {2}),
                _ => println!("Ha ganado P{}", if ventaja > 0 {1} else {2}),
            }
        } else {
            let p1_string = self.punto_to_string(self.p1.puntos);
            let p2_string= self.punto_to_string(self.p2.puntos);
            println!("{} - {}", p1_string, p2_string);
        }
    }

    fn fin_partido(&self) -> bool {
        self.finalizado
    }
}

fn get_puntos_ganados(line: Result<String, std::io::Error>) -> Result<Vec<String>, String> {
    // Validamos el contenido de la linea
    if !line.is_ok() {
        return Err("Error en la entrada de datos".to_string());
    }

    // Se obtiene el contenido de la linea
    let last_input : String = line.unwrap().to_uppercase();
    if last_input.is_empty() {
        return Ok(vec![]);
    }

    // Dividir last_input en tokens de dos caracteres y filtrar aquellos que no sean P1 o P2
    let vec_last_input : Vec<char> = last_input.chars().collect();
    let vec_chunks_last_input : Chunks<'_, char> = vec_last_input.chunks(2);
    let vec_tokens_last_input : Vec<String> = vec_chunks_last_input
        .map( |x| {
            let mut token : String = String::new();
            for c in x {
                token.push(*c);
            }
            token})
        .filter(|x| x == "P1" || x == "P2")
        .collect();

    return Ok(vec_tokens_last_input);
}

fn main() {
    
    // Se declara una varibla para iterar sobre la entrada estandar.
    let mut lines = io::stdin().lock().lines();

    // Inicializacion de la variable que contendra el juego de tenis
    let mut tenis = Tenis::new();

    // Mientras hay contenido para procesar, tratamos linea a linea.
    while let Some(line) = lines.next() {

        // Se transforma la linea en un vector de tokens
        let puntos_ganados = get_puntos_ganados(line);
        if puntos_ganados.is_err() {
            println!("{}", puntos_ganados.err().unwrap());
            break;
        }

        // Se procesa el vector de jugadas de tenis
        for token in puntos_ganados.unwrap() {
            // Contabilizamos el punto y mostramos la puntuacion
            tenis.punto(token);
            tenis.mostrar_puntuacion();
            // Si el partido ha finalizado, salimos del bucle
            if tenis.fin_partido() {
                return;
            }
        }
    };
}