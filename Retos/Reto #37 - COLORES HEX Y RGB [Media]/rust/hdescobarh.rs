// author: Hans D. Escobar H. (hdescobarh)

const ERROR_MSG: &str = "Formato invalido";

/***
 * Bajo el esquema True Color (24 bits) los colores se representan como una tripleta (Red, Green, Blue),
 * La notación RGB o HEX cambia la forma en que se representan los valores:
 * - RGB: como una tupla de decimales de 8 bits (0-255)
 * - HEX: hexadecimales de 8 bits escritos en dos dígitos (00-FF), concatenados y con trailing "#". Preserva el orden RGB.
 */
pub struct TrueColor {
    red: u8,
    green: u8,
    blue: u8,
}

impl TrueColor {
    /// Crea un TrueColor desde una cadena de texto en formato Hexadecimal de 6 dígitos
    /// es case-insensitive: e.g., "#CD853F", "#cd853f", "#cD853f", son validos
    pub fn from_hex(value: String) -> Self {
        /* Transforma la String en un iterador de caracteres y
        valida que tenga "#" como trailing character */
        let mut chars = value.chars();
        if chars.next().unwrap() != '#' {
            panic!("{ERROR_MSG}")
        };

        /* Toma los demas caracteres del iterador, los separa parejas,
        y cada pareja trata de interpretarla como un literal en base 16 (hexadecimal)*/
        let valores = chars
            .collect::<Vec<char>>()
            .chunks(2)
            .map(|chunck| u8::from_str_radix(&String::from_iter(chunck), 16).expect("{ERROR_MSG}"))
            .collect::<Vec<u8>>();
        if valores.len() != 3 {
            panic!("{ERROR_MSG}")
        };

        TrueColor {
            red: valores[0],
            green: valores[1],
            blue: valores[2],
        }
    }

    /// Genera una String con el color en formato HEX
    fn get_hex(&self) -> String {
        // la notación 0>2 indica que sí el número formateado tiene ancho menor que
        // dos, entonces agrega un 0 alineado a la derecha
        format!("#{:0>2X}{:0>2X}{:0>2X}", self.red, self.green, self.blue)
    }

    /// Crea un TrueColor desde una tripleta de valores de 8-bits (0-255)
    pub fn from_rgb(red: u8, green: u8, blue: u8) -> Self {
        // Los valores ya son unsigned de 8 bits. No hace falta validaciones adicionales
        TrueColor { red, green, blue }
    }

    /// Genera una String con el color en formato RGB
    fn get_rgb(&self) -> String {
        format!("(r: {}, g: {}, b: {})", self.red, self.green, self.blue)
    }

    /// Traduce de una notación RGB valida a un HEX
    pub fn rgb2hex(red: u8, green: u8, blue: u8) -> String {
        let true_color = Self::from_rgb(red, green, blue);
        true_color.get_hex()
    }
    /// Traduce de una notación HEX valida a RGB
    pub fn hex2rgb(value: String) -> String {
        let true_color = Self::from_hex(value);
        true_color.get_rgb()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    // Crea un alias para tipo existentes
    type TestCase = (&'static str, (u8, u8, u8), &'static str, &'static str);

    // Esto sería mas adecuado en un archivo aparte.
    const VALID_TEST_CASES: [TestCase; 8] = [
        ("Black", (0, 0, 0), "#000000", "(r: 0, g: 0, b: 0)"),
        (
            "White",
            (255, 255, 255),
            "#FFFFFF",
            "(r: 255, g: 255, b: 255)",
        ),
        (
            "RosyBrown",
            (188, 143, 143),
            "#BC8F8F",
            "(r: 188, g: 143, b: 143)",
        ),
        (
            "DarkTurquoise",
            (0, 206, 209),
            "#00CED1",
            "(r: 0, g: 206, b: 209)",
        ),
        (
            "GhostWhite",
            (248, 248, 255),
            "#F8F8FF",
            "(r: 248, g: 248, b: 255)",
        ),
        (
            "Turquoise - lowercase",
            (64, 224, 208),
            "#40e0d0",
            "(r: 64, g: 224, b: 208)",
        ),
        (
            "SlateBlue - lowercase",
            (106, 90, 205),
            "#6a5acd",
            "(r: 106, g: 90, b: 205)",
        ),
        (
            "Peru - mixedcase",
            (205, 133, 63),
            "#cD853f",
            "(r: 205, g: 133, b: 63)",
        ),
    ];

    const BAD_TEST_CASES: [TestCase; 4] = [
        ("Sin trailing #", (0, 0, 0), "FFFFFF", ""),
        ("Formato 3 valores", (0, 0, 0), "FFF", ""),
        ("Mas valores de los esperados", (0, 0, 0), "#FFFFFFFF", ""),
        (
            "No son valores hexadecimales validos",
            (0, 0, 0),
            "#FHFHFH",
            "",
        ),
    ];

    #[test]
    fn traduce_rgb2hex() {
        for case in VALID_TEST_CASES {
            let (_, (red, green, blue), hex_str, _) = case;
            assert_eq!(
                TrueColor::rgb2hex(red, green, blue),
                hex_str.to_ascii_uppercase()
            )
        }
    }

    #[test]
    fn traduce_hex2rgb() {
        for case in VALID_TEST_CASES {
            let (_, _, hex_str, rgb_str) = case;
            assert_eq!(TrueColor::hex2rgb(hex_str.to_string()), rgb_str)
        }
    }

    #[test]
    #[should_panic(expected = "Formato invalido")]
    fn fails_from_hex_string() {
        for case in BAD_TEST_CASES {
            let (_, _, hex_str, _) = case;
            TrueColor::hex2rgb(hex_str.to_string());
        }
    }
}
