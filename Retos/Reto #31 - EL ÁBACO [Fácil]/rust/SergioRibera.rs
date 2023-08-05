/*
 * Crea una función que sea capaz de leer el número representado por el á
baco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para reali
zar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último la
s unidades.
 * - El número en cada elemento se representa por las cuentas que están a
 la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *
 *  Resultado: 1.302.790
 */

///
/// Para correr los test corre los siguientes comandos
///
/// rustc --test SergioRibera.rs
/// ./SergioRibera
///
///

//
//
//  La Solucion
//
//
fn to_number(arr: &[&str]) -> String {
    // La solucion es relativamente sencilla
    // Solo dividimos cada elemento en 2
    // separados por ---
    arr.iter()
        .flat_map(|a| {
            let mut split = a.splitn(2, "---");
            // Luego agarramos el primer elemento
            // la funcion next() nos devuelve un Option<T>
            // Si es Some(T) pasa por el map
            // Es decir si existe un primer valor
            // En caso de que exista solo lo cambiamos
            // por la longitur del texto
            //
            // Ej: OOO---OOOOOO
            //     ^^^
            //      3 => len
            //
            split.next().map(|s| s.len().to_string())
        })
        // recogemos todo como un arreglo de String
        .collect::<Vec<String>>()
        // Juntamos todo en un solo String
        .join("")
        // Quitamos los 0 del principio
        // Para los casos de
        // 001.235.548
        // ^^
        .trim_start_matches('0')
        // Convertimos todo a texto porque
        // la funcion anterior devuelve &str
        .to_string()
}

// Separar la logica de colocar los . de centena
//
// Se puede ignorar
//
fn format_number(input: &str) -> String {
    input
        .chars()
        .rev()
        .collect::<Vec<_>>()
        .chunks(3)
        .map(|chunk| chunk.iter().collect::<String>())
        .collect::<Vec<_>>()
        .join(".")
        .chars()
        .rev()
        .collect::<String>()
}

#[test]
fn moure_example() {
    let arr = &[
        "O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO",
    ];
    let res = to_number(arr);
    assert_eq!(res, "1302790");

    let formated = format_number(&res);
    assert_eq!(&formated, "1.302.790");
}

#[test]
fn six_number() {
    let arr = &[
        "---0OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO",
    ];
    let res = to_number(arr);
    assert_eq!(res, "302790");

    let formated = format_number(&res);
    assert_eq!(&formated, "302.790");
}

#[test]
fn one_dot() {
    let arr = &[
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO",
    ];
    let res = to_number(arr);
    assert_eq!(res, "2790");

    let formated = format_number(&res);
    assert_eq!(&formated, "2.790");
}

#[test]
fn first_value_all_zero() {
    let arr = &[
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
    ];
    let res = to_number(arr);
    assert_eq!(res, "3000000");

    let formated = format_number(&res);
    assert_eq!(&formated, "3.000.000");
}

#[test]
fn empty_input() {
    let arr = &[];
    let res = to_number(arr);
    assert_eq!(res, "");

    let formated = format_number(&res);
    assert_eq!(&formated, "");
}

#[test]
fn empty_values_input() {
    let arr = &[
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
    ];
    let res = to_number(arr);
    assert_eq!(res, "");

    let formated = format_number(&res);
    assert_eq!(&formated, "");
}
