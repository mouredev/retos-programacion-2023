// author: hdescobarh (Hans D. Escobar H.)

fn main() {
    // ----------------------------------------------
    // ◆◆◆◆ ◆◆◆◆ TABLA DE CONTENIDO ◆◆◆◆ ◆◆◆◆
    // ----------------------------------------------

    // ▶ 0. Onwership system
    ownership_system();

    // ▶ 1. Hola mundo
    hola_mundo();

    // ▶ 2. Asignación variables
    asignando_variables();

    // ▶ 3. Tipos primitivos
    tipos_primitivos_escalares();
    caracteres_en_rust();
    tipos_primitivos_compuestos();
    y_donde_estan_las_strings();

    // ▶ 4. Definiendo funciones
    una_funcion_sin_parametros();
    una_funcion_con_parametros("¡Hola! Soy Ferris el cangrejo, la mascota no oficial de Rust 🦀");

    // ▶ 5. Estructuras de control I: conditional branching and loops
    condicionales(2, 21);
    uso_de_loops();

    // ▶ 6. Tipos personalizados
    las_structures();
    los_enums();

    // ▶ 7. Estructuras de control II: match control flow
    println!("{}", match_y_flujo_de_control(42));

    // ▶ 8. Otros tipos de la biblioteca estándar
    uso_de_option();
    uso_de_vectores();
    uso_de_hashmaps();

    // ▶ 9.Manejo de errores
    // panic! y Result son la interfaz primaria para el manejo de errores
    macro_panic();
    tipo_result();
    let _ = propagacion_de_errores();

    // ----------------------------------------------
    // ----------------------------------------------
}

// ▶▶▶▶▶ 0. Onwership system ◀◀◀◀◀

fn ownership_system() {
    // Esta es una caracteristica propia de Rust, para entenderla se requiere abordar
    // conceptos de uso de memoria y el scope, lo que excende los propositos de este documento.
    // Recomiendo checar ese tema aquí: https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html

    // En adición, conviene tener clara la diferencia entre expresiones y sentencias: https://doc.rust-lang.org/reference/statements-and-expressions.html)
}

// ▶▶▶▶▶ 1. Hola mundo ◀◀◀◀◀

fn hola_mundo() {
    println!("¡Hola mundo! 🦀");
}

// ▶▶▶▶▶ 2. Asignación variables ◀◀◀◀◀

fn asignando_variables() {
    // Rust es de tipado estatico y fuerte.
    // Las variables se declaran con la keyword 'let', seguido de el nombre, dos puntos, y el tipo
    let _asignando_un_numero: i32 = 10;
    // Rust cuenta con inferencia de tipo, por lo que se podria omitir el tipo:
    let _este_tambien_es_valido = 10; // toma el tipo i32, el tipo por defecto de entero

    // Por defecto las variables son INMUTABLES. Para hacerlas mutables se adiciona la keyword 'mut'
    let _esto_es_inmutable = 50;
    let mut esto_es_mutable = 42;
    assert_eq!(42, esto_es_mutable);
    esto_es_mutable = 50;
    assert_eq!(50, esto_es_mutable);

    // Para declarar constantes se usa la keyword 'const', la convención es mayuscula para el nombre
    const _ESTO_ES_UNA_CONSTANTE: f64 = 6.62607015e-34;
}

// ▶▶▶▶▶ 3. Tipos primitivos  ◀◀◀◀◀

fn tipos_primitivos_escalares() {
    // Rust maneja diferentes tipos de enteros según:
    //          1. Sí admiten negativos: signed (i) o unsigned (u).
    //          2. Tamaño de bits: 8, 16, 32, 64, 128, arch (size)

    let _entero_de_8_bits_unsigned: u8 = 200;
    let _entero_negativo_de_32_bits: i64 = -5230;
    let _entero_arch_unsigned: usize = 1024; // el tamaño de bits depende de la arquitectura del procesador

    // Los números de punto flotante (f) primitivos son de dos tipos:
    //          - Presición simple, de 32 bits.
    //          - Presición doble, de 64 bits.

    let _flotante_simple: f32 = 1.618_034; // tip: se puede usar underscore para mejorar la legibilidad
    let _flotante_doble: f64 = 1.618_033_988_749_894;

    // El tipo booleano solo tiene dos valores:
    let _esto_es_falso: bool = false;
    let _esto_es_verdadero: bool = true;

    // Rust tiene un tipo especial de escalar llamado 'Unit' o '()' con UN SOLO valor: ().
    let _unico_valor_del_tipo_unit = ();
}

