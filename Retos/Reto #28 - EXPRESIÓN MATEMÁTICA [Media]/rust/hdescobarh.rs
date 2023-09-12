// author: hdescobarh (Hans D. Escobar H.)

/*
Con Regular Expressions (regex) la expresión valida es equivalente a:
    "^(\d+(\.\d+)?)(\u{0020}(\+|-|\*|/|%)\u{0020}(\d+(\.\d+)?))+$"
    
Sin embargo, Rust NO CUENTA CON métodos para manejar Regular Expressions
en su biblioteca estándar (https://doc.rust-lang.org/std/).

Esta solución se limita a usar la biblioteca estándar; por lo tanto, no se empleará regex.
*/

const OPERADORES_VALIDOS: [&str; 5] = ["+", "-", "*", "/", "%"];

/*
Resultados posibles de la validación de la expresión,
Su uso esta pensado sobre todo para debugging
 */
#[derive(Debug, PartialEq)]
enum Expresion {
    Valida,
    ContieneNoAscii,
    LongitudInvalida,
    ValoresNoNumericos,
    OperadorInvalido,
}

/**
 * Retorna verdadero sí la expresión matemática es valida.
 *  - El texto debe contener solo texto ASCII
 *  - El separador decimal es el punto
 *  - Operaciones validas: + - / % *
 *  - Los números y operadores deben estar separados por espacio (\t or \n no son validos)
 */
pub fn validar_expresion(expresion: &str) -> bool {
    matches!(validar(expresion), Expresion::Valida)
}

// privada, no pensada para el usuario final
fn validar(expresion: &str) -> Expresion {
    // Debe contener solo valores ASCII
    if !expresion.is_ascii() {
        return Expresion::ContieneNoAscii;
    };

    // El caracter de espacio valido es el caracter space https://www.compart.com/en/unicode/U+0020
    // Sí hay espacios seguidos generara str vacias
    let secuencia_caracteres: Vec<&str> = expresion.split('\u{0020}').collect();

    // Una secuencia valida tiene almenos 3 elementos y longitud impar
    if (secuencia_caracteres.len() % 2 == 0) | (secuencia_caracteres.len() < 3) {
        return Expresion::LongitudInvalida;
    };

    // El vector sigue la forma [numero, operador]  n veces + [numero]
    // entonces, primero evaluamos por pares los n [numero, operador]
    for indice in (0..(secuencia_caracteres.len() - 1)).step_by(2) {
        match secuencia_caracteres[indice].parse::<f32>() {
            Ok(_) => (),
            Err(_) => return Expresion::ValoresNoNumericos,
        };

        if !OPERADORES_VALIDOS.contains(&secuencia_caracteres[indice + 1]) {
            return Expresion::OperadorInvalido;
        };
    }
    // segundo, evaluamos el ultimo [numero]
    match secuencia_caracteres[secuencia_caracteres.len() - 1].parse::<f32>() {
        Ok(_) => (),
        Err(_) => return Expresion::ValoresNoNumericos,
    };

    Expresion::Valida
}

/*
Pruebas unitarias
*/
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn valida_enteros_operacion_simple() {
        // operadores y numeros validos
        assert_eq!(validar("0 + 6"), Expresion::Valida);
        assert_eq!(validar("356 - 60"), Expresion::Valida);
        assert_eq!(validar("5 * 16"), Expresion::Valida);
        assert_eq!(validar("1 / -6"), Expresion::Valida);
        assert_eq!(validar("500 % 6"), Expresion::Valida);
        // expresiones invalidas
        assert_eq!(validar("5 %  6"), Expresion::LongitudInvalida);
        assert_eq!(validar("5 %\t6"), Expresion::LongitudInvalida);
        assert_eq!(validar("5 % "), Expresion::ValoresNoNumericos);
        assert_eq!(validar("5 %"), Expresion::LongitudInvalida);
        assert_eq!(validar("a % 6"), Expresion::ValoresNoNumericos);
        assert_eq!(validar("２ % 6"), Expresion::ContieneNoAscii);
    }

    #[test]
    fn valida_enteros_operaciones_multiples() {
        // pasan
        assert_eq!(validar("0 + 6 - -10 / 60 * 100 % 3"), Expresion::Valida);
    }

    #[test]
    fn valida_flotantes_operaciones_multiples() {
        // pasan
        assert_eq!(
            validar("0.5 + 60 - -10.345 / 0.314159 * 100 % 5971.12"),
            Expresion::Valida
        );

        assert_eq!(validar("0,5 % 6"), Expresion::ValoresNoNumericos);
    }

    #[test]
    fn valida_funcion_publica() {
        assert!(validar_expresion("0 + 6"));
        assert!(!validar_expresion("5 % "));
        assert!(validar_expresion(
            "0.5 + 60 - -10.345 / 0.314159 * 100 % 5971.12"
        ))
    }
}
