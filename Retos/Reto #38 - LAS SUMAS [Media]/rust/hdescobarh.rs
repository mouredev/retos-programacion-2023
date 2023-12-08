// author: Hans D. Escobar H. (hdescobarh)
#![crate_name = "combinacion_sumas"]
#![crate_type = "cdylib"]

/* 
Rust no cuenta con funciones para generar combinaciones en su biblioteca estándar (https://doc.rust-lang.org/std/).
Esta solución no usa bibliotecas externas.
*/

//! Dada una secuencia de valores enteros no negativos, encuentra todas las combinaciones
//! posibles que satisfacen la condición de que la suma de sus valores es igual a un valor objetivo
//!
//! Implementa un algoritmo sencillo que realiza una búsqueda en arbol, empezando por las
//! combinaciones (nCr), r=0. Desde cada combinación se ramifica a todas las combinaciones (nCk+r), r+1<=n
//! que no hayan sido generadas en otras ramas.
//!
//! # Ejemplo:
//!
//! ```
//! use combinacion_sumas::Combinacion;
//! let resultado = Combinacion::desde_secuencia(&[1, 5, 3, 2], &6);
//! // Retorna [[1, 2, 3], [1, 5]]
//! println!("{:?}", resultado);
//! ```

/// Almacena una posible combinación de una secuencia
#[derive(Clone)]
pub struct Combinacion {
    /// Contiene los valores que hacen parte de la combinación.
    valores: Vec<usize>,
    /// Contiene los valores de la secuencia original que aun no han sido incluidos
    pendientes: Vec<usize>,
    /// suma de los valores de la combinación. Se emplea para evitar iterar sobre todos valores
    /// cada que se agrega un nuevo elemento.
    suma: usize,
}

impl Combinacion {
    /// Desde una secuencia genera todas las posibles combinaciones que satisfacen
    /// que su suma es igual al valor objetivo.
    ///
    /// # Argumentos:
    /// * `secuencia` - Una secuencia de valores desde la cual generar las combinaciones
    /// * `objetivo` - El valor que deben satisfacer la suma de los valores de una combinación valida
    pub fn desde_secuencia(secuencia: &[usize], objetivo: &usize) -> Vec<Vec<usize>> {
        // genera la raíz del arbol de búsqueda
        let nodo_inicial = Self {
            valores: Vec::new(),
            pendientes: secuencia.to_vec(),
            suma: 0,
        };
        // La función asociada "generar_combinaciones" de forma recursiva genera combinaciones que cumplen la condición
        let mut buffer: Vec<Combinacion> = Vec::new();
        Combinacion::generar_combinaciones(&mut buffer, vec![nodo_inicial], objetivo);
        // Extrae los valores de cada combinación
        buffer
            .into_iter()
            .map(|combinacion| combinacion.valores)
            .collect::<Vec<Vec<usize>>>()
    }

    /// Privada.
    /// Genera todas las posibles combinaciones desde una secuencia de combinaciones de referencia.
    ///
    /// # Argumentos:
    /// * `buffer` - Almacenamiento temporal de las llamadas recursivas (memoization)
    /// * `base` - Combinación que actúa como raíz del arbol o sub-arbol de búsqueda
    /// * `objetivo` - El valor que deben satisfacer la suma de los valores de una combinación valida
    fn generar_combinaciones(
        buffer: &mut Vec<Combinacion>,
        base: Vec<Combinacion>,
        objetivo: &usize,
    ) {
        for combinacion in base {
            if let Some(nueva_base) = combinacion.derivar_desde_pendientes(objetivo) {
                Combinacion::generar_combinaciones(buffer, nueva_base, objetivo);
            }
            if combinacion.suma == *objetivo {
                buffer.push(combinacion);
            }
        }
    }

    /// Privada
    /// Sí contiene k elementos en pendientes, genera 0 a k combinaciones de tamaño r+1
    /// que los incluye sí su suma <= Objetivo.
    ///
    /// # Argumentos:
    /// * `objetivo` - El valor que deben satisfacer la suma de los valores de una combinación valida
    fn derivar_desde_pendientes(&self, objetivo: &usize) -> Option<Vec<Combinacion>> {
        if self.pendientes.is_empty() {
            return None;
        }
        let mut nuevas_combinaciones: Vec<Combinacion> = Vec::with_capacity(self.pendientes.len());
        for posicion in 0..self.pendientes.len() {
            // define la suma y sí esta es mayor al objetivo, no genera una nueva combinación
            let suma: usize = self.suma + self.pendientes[posicion];
            if suma > *objetivo {
                continue;
            }
            // Genera una nueva combinación extendiendo la original con el valor del indice i de pendientes.
            // Los pendiente de la nueva combinación corresponde a los indices i+1..n de pendientes de la combinación original.
            // Este paso es el que garantiza que no se repitan posiciones
            let mut nueva = self.clone();
            nueva.pendientes = nueva.pendientes.split_off(posicion);
            nueva.suma = suma;
            nueva.valores.push(nueva.pendientes.swap_remove(0));
            nuevas_combinaciones.push(nueva)
        }
        Some(nuevas_combinaciones)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn el_resultado_suma_objetivo() {
        let objetivo = 10;
        let secuencia = [11, 5, 3, 2, 7, 20, 1, 5, 4, 1, 3, 9, 11, 20, 13, 17];
        let resultado = Combinacion::desde_secuencia(&secuencia, &objetivo);
        for combinacion in resultado {
            assert_eq!(objetivo, combinacion.iter().sum());
        }
    }

    #[test]
    fn no_existe_combinacion() {
        let objetivo = 5;
        let secuencia = [11, 20, 15, 42, 13, 17];
        let resultado = Combinacion::desde_secuencia(&secuencia, &objetivo);
        assert!(resultado.is_empty());
    }

    #[test]
    fn caso_ejemplo() {
        let secuencia = [1, 5, 3, 2];
        let objetivo: usize = 6;
        let esperado = vec![vec![1, 2, 3], vec![1, 5]];
        let mut resultado = Combinacion::desde_secuencia(&secuencia, &objetivo);
        resultado.sort();
        assert_eq!(esperado, resultado);
    }

    #[test]
    fn caso_ejemplo_extendido() {
        let secuencia = [11, 5, 3, 2, 7, 20, 1, 5, 4];
        let objetivo: usize = 6;
        let esperado = vec![vec![1, 5], vec![2, 4], vec![3, 2, 1], vec![5, 1]];
        let mut resultado = Combinacion::desde_secuencia(&secuencia, &objetivo);
        resultado.sort();
        assert_eq!(esperado, resultado);
    }
}
