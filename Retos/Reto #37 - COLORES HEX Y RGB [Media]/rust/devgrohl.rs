/*
* Crea las funciones capaces de transformar colores HEX
* a RGB y viceversa.
* Ejemplos:
* RGB a HEX: r: 0, g: 0, b: 0 -> #000000
* HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
*/

use std::io::{self, Write};

#[derive(Debug)]
struct Color {
    red: u8,
    green: u8,
    blue: u8
}

fn hexCharToInt(c: &str) -> u8 {
    if c >= "0" && c <= "9" {
        c.parse::<u8>().unwrap()
    } else {
        match c.parse::<char>() {
            Ok('A') => 10,
            Ok('B') => 11,
            Ok('C') => 12,
            Ok('D') => 13,
            Ok('E') => 14,
            Ok('F') => 15,
            Err(_)  => todo!(),
            Ok('\0'..='@') | Ok('G'..='\u{d7ff}') | Ok('\u{e000}'..='\u{10ffff}') => todo!(),
        }
    }
}

fn intToHex(i: u8) -> String{
    if i >= 0 && i <= 9 {
        i.to_string()
    } else {
        match i {
            10 => "A".to_string(),
            11 => "B".to_string(),
            12 => "C".to_string(),
            13 => "D".to_string(),
            14 => "E".to_string(),
            15 => "F".to_string(),
            _  => todo!()
        }
    }
}

fn hex2int(hex_str: &str) -> u8 {
    let left = &hex_str[0..1];
    let right = &hex_str[1..2];

    ( 16 * hexCharToInt(left) ) + hexCharToInt(right)
}

fn hex2rgb(hex_value: &str) -> Color {
    Color{
        red: hex2int(&hex_value[0..2]),
        green: hex2int(&hex_value[2..4]),
        blue: hex2int(&hex_value[4..6])
    }
    
}

fn rgb2hex(rgb: Color) -> String {
    let mut result: String = Default::default();

    result.push_str(intToHex(rgb.red/16).as_str());
    result.push_str(intToHex(rgb.red%16).as_str());
    result.push_str(intToHex(rgb.green/16).as_str());
    result.push_str(intToHex(rgb.green%16).as_str());
    result.push_str(intToHex(rgb.blue/16).as_str());
    result.push_str(intToHex(rgb.blue%16).as_str());

    result
}

fn main () -> io::Result<()> {
    let mut buffer = String::new();
    let mut r = String::new();
    let mut g = String::new();
    let mut b = String::new();

    print!("Insert a Hex Value: #");
    io::stdout().flush().unwrap();
    io::stdin()
        .read_line(&mut buffer)
        .expect("Failed to read from STDIN");

    let hex_value = buffer.trim();

    if hex_value.len() > 6 {
        println!("Inserted value is longer than a HEX value: {:?}, lenght: {:?}", hex_value, hex_value.len());
    }
    
    if !buffer.is_empty() {
        let c = hex2rgb(&buffer);
        println!("{:?}", c);
    }

    print!("Insert an RGB value in the form: \n<R>: ");
    io::stdout().flush().unwrap();
    io::stdin()
        .read_line(&mut r)
        .expect("Failed to read from STDIN");

    print!("<G>: ");
    io::stdout().flush().unwrap();
    io::stdin()
        .read_line(&mut g)
        .expect("Failed to read from STDIN");

    print!("<B>: ");
    io::stdout().flush().unwrap();
    io::stdin()
        .read_line(&mut b)
        .expect("Failed to read from STDIN");

    let color = Color {
        red: r.trim().parse::<u8>().unwrap(),
        green: g.trim().parse::<u8>().unwrap(),
        blue: b.trim().parse::<u8>().unwrap()
    };

    println!("{:?}", color);

    println!("{:?}", rgb2hex(color));

    Ok(())
}