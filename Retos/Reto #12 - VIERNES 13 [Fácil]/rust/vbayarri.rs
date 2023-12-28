/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

 use chrono::Datelike;

// Función que detecta si existe un viernes 13 en el mes y el año indicados.
fn is_friday_13(month: u32, year: i32) -> bool {
    let date = chrono::NaiveDate::from_ymd_opt(year, month, 13);
    date.is_some() && date.unwrap().weekday() == chrono::Weekday::Fri
}

// Función principal recorriendo los meses y años hasta el 2050.
fn main() {

    for year in 2000..2050 {
        for month in 1..13 {
            if is_friday_13(month, year) {
                println!("{}-{}-13 es viernes 13", year, month);
            }
        }
    }
}

