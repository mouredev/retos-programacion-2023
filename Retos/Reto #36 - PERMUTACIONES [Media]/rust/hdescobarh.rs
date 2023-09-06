// author: hdescobarh (Hans D. Escobar H.)

// Este modulo tiene mi solución
use crate::permutacion_naive::RamaArbol;

fn main() {
    /*
    Implementación naive O(n!):
        -   case_sensitive
        -   acepta cualquier caracter Unicode (e.g., el texto '漢字한국어' es valido).

    Reordenar la secuencia es equivalente a,
    dada una secuencia de tamaño n, generar un arbol de n! hojas,
    con (n-k) ramificaciones desde cada nodo en cada nivel, siendo la raíz del arbol el nivel 0
    */
    loop {
        let texto = match entrada_de_texto() {
            Some(string) => string,
            None => continue,
        };

        // Inicializa el nivel 0
        let tree_root = RamaArbol::desde_string(texto);

        // caché para la memoización. Se inicia con capacidad n! para reducir el allocation
        let mut cache: Vec<RamaArbol> = Vec::with_capacity(factorizar(tree_root.restantes.len()));

        // El método para generar todas las hojas del arbol es recursivo
        RamaArbol::generar_hojas(&mut cache, vec![tree_root]);

        // Finalmente, extrae las secuencias de la caché para imprimirlas
        let para_imprimir: Vec<String> = cache
            .into_iter()
            .map(|rama| rama.camino_sequencia)
            .collect();

        println!("{:?}", para_imprimir);
    }
}

mod permutacion_naive {

    /**
     * Cada nodo tiene una secuencia de caracteres hasta ese nodo y los nodos que faltan por usar.
     * Por ejemplo, para el texto "abcd" la raíz comienza con un camino de 4 espacios vacio y un restantes de 4;
     * Uno de los nodos del siguiente nivel tendra una string con un valor y 3 vacios, y un vector
     * de restantes de tamaño 3. Por ejemplo "a" y ['b', 'c', 'd']
     */
    #[derive(Clone)]
    pub struct RamaArbol {
        pub camino_sequencia: String,
        pub restantes: Vec<char>,
    }

    impl RamaArbol {
        pub fn desde_string(s: String) -> Self {
            RamaArbol {
                camino_sequencia: String::with_capacity(s.len()),
                restantes: s.chars().collect(),
            }
        }

        /**
         * Genera todas las posibles ramas a partir de una rama
         */
        fn ramificar(ramas: RamaArbol) -> Vec<RamaArbol> {
            if ramas.restantes.is_empty() {
                panic!("No puede generar mas ramas!");
            }
            let mut nuevas_ramas: Vec<RamaArbol> = Vec::with_capacity(ramas.restantes.len());
            for indice in 0..ramas.restantes.len() {
                /*Hace una deep copy de la Rama, remueve un caracter en el indice de los restantes
                y lo agrega al final de la secuencia */
                let mut rama: RamaArbol = ramas.clone();
                rama.camino_sequencia
                    .push(rama.restantes.swap_remove(indice));
                nuevas_ramas.push(rama);
            }
            nuevas_ramas
        }

        pub fn generar_hojas(resultado: &mut Vec<RamaArbol>, base: Vec<RamaArbol>) {
            for rama in base {
                if rama.restantes.is_empty() {
                    resultado.push(rama);
                } else {
                    let nueva_base = RamaArbol::ramificar(rama);
                    RamaArbol::generar_hojas(resultado, nueva_base);
                };
            }
        }
    }
}

fn factorizar(numero: usize) -> usize {
    let mut resultado = 1;
    for valores in 1..(numero + 1) {
        resultado *= valores;
    }
    resultado
}

use std::io;

/**
 * Se encarga de imprimir mensajes en consola y del parsing del input del usuario
 */
pub fn entrada_de_texto() -> Option<String> {
    println!("Ingrese el texto a permutar (o '0' para salir):\n");

    let mut input: String = String::new();
    // Validar la entrada
    io::stdin()
        .read_line(&mut input)
        .expect("Error al leer la entrada.\n");

    // Detectar si hay código de salida
    if let Ok(numero) = input.trim().parse::<usize>() {
        if numero == 0 {
            println!("Saliendo...\n");
            std::process::exit(0);
        }
    };

    if input.chars().count() > 11 {
        println!("La longitud es muy grande la el algoritmo implementado.\n");
        None
    } else {
        Some(input.trim().to_string())
    }
}

// Unit Tests
#[cfg(test)]
mod tests {
    use crate::factorizar;
    use crate::permutacion_naive::RamaArbol;

    #[test]
    fn texto_vacio() {
        let texto = String::from("");
        let tree_root = RamaArbol::desde_string(texto);
        let mut cache: Vec<RamaArbol> = Vec::with_capacity(factorizar(tree_root.restantes.len()));
        RamaArbol::generar_hojas(&mut cache, vec![tree_root]);
        assert_eq!("".to_string(), cache[0].camino_sequencia);
    }

    #[test]
    fn texto_2() {
        let texto = String::from("ab");
        let tree_root = RamaArbol::desde_string(texto);
        let mut cache: Vec<RamaArbol> = Vec::with_capacity(factorizar(tree_root.restantes.len()));
        RamaArbol::generar_hojas(&mut cache, vec![tree_root]);
        let mut resultado: Vec<String> = cache
            .into_iter()
            .map(|rama| rama.camino_sequencia)
            .collect();
        resultado.sort();
        let esperado = ["ab", "ba"];
        for index in 0..1 {
            assert_eq!(esperado[index], resultado[index])
        }
    }

    #[test]
    fn texto_4() {
        let texto = String::from("hLOa");
        let tree_root = RamaArbol::desde_string(texto);
        let mut cache: Vec<RamaArbol> = Vec::with_capacity(factorizar(tree_root.restantes.len()));
        RamaArbol::generar_hojas(&mut cache, vec![tree_root]);
        let mut resultado: Vec<String> = cache
            .into_iter()
            .map(|rama| rama.camino_sequencia)
            .collect();
        resultado.sort();
        let mut esperado = [
            "hOLa", "OhLa", "LhOa", "hLOa", "OLha", "LOha", "LOah", "OLah", "aLOh", "LaOh", "OaLh",
            "aOLh", "ahLO", "haLO", "LahO", "aLhO", "hLaO", "LhaO", "OhaL", "hOaL", "aOhL", "OahL",
            "haOL", "ahOL",
        ];
        esperado.sort();
        for index in 0..24 {
            assert_eq!(esperado[index], resultado[index])
        }
    }
}
