use clap::{Command, Arg};

use api::functions::decrementar;

mod api;

fn main() {
    let matches = Command::new("retos")
        .version("0.0.27")
        .author("Charly Ramirez, pingestudio@gamil.com")
        .about("Retos Semanales")
        .long_about("Reto #27: Cuenta atrás

        Crea una función que reciba dos parámetros para crear una cuenta atrás.
        - El primero, representa el número en el que comienza la cuenta.
        - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
        - Sólo se aceptan números enteros positivos.
        - El programa finaliza al llegar a cero.
        - Debes imprimir cada número de la cuenta atrás.")
        .arg_required_else_help(true)
        .subcommand(
        Command::new("decrementar")
            .about("Comando decrementar")
            .arg_required_else_help(true)
            .subcommand(
            Command::new("tiempo")
                .about("Crea una función que reciba dos parámetros para crear una cuenta atrás")
                .arg_required_else_help(true)
                .arg(Arg::new("comienza").required(true).value_parser(clap::value_parser!(u8)))
                .arg(Arg::new("segundos").required(true).value_parser(clap::value_parser!(u64)))
            )
        ).get_matches();

    match matches.subcommand() {
        Some(("decrementar", matchs_decrementar)) => match matchs_decrementar.subcommand() {
            Some(("tiempo", matches_timer)) => {
                let comienza = matches_timer.get_one::<u8>("comienza").expect("Solo recibe numeros enteros positivos").to_owned();
                let segundos = matches_timer.get_one::<u64>("segundos").unwrap().to_owned();
                decrementar(comienza, segundos);
            },
            _ => println!("No se encontraron subcomandos para decrementar")
        },
        _ => println!("No se encontraron subcomandos"),
    }
}
