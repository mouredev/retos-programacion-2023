// author: hdescobarh (Hans D. Escobar H.)

use mi_editor::Editor;
use std::path::PathBuf;

const RUTA_FICHERO_STR: &str = "./text.txt";

fn main() {
    let mut input_buffer = String::new();
    let ruta: PathBuf = PathBuf::from(RUTA_FICHERO_STR);
    let mut editor_activo: Editor;

    /*
    Valida que la ruta sea accesible, sí es accesible y no existe, crea el archivo.
    Sí es accesible y existe, pregunta sí abrir sobreescribiendo todo el contenido, o
    agregando las nuevas lineas al final del fichero.
    */
    if ruta.try_exists().unwrap() {
        let sobrescribir = cli::obtener_opcion_sobrescritura(&mut input_buffer);
        editor_activo = Editor::desde_fichero_existente(ruta, sobrescribir);
        if !sobrescribir {
            println!("\n{}", editor_activo.mostrar_buffer());
        }
    } else {
        editor_activo = Editor::desde_fichero_nuevo(ruta)
    };

    /*
    Inicia ciclo principal del programa.
    */
    loop {
        cli::input_de_linea_nueva(&mut input_buffer);
        editor_activo.escribir_linea(&input_buffer).unwrap();
    }
}

/// Modulo encargado de gestionar el fichero
pub mod mi_editor {
    use std::fs::{File, OpenOptions};
    use std::io::{Read, Write};
    use std::path::PathBuf;

    pub struct Editor {
        _ruta: PathBuf,
        fichero: File,
        buffer: String,
    }

    impl Editor {
        pub fn desde_fichero_nuevo(ruta: PathBuf) -> Self {
            // crea directorios sí no existen, luego crea el archivo
            if let Some(parent_path) = ruta.parent() {
                std::fs::create_dir_all(parent_path).unwrap()
            };
            let fichero = OpenOptions::new()
                .read(true)
                .write(true) // requerido por create_new
                .create_new(true) // create_new asegura que el archivo no exista
                .open(&ruta)
                .unwrap();

            Self {
                _ruta: ruta,
                fichero,
                buffer: String::new(),
            }
        }

        pub fn desde_fichero_existente(ruta: PathBuf, sobrescribir: bool) -> Self {
            let mut fichero = OpenOptions::new()
                .read(true)
                .write(true) // truncate requiere write(true)
                .append(!sobrescribir) // sí write y append son true, aplica append
                .truncate(sobrescribir)
                .open(&ruta)
                .unwrap();

            let mut buffer = String::new();
            fichero.read_to_string(&mut buffer).unwrap();
            Self {
                _ruta: ruta,
                fichero,
                buffer,
            }
        }

        pub fn escribir_linea(&mut self, linea: &String) -> std::io::Result<()> {
            //self.fichero.write_all(&buffer)
            write!(self.fichero, "{}", linea)
        }

        pub fn mostrar_buffer(&self) -> &String {
            &self.buffer
        }

        pub fn _mostrar_ruta(&self) -> &PathBuf {
            &self._ruta
        }
    }
}

/// modulo encargado de la interacción con el usuario a través de la linea de comandos
pub mod cli {
    use std::io;

    const PROMPT: &str = "Ingrese el texto >";
    const MSJ_SOBRESCRIBIR: &str = "
    El fichero ya existe, desea sobrescribirlo?
    0: No
    1: Sí:";
    const MSJ_OPCION_NO_VALIDA: &str = "Error: El número ingresado no es una opción valida.";

    // limpia el buffer y espera el input del usuario
    pub fn input_de_linea_nueva(input_buffer: &mut String) {
        input_buffer.clear();
        println!("{}", PROMPT);
        io::stdin().read_line(input_buffer).unwrap();
    }

    // Captura el input del usuario sí sobrescribir o no un archivo existente
    pub fn obtener_opcion_sobrescritura(input_buffer: &mut String) -> bool {
        loop {
            println!("{}", MSJ_SOBRESCRIBIR);
            io::stdin().read_line(input_buffer).unwrap();

            match input_buffer.trim().parse::<u8>() {
                Ok(0) => return false,
                Ok(1) => return true,
                _ => println!("{}", MSJ_OPCION_NO_VALIDA),
            }
        }
    }
}
