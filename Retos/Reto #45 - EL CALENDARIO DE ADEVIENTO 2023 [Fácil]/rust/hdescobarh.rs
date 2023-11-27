// author: Hans D. Escobar H. (hdescobarh)

/*
Solución con el mínimo de bibliotecas externas. Solo emplea rand para generar números aleatorios.

Esta organizada en tres módulos:
- giveaway_data: contiene las entidades encargadas del acceso a los medios de persistencia.
- giveaway: se encarga de la logica de negocio
- giveaway_cli: interfaz de linea de comandos

Cargo manifest:
[package]
name = "giveaway"
version = "0.1.0"
edition = "2021"
[dependencies]
rand = "0.8.5"
*/

use giveaway::Giveaway;
use giveaway_cli::Cli;
use giveaway_data::MockRepository;

fn main() {
    // inicializa la interfaz de linea de comandos
    let mut cli = Cli::default();
    // inicializa el controlador y el repositorio, uno falso para el ejercicio.
    let mut giveaway = Giveaway::new(MockRepository::default());
    loop {
        let state = cli.run(&mut giveaway);
        println!("{}", state);
    }
}

// command line interface module
pub mod giveaway_cli {
    use crate::giveaway::{Giveaway, Request};

    const PROMPT_OPTION: &str = "\n\
    Ingrese el número de la acción que desea realizar:
    1 Agregar participante.
    2 Mostrar todos los participantes.
    3 Eliminar a un participante.
    4 Realizar el sorteo.
    5 Salir.";
    const PROMPT_USERNAME: &str = "Por favor ingrese el nombre de usuario del participante.";
    const MSG_INVALID_OPTION: &str = "La opción ingresada no es valida.";
    const MSG_EXIT: &str = "Cerrando el programa. Hasta pronto.";

    #[derive(Default)]
    pub struct Cli {
        buffer: String,
    }

    impl Cli {
        pub fn run(&mut self, giveaway: &mut Giveaway) -> String {
            self.buffer.clear();
            println!("{}", PROMPT_OPTION);

            std::io::stdin().read_line(&mut self.buffer).unwrap();

            let choice = match self.buffer.trim().parse::<usize>() {
                Ok(number) => {
                    if (1..=5).contains(&number) {
                        number
                    } else {
                        return MSG_INVALID_OPTION.to_string();
                    }
                }
                Err(_) => return MSG_INVALID_OPTION.to_string(),
            };

            match choice {
                1 => giveaway.request(Request::AddParticipant, Some(self.ask_username())),
                2 => giveaway.request(Request::ListParticipants, None),
                3 => giveaway.request(Request::RemoveParticipant, Some(self.ask_username())),
                4 => giveaway.request(Request::Draw, None),
                5 => {
                    println!("{}", MSG_EXIT);
                    std::process::exit(0)
                }
                _ => panic!("Unexpected error: allowed choice out of bounds."),
            }
        }

        fn ask_username(&mut self) -> &str {
            self.buffer.clear();
            println!("{}", PROMPT_USERNAME);
            std::io::stdin().read_line(&mut self.buffer).unwrap();
            self.buffer.trim()
        }
    }
}

pub mod giveaway {
    use crate::giveaway_data::{ErrorKind, Participant, Repository};
    use rand::seq::SliceRandom;
    use std::fmt::Display;

    const MSG_ERR_NOT_FOUND: &str = "El participante no existe.";
    const MSG_ERR_ALREADY_EXIST: &str = "El participante ya se encuentra en el sorteo.";
    const MSG_ERR_EMPTY_DATA: &str = "No hay participantes en el sorteo.";
    const MSG_SUCCESS_ADDING: &str = "Se ha agregado un al participante.";
    const MSG_SUCCESS_DELETING: &str = "El participante ha sido removido.";
    const MSG_WARNING_MISSING: &str = "Faltó el nombre de usaurio.";
    const MSG_WINNER: &str = "El ganador es el usuario";

    pub struct Giveaway {
        repository: Box<dyn Repository + 'static>,
    }

    impl Giveaway {
        pub fn new(repository: impl Repository + 'static) -> Self {
            Self {
                repository: Box::new(repository),
            }
        }

        pub fn request(&mut self, kind: Request, username: Option<&str>) -> String {
            match kind {
                Request::AddParticipant => match username {
                    Some(username) => self.add_participant(username),
                    None => MSG_WARNING_MISSING.to_string(),
                },
                Request::ListParticipants => self.get_all_participants(),
                Request::RemoveParticipant => match username {
                    Some(username) => self.remove_participant(username),
                    None => MSG_WARNING_MISSING.to_string(),
                },
                Request::Draw => self.draw(),
            }
        }