fn caracteres_en_rust() {
    // El tipo caracter o char tambien es un tipo primitivo,
    // pero merece su propia sección porque puede ser complejo de manejar
    // sí no se conoce como funcionan los sistemas de códificación de caracteres.
    // Rust define un caracter como un 'UNICODE SCALAR VALUE'.
    // ...
    // De forma MUY breve: el Estandar Unicode define un conjunto de caracteres
    // codificados ('encoded character set'), y un mapa entre dicho conjunto y otro
    // conjunto de enteros no-negativos ('code points') denominado el 'codespace'.
    // El conjunto de 'unicode scalar values' es un SUBCONJUNTO del 'codespace'.
    // Se sugiere revisar los terminos entre comillas en este glosario: https://www.unicode.org/glossary/

    // Por ejemplo, 'ϵ' mapea a 0x3B5 (https://www.compart.com/en/unicode/U+03B5)
    let la_letra_epsilon: char = 'ϵ';
    let este_tambien_es_epsilon: char = '\u{03F5}';
    assert_eq!(la_letra_epsilon, este_tambien_es_epsilon); // pass

    // Un Unicode Scalar Value puede diferir notablemente de lo que la intuición nos dice que es un caracter:

    // Por ejemplo, este dragón
    let _este_dragon_tambien_es_un_caracter: char = '🐉';

    // Otro ejemplo. El caracter Latin Small Letter E with Acute (https://www.compart.com/en/unicode/U+00E9),
    // es el mismo elemento del encoded character set,
    // pero aquí esta representado en un solo code point, 0xE9
    println!("Esta 'é' es UN caracter: {:?}", "é".chars()); // Chars(['é'])
                                                            // y aquí esta representado con DOS code points: 0x65 0x301
    println!("Esta 'é' son DOS caracteres: {:?}", "é".chars()); // Chars(['e', '\u{301}'])
}

fn tipos_primitivos_compuestos() {
    // Su TAMAÑO es constante y conocido en tiempo de compilación.

    // La tupla soporta mas de un tipo
    let mut esto_es_una_tupla: (char, u8, i32) = ('👽', 42, -999);
    esto_es_una_tupla.0 = '🛸';
    assert_eq!('🛸', esto_es_una_tupla.0);

    // el array soporta un solo tipo
    let mut esto_es_un_array: [usize; 4] = [1, 9, 8, 9];
    esto_es_un_array[3] = 42;
    assert_eq!(42, esto_es_un_array[3]);

    // Hay mas tipos primitivos, como el slice o reference. Pero primero se requiere
    // entender el 'Ownership sytem'
}

fn y_donde_estan_las_strings() {
    // las Strings NO son primitivos,
    // son structures (struct), algo parecido a las clases (mas detalles en sección "tipos personalizados")
    // y son parte de la biblioteca estandar (https://doc.rust-lang.org/std/index.html#the-rust-standard-library).

    // El tipo String son secuencias de bytes almacenados como valores UTF-8 validos
    let _saludo = String::from("Hola");

    // IMPORTANTE: el tipo String NO SON secuencias caracteres. Por ejemplo:
    // el caracter ñ mapea al code point 0xF1,
    let esto_es_un_caracter = 'ñ';
    assert_eq!(4, std::mem::size_of::<char>()); // el tipo char tiene un tamaño fijo de CUATRO bytes

    // ñ bajo el esquema UTF-8 mapea la SECUENCIA de DOS bytes: 0xC3 0xB1 (195 177 en decimal) https://unicode.org/glossary/#unicode_encoding_form)
    let esto_es_una_string = String::from(esto_es_un_caracter); // representemos la ñ como String
    assert_eq!([195u8, 177u8], esto_es_una_string.as_bytes()); // coincide con la secuencia y tamaño esperados
}

// ▶▶▶▶▶ 4. Definiendo funciones  ◀◀◀◀◀

// Para definir funciones se emplea la keyword 'fn'

fn una_funcion_sin_parametros() -> String {
    // Se puede usar la keyword return, o, sí termina en expresión se puede omitir
    "No tiene parametros, pero retorna un tipo String".to_string()
}

fn una_funcion_con_parametros(mensaje: &str) {
    // Esta función tiene parametros, pero retorna nada; es decir, retorna el tipo 'unit' ()
    println!("{}", mensaje)
}

// ▶▶▶▶▶  5. Estructuras de control I: conditional branching and loops  ◀◀◀◀◀

