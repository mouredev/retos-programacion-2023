// author: Hans D. Escobar H. (hdescobarh)
#![crate_name = "triples_pitagoricos"]
#![crate_type = "cdylib"]
use std::cmp::min;

/// Representa un triple pitagórico.
///
/// Un triple pitagórico se define como un conjunto de tres números {a, b, c}
/// que satisfacen a² + b² = c², tal que a,b,c ∈ ℤ⁺.
/// Un triple cumple que a > b > c, por lo que se puede anotar como (a,b,c)
#[derive(PartialEq, Eq, Hash, Debug)]
pub struct TriplePitagorico {
    cateto_menor: usize,
    cateto_mayor: usize,
    hipotenusa: usize,
}

impl TriplePitagorico {
    /// Genera todos los triples pitagóricos que satisfacen que su máximo
    /// valor es menor o igual a un entero positivo r constante.
    ///
    /// # Descripción:
    /// Como un triple pitagórico satisface que a < b < c, una estrategia sencilla es por cada
    /// b < r explorar cada a < b y encontrar los sqrt(a² + b²) enteros menores o iguales a r.
    /// Esta implementación además aprovecha que a < sqrt(r² - b²) + 1.
    ///
    /// El problema es equivalente a, dada una constante constante r ∈ ℤ⁺ y las variables a,b,c ∈ ℤ⁺,
    /// encontrar los triples pitagóricos (a,b,c) tales que a² + b² = c² ≤ r².
    ///
    /// * (1) a, b, c, r ∈ ℤ⁺ (condición)
    /// * (2) a² + b² = c² ≤ r² (condición)
    /// * (3) 1 ≤ a < b < c ≤ r (por 1 y 2)
    /// * (4) a² ≤ r² - b² ⇒ a ≤ sqrt(r² - b²) ⇒ a < sqrt(r² - b²) + 1 (por 2 y 3)
    /// * (5) a < min(b, sqrt(r² - b²) + 1) (por 3 y 4)
    ///
    /// # Argumentos:
    /// * `numero` - indica el máximo valor que puede aparecer en los triples pitagóricos generados.
    ///
    /// # Ejemplo:
    ///
    /// ```
    /// use triples_pitagoricos::TriplePitagorico;
    /// let resultado = TriplePitagorico::desde_numero_maximo(&14).unwrap();
    /// //Retorna los triples (3,4,5), (6,8,10), (5,12,13)
    /// println!("{:?}", resultado);
    ///
    /// ```
    pub fn desde_numero_maximo(numero: &usize) -> Option<Vec<TriplePitagorico>> {
        let mut triples: Vec<Self> = Vec::new();
        // Sí (a, b, c) es un triple pitagórico, 2 < a < b < c <= numero
        for b in 3..*numero {
            let limite_busqueda = min(
                b,
                ((numero.pow(2) - b.pow(2)) as f64).sqrt().floor() as usize + 1,
            );
            for a in 2..limite_busqueda {
                // Sí a² + b² son catetos de un triple pitagórico, necesariamente forman un cuadrado perfecto
                if let Some(c) = raiz_cuadrada_perfecta(&(a.pow(2) + b.pow(2))) {
                    triples.push(Self {
                        cateto_menor: a,
                        cateto_mayor: b,
                        hipotenusa: c,
                    })
                };
            }
        }
        if triples.is_empty() {
            None
        } else {
            Some(triples)
        }
    }
}

/// Retorna la raíz de número sí este es un cuadrado perfecto
fn raiz_cuadrada_perfecta(numero: &usize) -> Option<usize> {
    let raiz_entera = (*numero as f64).sqrt().floor() as usize;
    if raiz_entera.pow(2) == *numero {
        Some(raiz_entera)
    } else {
        None
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::collections::HashSet;

    #[test]
    fn no_hay_triple_para_valor() {
        let resultado = TriplePitagorico::desde_numero_maximo(&4);
        assert_eq!(None, resultado);
    }
    #[test]
    fn genera_triple_y_multiplo() {
        let resultado: HashSet<TriplePitagorico> = TriplePitagorico::desde_numero_maximo(&10)
            .unwrap()
            .into_iter()
            .collect();
        let esperado: HashSet<TriplePitagorico> = [[3, 4, 5], [6, 8, 10]]
            .into_iter()
            .map(|tripla| TriplePitagorico {
                cateto_menor: tripla[0],
                cateto_mayor: tripla[1],
                hipotenusa: tripla[2],
            })
            .collect();
        assert_eq!(esperado, resultado);
    }

    #[test]
    fn genera_triples_menores_o_iguales() {
        let resultado: HashSet<TriplePitagorico> = TriplePitagorico::desde_numero_maximo(&25)
            .unwrap()
            .into_iter()
            .collect();
        let esperado: HashSet<TriplePitagorico> = [
            [3, 4, 5],
            [6, 8, 10],
            [5, 12, 13],
            [9, 12, 15],
            [8, 15, 17],
            [12, 16, 20],
            [15, 20, 25],
            [7, 24, 25],
        ]
        .into_iter()
        .map(|tripla| TriplePitagorico {
            cateto_menor: tripla[0],
            cateto_mayor: tripla[1],
            hipotenusa: tripla[2],
        })
        .collect();
        assert_eq!(esperado, resultado);
    }
}
