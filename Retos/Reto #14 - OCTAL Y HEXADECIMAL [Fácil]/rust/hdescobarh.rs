// Define the accepted bases and their respective digits set
pub enum Base {
    Octal([char; 8]),
    Hexadecimal([char; 16]),
}

impl Base {
    pub fn value_at_index(&self, index: usize) -> &char {
        match self {
            Self::Hexadecimal(array) => &array[index],
            Self::Octal(array) => &array[index],
        }
    }

    pub fn base_size(&self) -> usize {
        match self {
            Self::Hexadecimal(_) => 16,
            Self::Octal(_) => 8,
        }
    }

    pub fn format_symbol(&self) -> &str {
        match self {
            Base::Octal(_) => "0o",
            Base::Hexadecimal(_) => "0x",
        }
    }
}

pub const HEXADECIMAL: Base = Base::Hexadecimal([
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
]);

pub const OCTAL: Base = Base::Octal(['0', '1', '2', '3', '4', '5', '6', '7']);

// Define the function to convert decimal numbers to some of the valid bases
pub fn convert_from_decimal(to: Base, decimal_number: isize) -> String {
    // recover and remove sign
    let sign: &str = {
        if decimal_number < 0 {
            "-"
        } else {
            ""
        }
    };
    let mut current_dec_value: usize = decimal_number.unsigned_abs();

    // convert and put in correct order the output
    let mut transformed: String = String::new();
    while current_dec_value > 0 {
        let remainer = current_dec_value.rem_euclid(to.base_size());
        transformed.push(*to.value_at_index(remainer));
        current_dec_value = current_dec_value.div_euclid(to.base_size());
    }
    transformed = transformed.chars().rev().collect();

    // format literal representation
    format!("{sign}{symbol}{transformed}", symbol = to.format_symbol())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn correctly_transforms_dec_to_hex() {
        let testing_pairs: [(isize, &str); 5] = [
            (2474064, "0x25C050"),
            (1140706, "0x1167E2"),
            (5141319, "0x4E7347"),
            (-7486729, "-0x723D09"),
            (-1824358, "-0x1BD666"),
        ];

        for (decimal_number, expected_literal) in testing_pairs {
            let hex_number = convert_from_decimal(HEXADECIMAL, decimal_number);
            assert_eq!(expected_literal, hex_number);
        }
    }

    #[test]
    fn correctly_transforms_dec_to_oct() {
        let testing_pairs: [(isize, &str); 5] = [
            (2474064, "0o11340120"),
            (1140706, "0o4263742"),
            (5141319, "0o23471507"),
            (-7486729, "-0o34436411"),
            (-1824358, "-0o6753146"),
        ];

        for (decimal_number, expected_literal) in testing_pairs {
            let oct_number = convert_from_decimal(OCTAL, decimal_number);
            assert_eq!(expected_literal, oct_number);
        }
    }
}