fn condicionales(numero1: usize, numero2: usize) {
    let primero_es_par = numero1 % 2 == 0;
    let segundo_es_par = numero2 % 2 == 0;

    // multiples condiciones
    if primero_es_par && segundo_es_par {
        println!("Ambos son pares");
    } else if !primero_es_par && !segundo_es_par {
        println!("Ambos son impares");
    } else {
        println!("Alguno es impar y el otro par");
    }

    // Asignación de variable con condicional.

    let mensaje = if primero_es_par || segundo_es_par {
        "El producto es par"
    } else {
        "El producto es impar"
    };
    println!("{}", mensaje);
}

fn uso_de_loops() {
    // loop condicional - while
    const VALOR_MAXIMO_PERMITIDO: i32 = 3;
    let mut valor_actual = 0;

    while valor_actual <= VALOR_MAXIMO_PERMITIDO {
        println!("{}", valor_actual);
        valor_actual += 1;
    }

    // loops sobre iteradores - for in
    let una_coleccion: [f64; 3] = [6.62607015e-34, 1.618033, std::f64::consts::PI];

    // implicitamente transforma las colecciones en un iterador (https://doc.rust-lang.org/rust-by-example/trait/iter.html)
    for elemento in una_coleccion {
        println!("The value is {}", elemento);
    }

    // loop en un rango
    for valor in 0..3 {
        println!("The value is {}", valor);
    }

    // kewords loop y break
    valor_actual = 0;
    'esto_es_una_label: loop {
        println!("{}", valor_actual);
        loop {
            if valor_actual <= 3 {
                valor_actual += 1;
            } else if valor_actual == 4 {
                println!("Esto es cuatro");
                break; // Rompe el loop MAS INTERNO
            } else if valor_actual >= 10 {
                println!("Fin del camino");
                break 'esto_es_una_label; // Rompe el loop con la etiqueta "esto_es_una_label"
            }
        }
        valor_actual += 6;
    }
}

// ▶▶▶▶▶ 6. Tipos personalizados  ◀◀◀◀◀

fn las_structures() {
    // Las structures permiten agrupar datos y relacionarlos con funciones (funciones asociadas)

    // definición: nombre y campos
    struct Poblacion {
        // Notese la MAYUSCULA INICIAL
        genero: String,
        especie: String,
        numero_individuos: u64,
    }

    // creando funciones asociadas
    impl Poblacion {
        // esto es un método, un tipo especial de función asociada.
        // Requiere una instancia de un struct (note el &self)
        fn esta_extinta(&self) -> bool {
            self.numero_individuos == 0
        }
        // esta no requiere una instancia
        fn homosapiens(numero_individuos: u64) -> Poblacion {
            Poblacion {
                genero: "Homo".to_string(),
                especie: "spiens".to_string(),
                numero_individuos,
            }
        }
    }

    // instanciando structures
    let humanos_actuales = Poblacion::homosapiens(8_057_743_981); // note como se llama esta funcion asociada
    println!(
        "Especie: {}{}\n\t- Extinta: {}",
        humanos_actuales.genero,
        humanos_actuales.especie,
        humanos_actuales.esta_extinta() // notese como se llama un método
    )

    // Hay tipos especiales de structure, tambien una variedad de shorthands y formas de actualizar
    // o generar instancias apartir de otras. Pero se requiere entender como funciona el ownership system
    // las referencias, y  las diferencias entre copiar y mover una variable
}

fn los_enums() {
    // Las enumeraciones vienen bien para conjuntos de valores exhaustivos y excluyentes
    // La convención es usar CamelCase para las enumeraciones y sus variantes
    enum UnEnum {
        Variante1,                                 // variante sin un tipo asociado
        Variante2(String),                         // variante asociada a un String
        _Variante3 { campo1: usize, campo2: i16 }, // Variante asociada a una Structure
    }

    // Los enums tambien tienen funciones asociadas; por ejemplo, las variantes inducen constructores
    let _tiene_asignado_variante1: UnEnum = UnEnum::Variante1;
    let _este_tiene_asignado_variante2: UnEnum = UnEnum::Variante2("Hola mundo".to_string());
}

// ▶▶▶▶▶ 7. Estructuras de control II: match control flow  ◀◀◀◀◀

fn match_y_flujo_de_control(numero: usize) -> String {
    // Para el ejemplo usaremos este enum
    enum Numero {
        Par(usize),
        Impar(usize),
    }

    impl Numero {
        fn nuevo(valor: usize) -> Numero {
            if valor % 2 == 0 {
                Numero::Par(valor)
            } else {
                Numero::Impar(valor)
            }
        }
    }

    let un_numero = Numero::nuevo(numero);

    // la keyword match viene seguida de una EXPRESSION y una colección de ramas o brazos (ARMS)
    match un_numero {
        Numero::Par(valor) => format!("{valor} es par"), // cada brazo tiene la forma: PATRÓN => EXPRESIÓN
        Numero::Impar(valor) => format!("{valor} es impar"), // El compilador evalua que el match sea exhaustivo
    }
}