        // Agrega un nuevo participante
        fn add_participant(&mut self, username: &str) -> String {
            match self.repository.create(Participant {
                username: username.to_owned(),
            }) {
                Ok(_) => MSG_SUCCESS_ADDING.to_string(),
                Err(e) => format!("{e}"),
            }
        }

        // Lista todos los participantes
        fn get_all_participants(&self) -> String {
            match self.repository.read_all() {
                Ok(l) => String::from_iter(
                    l.into_iter()
                        .map(|participant| format!("- {}\n", participant.username)),
                ),
                Err(e) => format!("{e}"),
            }
        }

        // Remueve por nombre de usuario a un participante
        fn remove_participant(&mut self, username: &str) -> String {
            match self.repository.delete(username) {
                Ok(_) => MSG_SUCCESS_DELETING.to_string(),
                Err(e) => format!("{e}"),
            }
        }

        // Obtiene un ganador y lo remueve de la lista de participantes
        fn draw(&mut self) -> String {
            let mut rng = rand::thread_rng();
            let participants = match self.repository.read_all() {
                Ok(l) => l,
                Err(e) => return format!("{e}"),
            };

            let winner = match participants.choose(&mut rng) {
                Some(participant) => participant.username.to_owned(),
                None => return format!("{}", ErrorKind::Empty),
            };
            match self.repository.delete(&winner) {
                Ok(_) => format!("{} {}.", MSG_WINNER, winner),
                Err(e) => format!("{e}"),
            }
        }
    }

    pub enum Request {
        AddParticipant,
        ListParticipants,
        RemoveParticipant,
        Draw,
    }

    impl Display for ErrorKind {
        fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
            let msg = match self {
                ErrorKind::NotFound => MSG_ERR_NOT_FOUND,
                ErrorKind::AlreadyExist => MSG_ERR_ALREADY_EXIST,
                ErrorKind::Empty => MSG_ERR_EMPTY_DATA,
            };
            write!(f, "{msg}")
        }
    }
}

pub mod giveaway_data {

    // Las nombres de usuario de Twitter son únicos, por lo que pueden usarse como identificadores únicos del participante
    #[derive(PartialEq, Clone)]
    pub struct Participant {
        pub username: String,
    }

    pub trait Repository {
        fn create(&mut self, participant: Participant) -> Result<(), ErrorKind>;
        fn read_all(&self) -> Result<Vec<Participant>, ErrorKind>;
        fn delete(&mut self, username: &str) -> Result<(), ErrorKind>;
    }

    #[non_exhaustive]
    pub enum ErrorKind {
        NotFound,
        AlreadyExist,
        Empty,
    }

    // Para el ejercicio la "conexión" será falseada por una simple colección
    pub struct MockRepository {
        connection: Vec<Participant>,
    }

    impl MockRepository {
        fn get_username_index(&self, username: &str) -> Result<usize, ErrorKind> {
            for (index, entry) in self.connection.iter().enumerate() {
                if entry.username == username {
                    return Ok(index);
                }
            }
            Err(ErrorKind::NotFound)
        }
    }

    impl Default for MockRepository {
        fn default() -> Self {
            Self {
                connection: Vec::from(
                    [
                        "QuantumFracture",
                        "mouredev",
                        "midudev",
                        "sama",
                        "neiltyson",
                        "HiromuArakawa",
                    ]
                    .map(|i| Participant {
                        username: i.to_string(),
                    }),
                ),
            }
        }
    }

    impl Repository for MockRepository {
        fn create(&mut self, participant: Participant) -> Result<(), ErrorKind> {
            if self.connection.contains(&participant) {
                return Err(ErrorKind::AlreadyExist);
            }

            self.connection.push(participant);
            Ok(())
        }

        fn read_all(&self) -> Result<Vec<Participant>, ErrorKind> {
            if self.connection.is_empty() {
                Err(ErrorKind::Empty)
            } else {
                Ok(Vec::from_iter(self.connection.iter().cloned()))
            }
        }

        fn delete(&mut self, username: &str) -> Result<(), ErrorKind> {
            let index = self.get_username_index(username)?;
            self.connection.swap_remove(index);
            Ok(())
        }
    }
}