// ▶▶▶▶▶ 8. Otros tipos de la biblioteca estándar ◀◀◀◀◀

fn uso_de_option() {
    // El tipo Option es un Enum con dos variantes: None y Some(value)
    // Por ejemplo, el método checked_add solo retorna un valor si no hay integer overflow
    let numero1: u8 = 255;
    let numero2: u8 = 50;
    let suma = numero1.checked_add(numero2);

    match suma {
        Option::None => println!("Sobrecarga de enteros!"),
        Option::Some(valor) => println!("El resultado es {}", valor),
    };
}
fn uso_de_vectores() {
    // Los vectores son colecciones de valores de un mismo tipo y almacenadas en memoria uno seguido del otro

    // Notese que son de tamaño variable
    let mut esto_es_un_vector: Vec<usize> = Vec::new();
    assert_eq!(0, esto_es_un_vector.len());
    esto_es_un_vector.push(123);
    assert_eq!(1, esto_es_un_vector.len());

    //Tambien puede inicializarse vectores con datos
    let esto_es_otro_vector: Vec<usize> = vec![3, 1, 4, 1, 5];
    assert_eq!(5, esto_es_otro_vector.len());

    // Leer datos de un vector
    let _lectura_con_indices = esto_es_otro_vector[2];
    let _lectura_con_get = match esto_es_otro_vector.get(2) {
        Some(value) => *value,
        None => 0,
    };
}

fn uso_de_hashmaps() {
    // Es una implementación de diccionario: almacena pares de llaves y valores.
    // No esta en el preludio (https://doc.rust-lang.org/std/prelude/index.html),
    // por lo que debe traerse con la keyword 'use'
    use std::collections::HashMap;

    // Un HashMap vacio
    let mut numeros_atomicos: HashMap<String, u8> = HashMap::new();

    // Agregando algunos datos
    numeros_atomicos.insert("C".to_string(), 12);
    numeros_atomicos.insert("P".to_string(), 255);

    // Actualiza la key, o la agrega sí no está
    numeros_atomicos.entry("P".to_string()).or_insert(15);

    // Leer valores con get
    let _numero_oxigeno = match numeros_atomicos.get("O") {
        Some(valor) => *valor,
        None => 0,
    };
}

// ▶▶▶▶▶ 9.Manejo de errores  ◀◀◀◀◀

// panic! y Result son la interfaz primaria para el manejo de errores

fn macro_panic() {
    // Errores no esperados, como tratar de acceder a posiciones de memoria no validas
    // llaman al macro panic!, este limpia el stack y cierra el programa

    let _un_vector: Vec<usize> = vec![0, 1, 1, 2, 3];

    // La siguiente linea genera un error (para observarlo, descomentarla):
    // _un_vector[7];

    // Tambien el usuario pudee llamar panic! (descomentarla la siguiente linea para observarlo):
    // panic!("¡Esto fue un craso error!");
}
use std::str::FromStr;
fn tipo_result() {
    // Se pueden manejar errores en Runtime anticipados con el tipo Result
    // Result es un Enum, con variantes:
    //          - Ok(T), T es un genérico, es el tipo esperado
    //          - Err(E), E es un valor de error

    // Devuelve un Result<T, Err>
    let _ = char::from_str("a");

    // Sí el Result es un Err, llama panic! con el mensaje especificado
    let un_caracter1 = char::from_str("a").expect("Un mensaje");
    assert_eq!('a', un_caracter1);

    // En lugar de llamar panic! le da un valor por defecto en caso de Error;
    let un_caracter2 = char::from_str("esto da un error").unwrap_or('🦀');
    assert_eq!('🦀', un_caracter2);
}

use std::char::ParseCharError;
fn propagacion_de_errores() -> Result<usize, ParseCharError> {
    // Para propagar errores basta con devolver el Result
    let esto_es_un_result = char::from_str("a");

    // Se puede usar pattern matching, o el operador ?
    // Sí es un Ok, devuelve el valor, síno sale de la función y devuelve Err(e)
    let caracter: char = esto_es_un_result?;

    if caracter.is_ascii_control() {
        Ok(500)
    } else {
        Ok(1)
    }
}

